import os
os.environ["GLOG_minloglevel"] = "2"  # suppress mediapipe warnings

import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import numpy as np
import time
import base64
import requests
import json
import threading

from config import GROQ_API_KEY, GROQ_MODEL, IDLE_TIMEOUT, ACTION_COOLDOWN
from gestures import fingers_up, is_drawing, is_selecting
from ai import trigger_guess, ai_result, ai_thinking, ai_show_until
from ui import draw_ui, check_ui_click, COLORS, BRUSH_SIZES

# ─── MediaPipe Setup ──────────────────────────────────────────────────────────
base_options = python.BaseOptions(model_asset_path='assets/hand_landmarker.task')
options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1,
    min_hand_detection_confidence=0.7,
    min_hand_presence_confidence=0.7,
    min_tracking_confidence=0.7
)
detector = vision.HandLandmarker.create_from_options(options)

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
h, w = frame.shape[:2]

# ─── Canvas & Drawing State ───────────────────────────────────────────────────
canvas         = np.zeros((h, w, 3), dtype=np.uint8)
prev_x, prev_y = None, None
current_color_idx = 0
current_brush_idx = 1

# ─── AI State ─────────────────────────────────────────────────────────────────
last_draw_time = time.time()
last_action_time = 0

# ─── Main Loop ────────────────────────────────────────────────────────────────
print("🎨 AI Finger Paint — Powered by Groq Llama 4 Scout Vision")
print("   ☝  One finger  = Draw")
print("   ✌  Two fingers = Select UI buttons")
print("   G = Force guess  |  C = Clear canvas  |  Q = Quit")
print("   Auto-guesses 2.5s after you stop drawing\n")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame  = cv2.flip(frame, 1)
    rgb    = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_img = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
    results = detector.detect(mp_img)
    currently_drawing = False

    if results.hand_landmarks:
        lm = results.hand_landmarks[0]
        ix = int(lm[8].x * w)
        iy = int(lm[8].y * h)
        draw_mode   = is_drawing(lm)
        select_mode = is_selecting(lm)
        color_name, color_val = COLORS[current_color_idx]
        brush_r = BRUSH_SIZES[current_brush_idx]

        if select_mode:
            now = time.time()
            if now - last_action_time > ACTION_COOLDOWN:
                action = check_ui_click(ix, iy, current_color_idx, current_brush_idx)
                if action:
                    if action[0] == 'color':
                        current_color_idx = action[1]
                    elif action[0] == 'brush':
                        current_brush_idx = action[1]
                    elif action[0] == 'clear':
                        canvas[:] = 0
                        import ai; ai.ai_result = None
                    elif action[0] == 'guess' and not ai_thinking:
                        trigger_guess(canvas, w, h)
                        last_draw_time = time.time() + 999
                    last_action_time = now
            prev_x, prev_y = None, None

        elif draw_mode and ix > 108:
            currently_drawing = True
            last_draw_time    = time.time()
            import ai; ai.ai_result = None
            if prev_x is not None:
                is_eraser = color_name == "Eraser"
                draw_col  = (0, 0, 0) if is_eraser else color_val
                r         = brush_r * 4 if is_eraser else brush_r
                cv2.line(canvas, (prev_x, prev_y), (ix, iy), draw_col, r * 2)
                cv2.circle(canvas, (ix, iy), r, draw_col, -1)
            prev_x, prev_y = ix, iy
        else:
            prev_x, prev_y = None, None

        cv2.circle(frame, (ix, iy), BRUSH_SIZES[current_brush_idx], COLORS[current_color_idx][1], 2)
        cv2.circle(frame, (ix, iy), 3, (255, 255, 255), -1)
    else:
        prev_x, prev_y = None, None

    # Auto-guess after idle
    if (not currently_drawing
            and not ai_thinking
            and ai_result is None
            and time.time() - last_draw_time > IDLE_TIMEOUT):
        gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
        if cv2.countNonZero(gray) > 200:
            trigger_guess(canvas, w, h)
            last_draw_time = time.time() + 999

    display = draw_ui(frame, canvas, h, w, current_color_idx, current_brush_idx)
    cv2.imshow("🎨 AI Finger Paint — Groq Vision", display)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('c'):
        canvas[:] = 0
        import ai; ai.ai_result = None
    elif key == ord('g') and not ai_thinking:
        trigger_guess(canvas, w, h)
        last_draw_time = time.time() + 999

cap.release()
cv2.destroyAllWindows()

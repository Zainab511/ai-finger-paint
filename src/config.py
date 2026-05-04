# ─── config.py ───────────────────────────────────────────────────────────────
# Central configuration for AI Finger Paint.
# Copy .env.example to .env and fill in your keys.

import os
from dotenv import load_dotenv

load_dotenv()

# Groq API
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
GROQ_MODEL   = os.getenv("GROQ_MODEL", "meta-llama/llama-4-scout-17b-16e-instruc")

# Camera
CAMERA_INDEX = int(os.getenv("CAMERA_INDEX", "0"))

# MediaPipe thresholds
HAND_DETECTION_CONFIDENCE = float(os.getenv("HAND_DETECTION_CONFIDENCE", "0.7"))
HAND_PRESENCE_CONFIDENCE  = float(os.getenv("HAND_PRESENCE_CONFIDENCE",  "0.7"))
HAND_TRACKING_CONFIDENCE  = float(os.getenv("HAND_TRACKING_CONFIDENCE",  "0.7"))
NUM_HANDS                 = int(os.getenv("NUM_HANDS", "1"))

# App behaviour
IDLE_TIMEOUT     = float(os.getenv("IDLE_TIMEOUT",     "2.5"))   # seconds before auto-guess
ACTION_COOLDOWN  = float(os.getenv("ACTION_COOLDOWN",  "0.7"))   # UI click debounce
AI_SHOW_DURATION = float(os.getenv("AI_SHOW_DURATION", "7.0"))   # seconds to show result
MIN_PIXELS       = int(os.getenv("MIN_PIXELS",         "200"))   # min canvas pixels to guess

# 🏗️ Architecture — AI Finger Paint

## System Overview

```
┌─────────────────────────────────────────────────────┐
│                  USER'S BROWSER                     │
│                                                     │
│  ┌─────────────┐   ┌──────────────┐                 │
│  │ HTML Canvas │   │ MediaPipe.js │ ← CDN           │
│  │ (drawing)   │   │ (hand track) │                 │
│  └──────┬──────┘   └──────┬───────┘                 │
│         │                 │                         │
│         └────── JS ───────┘                         │
│                  │                                  │
│         POST /guess  (base64 JPEG)                  │
└──────────────────┼──────────────────────────────────┘
                   │  HTTPS
┌──────────────────▼──────────────────────────────────┐
│              RENDER.COM (free tier)                 │
│                                                     │
│  FastAPI (Python)                                   │
│  ├── GET  /          → serves index.html            │
│  ├── GET  /health    → uptime check                 │
│  └── POST /guess     → calls Groq API               │
│                           │                         │
└───────────────────────────┼─────────────────────────┘
                            │  HTTPS + Bearer token
                ┌───────────▼────────────┐
                │   GROQ CLOUD API       │
                │   Llama 4 Scout Vision │
                │   (image → JSON)       │
                └────────────────────────┘
```

---

## Component Breakdown

### Backend (`backend/`)

| File | Role |
|------|------|
| `main.py` | FastAPI app, routes, static file serving, CORS |
| `ai.py` | Async Groq API call, prompt, JSON parsing, error handling |

**Key decisions:**
- `httpx.AsyncClient` for non-blocking Groq calls (FastAPI async)
- API key stored server-side only — never exposed to frontend
- CORS `allow_origins=["*"]` acceptable since no auth/user data stored

### Frontend (`frontend/index.html`)

Single-file, zero build step. Sections:

| Section | What it does |
|---------|--------------|
| CSS variables | Theming, dark mode |
| Sidebar UI | Color swatches, brush sizes, buttons |
| `<canvas id="drawCanvas">` | Where strokes are drawn |
| `<canvas id="gestureCanvas">` | Overlays fingertip cursor (transparent) |
| `<video id="videoEl">` | Hidden, feeds MediaPipe |
| Mouse/Touch handlers | `mousedown/move/up`, `touchstart/move/end` |
| `onHandResults()` | MediaPipe callback → gesture logic |
| `triggerGuess()` | Sends canvas to `/guess`, shows result |

---

## Data Flow — Guess Request

```
1. User stops drawing (2.5s idle timer fires)
2. JS calls canvasToBase64()
   - Creates offscreen canvas with white bg
   - Composites drawCanvas on top
   - Exports as JPEG base64 string
3. fetch('POST /guess', { image_b64: "..." })
4. FastAPI receives GuessRequest pydantic model
5. ai.py builds Groq payload with vision prompt
6. Groq returns JSON: { label, emoji, reaction, hype }
7. FastAPI returns JSON to browser
8. JS updates resultCard + history list
```

---

## Gesture Logic

```
MediaPipe landmark 8  = index fingertip
MediaPipe landmark 12 = middle fingertip

fingersUp() checks:
  - Thumb: tip.x < joint3.x  (mirrored frame)
  - Fingers: tip.y < pip.y   (up = lower y value)

Gestures:
  index up, middle down  → DRAW mode
  index up, middle up    → SELECT mode
  anything else          → neutral (schedules auto-guess)
```

---

## Deployment

- **Platform:** Render free tier (web service)
- **Build:** `pip install -r requirements.txt`
- **Start:** `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
- **Env vars set in Render dashboard:** `GROQ_API_KEY`
- **Static files:** FastAPI serves `frontend/` directory at `/static`, `index.html` at `/`

---

## Tech Choices & Rationale

| Choice | Reason |
|--------|--------|
| FastAPI over Flask | Native async, Pydantic validation, auto docs |
| httpx over requests | Async HTTP — won't block FastAPI event loop |
| Single HTML file frontend | Zero build step, easy to deploy, no Node.js needed |
| MediaPipe.js from CDN | No server-side webcam needed |
| Groq over OpenAI | Faster inference, free tier available |
| Render over Railway | More generous free tier for Python web services |

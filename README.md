# 🎨 AI Finger Paint

> Draw with your mouse, touch, or hand gestures — Groq Llama 4 Vision guesses what you drew!

![Demo](docs/demo-placeholder.gif)

## ✨ Features

- 🖱️ **Mouse & Touch Drawing** — works on any device, no setup needed
- ✋ **Hand Gesture Mode** — draw with your index finger via webcam (MediaPipe.js)
- 🤖 **AI Guessing** — Groq Llama 4 Scout Vision identifies your sketch instantly
- 🎨 **7 Colors + Eraser** — full color palette with 4 brush sizes
- ⏱️ **Auto-Guess** — AI triggers automatically 2.5s after you stop drawing
- 📜 **History Panel** — tracks your last 8 guesses
- 📱 **Mobile Responsive** — works on phones and tablets

---

## 🏗️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML5 + CSS3 + Vanilla JS |
| Hand Tracking | MediaPipe.js (runs in browser) |
| Backend | FastAPI + Uvicorn (Python) |
| AI Vision | Groq API — Llama 4 Scout 17B |
| Deployment | Render (free tier) |

---

## 🚀 Quick Start (Local)

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/ai-finger-paint.git
cd ai-finger-paint
```

### 2. Set up Python environment
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Add your Groq API key
```bash
cp .env.example .env
# Edit .env and paste your GROQ_API_KEY
```
Get a free key at: https://console.groq.com

### 4. Run the server
```bash
uvicorn backend.main:app --reload --port 8000
```

### 5. Open in browser
```
http://localhost:8000
```

---

## ☁️ Deploy to Render (Free)

### Step 1 — Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/ai-finger-paint.git
git push -u origin main
```

### Step 2 — Create Render Web Service
1. Go to [render.com](https://render.com) → **New** → **Web Service**
2. Connect your GitHub repo
3. Render auto-detects `render.yaml` ✅

### Step 3 — Set environment variable
In Render dashboard → **Environment** tab:
```
GROQ_API_KEY = your_actual_groq_api_key
```

### Step 4 — Deploy
Click **Deploy** — Render builds and starts your app.
Your live URL will be: `https://ai-finger-paint.onrender.com`

> ⚠️ **Free tier note:** Render spins down after 15min of inactivity.
> First request after sleep takes ~30s to wake up. This is normal.

---

## 🕹️ How to Use

### Mouse / Touch Mode (default)
| Action | Result |
|--------|--------|
| Click + drag | Draw |
| Select color swatch | Change color |
| Select brush size | Change brush |
| Click CLEAR | Wipe canvas |
| Click GUESS! | Force AI guess |
| Stop drawing 2.5s | Auto-guess |

### Hand Gesture Mode
| Gesture | Action |
|---------|--------|
| ☝️ Index finger up | Draw |
| ✌️ Index + middle up | Select UI (hover over swatches) |
| Stop moving | Auto-guess after 2.5s |

---

## 📁 Project Structure

```
ai-finger-paint/
├── backend/
│   ├── __init__.py
│   ├── main.py          # FastAPI app + routes
│   └── ai.py            # Groq Vision API integration
├── frontend/
│   └── index.html       # Complete frontend (single file)
├── docs/
│   ├── ARCHITECTURE.md  # System design
│   ├── BACKLOG.md       # Agile user stories + sprints
│   └── CONTRIBUTING.md  # How to contribute
├── .env.example         # Environment variable template
├── .gitignore
├── render.yaml          # Render deployment config
├── requirements.txt
└── README.md
```

---

## 🧪 API Reference

### `POST /guess`
Accepts a base64-encoded image, returns AI recognition result.

**Request:**
```json
{
  "image_b64": "<base64 JPEG string>"
}
```

**Response:**
```json
{
  "label": "house",
  "emoji": "🏠",
  "reaction": "🔥",
  "hype": "Amazing house!"
}
```

### `GET /health`
```json
{ "status": "ok" }
```

---

## 🗺️ Agile Roadmap

| Sprint | Focus | Status |
|--------|-------|--------|
| Sprint 1 | Core drawing + AI guessing | ✅ Complete |
| Sprint 2 | Hand gestures + Render deploy | 🔄 In Progress |
| Sprint 3 | Polish, mobile, error handling | ⬜ Planned |

See full backlog → [`docs/BACKLOG.md`](docs/BACKLOG.md)

---

## 🤝 Contributing

See [`docs/CONTRIBUTING.md`](docs/CONTRIBUTING.md)

---

## 📄 License

MIT © 2025

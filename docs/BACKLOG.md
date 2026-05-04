# 📋 Product Backlog — AI Finger Paint

> SDLC Model: Agile Scrum | Sprints: 3 × 1-week | Team: 1-2 devs

---

## 🗂️ Epics

| ID | Epic | Description |
|----|------|-------------|
| E1 | Core Drawing | Canvas, brush, color, eraser |
| E2 | AI Recognition | Groq Vision integration |
| E3 | Hand Gestures | MediaPipe.js in browser |
| E4 | Deployment | Render CI/CD, env config |
| E5 | UX Polish | History, animations, mobile |

---

## 📌 User Stories

### Epic E1 — Core Drawing

| ID | Story | Points | Priority |
|----|-------|--------|----------|
| US-01 | As a user, I can draw on a canvas using my mouse so that I can create sketches | 3 | High |
| US-02 | As a user, I can draw using touch on mobile so that I can use the app on my phone | 2 | High |
| US-03 | As a user, I can pick from 7 colors + eraser so that I can draw with variety | 2 | High |
| US-04 | As a user, I can choose 4 brush sizes so that I can control stroke thickness | 1 | Medium |
| US-05 | As a user, I can clear the canvas with one click so that I can start over | 1 | High |

### Epic E2 — AI Recognition

| ID | Story | Points | Priority |
|----|-------|--------|----------|
| US-06 | As a user, AI automatically guesses my drawing after I stop so that I get instant feedback | 5 | High |
| US-07 | As a user, I can manually trigger a guess by clicking GUESS! so that I can control timing | 2 | High |
| US-08 | As a user, I see the label, emoji, reaction and hype message so that the result feels fun | 3 | High |
| US-09 | As a user, I see a loading spinner while AI is thinking so that I know it's working | 1 | Medium |
| US-10 | As a user, I see my last 8 guesses in a history panel so that I can track my session | 2 | Low |

### Epic E3 — Hand Gestures

| ID | Story | Points | Priority |
|----|-------|--------|----------|
| US-11 | As a user, I can draw using my index finger in front of the webcam so that I get the original experience | 8 | High |
| US-12 | As a user, I can switch between mouse mode and gesture mode with a tab so that I can choose my preferred input | 3 | High |
| US-13 | As a user, two-finger gesture selects colors/brushes so that I don't need to use the mouse in gesture mode | 5 | Medium |
| US-14 | As a user, I see a live fingertip cursor on the canvas so that I know where I'm drawing | 2 | Medium |

### Epic E4 — Deployment

| ID | Story | Points | Priority |
|----|-------|--------|----------|
| US-15 | As a developer, the app deploys to Render with one push so that deployment is automated | 5 | High |
| US-16 | As a developer, the GROQ_API_KEY is set via environment variable so that secrets are safe | 2 | High |
| US-17 | As a developer, there is a /health endpoint so that Render can monitor uptime | 1 | Medium |

### Epic E5 — UX Polish

| ID | Story | Points | Priority |
|----|-------|--------|----------|
| US-18 | As a user, the UI works on mobile screens so that I can use it on any device | 3 | Medium |
| US-19 | As a user, the result panel animates in so that the reveal feels satisfying | 2 | Low |
| US-20 | As a user, I see a gesture mode indicator overlay so that I know my current gesture | 1 | Low |

---

## 🏃 Sprint Plans

### Sprint 1 — Foundation (Week 1)
**Goal:** Working local app with drawing + AI guessing

| Story | Owner | Status |
|-------|-------|--------|
| US-01 Mouse drawing | Dev | ✅ Done |
| US-02 Touch drawing | Dev | ✅ Done |
| US-03 Color palette | Dev | ✅ Done |
| US-04 Brush sizes   | Dev | ✅ Done |
| US-05 Clear canvas  | Dev | ✅ Done |
| US-06 Auto-guess    | Dev | ✅ Done |
| US-07 Manual guess  | Dev | ✅ Done |
| US-08 Result display| Dev | ✅ Done |
| US-09 Spinner       | Dev | ✅ Done |

**Velocity:** 20 points

---

### Sprint 2 — Gesture + Deploy (Week 2)
**Goal:** Hand gesture mode + live on Render

| Story | Owner | Status |
|-------|-------|--------|
| US-11 Webcam drawing | Dev | 🔄 In Progress |
| US-12 Mode tabs      | Dev | ✅ Done |
| US-13 Two-finger select | Dev | 🔄 In Progress |
| US-14 Finger cursor  | Dev | ✅ Done |
| US-15 Render deploy  | Dev | ⬜ Todo |
| US-16 Env var secrets| Dev | ✅ Done |
| US-17 /health route  | Dev | ✅ Done |

**Velocity target:** 26 points

---

### Sprint 3 — Polish + Stabilise (Week 3)
**Goal:** Production-ready, mobile-responsive, tested

| Story | Owner | Status |
|-------|-------|--------|
| US-10 History panel  | Dev | ✅ Done |
| US-18 Mobile layout  | Dev | ✅ Done |
| US-19 Result animation | Dev | ⬜ Todo |
| US-20 Gesture overlay | Dev | ✅ Done |
| — Write unit tests   | Dev | ⬜ Todo |
| — Error handling hardening | Dev | ⬜ Todo |

**Velocity target:** 18 points

---

## ✅ Definition of Done

A story is DONE when:
- [ ] Feature works in Chrome and Firefox
- [ ] Works on mobile viewport (375px wide)
- [ ] No console errors
- [ ] Code reviewed (self-review for solo dev)
- [ ] Deployed to Render and verified live

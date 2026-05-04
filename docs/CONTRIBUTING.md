# 🤝 Contributing to AI Finger Paint

Thanks for your interest! This project follows a lightweight Agile workflow.

---

## 🌿 Branch Strategy

```
main           → production (auto-deploys to Render)
dev            → integration branch
feature/US-XX  → one branch per user story
bugfix/short-description
```

**Example:**
```bash
git checkout -b feature/US-13-two-finger-select
```

---

## 📋 Workflow

1. Pick a story from `docs/BACKLOG.md` marked ⬜ Todo
2. Create a branch from `dev`
3. Build + test locally
4. Open a Pull Request into `dev`
5. Self-review checklist (see below)
6. Merge → `dev` deploys to staging
7. At sprint end, merge `dev` → `main`

---

## ✅ PR Checklist

Before merging, confirm:
- [ ] Feature works in Chrome and Firefox
- [ ] Mobile viewport (375px) tested
- [ ] No `console.error` messages
- [ ] Backend: new routes have docstrings
- [ ] `.env` not committed
- [ ] `BACKLOG.md` story updated to ✅ Done

---

## 🐛 Reporting Bugs

Open a GitHub Issue with:
- Browser + OS
- Steps to reproduce
- Expected vs actual behaviour
- Screenshot if possible

---

## 💡 Suggesting Features

Open a GitHub Issue with the `enhancement` label.
Include: user story format — *"As a [user], I want [feature] so that [benefit]"*

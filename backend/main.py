import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from backend.ai import guess_drawing

app = FastAPI(title="AI Finger Paint", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve frontend
app.mount("/static", StaticFiles(directory="frontend"), name="static")

class GuessRequest(BaseModel):
    image_b64: str  # base64 JPEG/PNG from canvas

@app.get("/")
async def root():
    return FileResponse("frontend/index.html")

@app.post("/guess")
async def guess(req: GuessRequest):
    if not req.image_b64:
        raise HTTPException(status_code=400, detail="No image provided")
    result = await guess_drawing(req.image_b64)
    return result

@app.get("/health")
async def health():
    return {"status": "ok"}

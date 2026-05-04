import os
import json
import httpx
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
GROQ_MODEL   = os.getenv("GROQ_MODEL", "meta-llama/llama-4-scout-17b-16e-instruct")

PROMPT = (
    "This is a finger-drawn sketch on a white background. "
    "Identify what was drawn in ONE short word or phrase "
    "(e.g. 'house', 'cat', 'star', 'heart', 'tree', 'car', 'sun', 'fish', 'flower'). "
    "Reply ONLY with valid JSON, no extra text, no markdown backticks:\n"
    "{\"label\": \"house\", \"emoji\": \"🏠\", \"reaction\": \"🔥\", \"hype\": \"Amazing house!\"}\n\n"
    "Rules:\n"
    "- label: what was drawn (1-3 words, lowercase)\n"
    "- emoji: single best matching emoji\n"
    "- reaction: one fun celebratory emoji (pick from: 👏 🎉 🔥 ✨ 👍 🤩 😍 💯 🌟 😎)\n"
    "- hype: short fun hype phrase, max 5 words\n"
    "If unrecognizable: {\"label\":\"mystery\",\"emoji\":\"🤔\",\"reaction\":\"👀\","
    "\"hype\":\"Picasso would be confused\"}"
)

async def guess_drawing(image_b64: str) -> dict:
    """Send base64 image to Groq Vision and return parsed result."""
    if not GROQ_API_KEY:
        return {
            "label": "error",
            "emoji": "😵",
            "reaction": "🔧",
            "hype": "No API key set!"
        }

    payload = {
        "model": GROQ_MODEL,
        "max_tokens": 120,
        "temperature": 0.6,
        "messages": [{
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{image_b64}"}
                },
                {
                    "type": "text",
                    "text": PROMPT
                }
            ]
        }]
    }

    try:
        async with httpx.AsyncClient(timeout=20.0) as client:
            resp = await client.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {GROQ_API_KEY}",
                    "Content-Type": "application/json"
                },
                json=payload
            )
        data = resp.json()
        if resp.status_code != 200:
            raise Exception(f"Groq HTTP {resp.status_code}: {data}")

        text = data["choices"][0]["message"]["content"].strip()
        text = text.replace("```json", "").replace("```", "").strip()
        parsed = json.loads(text)

        return {
            "label":    parsed.get("label",    "mystery"),
            "emoji":    parsed.get("emoji",    "🤔"),
            "reaction": parsed.get("reaction", "👀"),
            "hype":     parsed.get("hype",     "Interesting...")
        }

    except json.JSONDecodeError as e:
        return {"label": "mystery", "emoji": "🤔", "reaction": "👀",
                "hype": "Brain glitched, try again!"}
    except Exception as e:
        print(f"Groq error: {e}")
        return {"label": "error", "emoji": "😵", "reaction": "🔧",
                "hype": "Something went wrong!"}

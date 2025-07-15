# llm.py
import aiohttp
import os

API_KEY = os.getenv("GOOGLE_API_KEY")
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

async def send_request(prompt: str) -> str:
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }
    headers = {"Content-Type": "application/json"}

    async with aiohttp.ClientSession() as session:
        async with session.post(API_URL, json=payload, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                return data["candidates"][0]["content"]["parts"][0]["text"]
            else:
                return f"Error {response.status}: {await response.text()}"

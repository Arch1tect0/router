import asyncio
import aiohttp
import json
import os

API_KEY = os.getenv("GOOGLE_API_KEY")
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

async def send_request(prompt):
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    headers = {"Content-Type": "application/json"}
    
    async with aiohttp.ClientSession() as session:
        async with session.post(API_URL, json=payload, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                return data["candidates"][0]["content"]["parts"][0]["text"]
            else:
                return f"Error {response.status}: {await response.text()}"

async def main():
    if not API_KEY:
        print("Set GOOGLE_API_KEY environment variable")
        return
    
    prompt = "Hello! Can you tell me a short joke?"
    print(f"Prompt: {prompt}")
    print("-" * 30)
    
    response = await send_request(prompt)
    print(f"Response: {response}")

if __name__ == "__main__":
    asyncio.run(main())

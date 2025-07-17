# router.py
import aiohttp
import os
from agents import AGENTS

API_KEY = os.getenv("OPENROUTER_API_KEY")
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

async def route_input(user_input: str) -> str:
    agent_list = "\n".join(
        f"- {name}" for name in AGENTS.keys()
    )

    routing_prompt = (
        f"You are an intelligent router.\n\n"
        f"The following agents are available:\n"
        f"{agent_list}\n\n"
        f"User input: \"{user_input}\"\n\n"
        f"Which agent should handle this input? "
        f"Respond ONLY with the exact agent name from the list above. "
        f"No other words or explanations."
    )

    agent_name = await send_request(routing_prompt)
    agent_name = agent_name.strip()

    if agent_name in AGENTS:
        return agent_name
    else:
        return None

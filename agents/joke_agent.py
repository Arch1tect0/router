# agents/joke_agent.py
from llm import send_request

async def joke_agent(user_input: str) -> str:
    prompt = f"You are a funny assistant. Tell a short joke about: {user_input}"
    return await send_request(prompt)

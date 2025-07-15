# agents/marketing_agent.py
from llm import send_request

async def marketing_agent(user_input: str) -> str:
    prompt = f"You are a marketing expert. Write a short, catchy marketing blurb about: {user_input}"
    return await send_request(prompt)

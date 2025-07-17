# agents/data_loader_agent.py

from core.llm import send_request

async def data_loader_agent(user_input: str) -> str:
    prompt = f"You are a data assistant. Help me with this task: {user_input}"
    return await send_request(prompt)

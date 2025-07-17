from core.llm import send_request
from agents import AGENTS

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


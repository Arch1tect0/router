import asyncio
from agents import AGENTS
from router import route_input

async def main():
    user_input = input("Enter your request: ")

    agent_name = await route_input(user_input)

    if agent_name:
        print(f"✅ Routing to agent: {agent_name}")
        result = await AGENTS[agent_name](user_input)
        print(f"Result: {result}")
    else:
        print("❌ Sorry, no suitable agent found.")

if __name__ == "__main__":
    asyncio.run(main())

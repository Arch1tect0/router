import asyncio
from agents import AGENTS

async def main():
    print("Available agents:", list(AGENTS.keys()))
    for agent_name in AGENTS:
        print(f"\n🤖 Calling agent: {agent_name}")
        result = await AGENTS[agent_name]("summer vacations")
        print(result)

if __name__ == "__main__":
    asyncio.run(main())

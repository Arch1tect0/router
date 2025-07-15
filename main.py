from agents.joke_agent import joke_agent
import asyncio
import os

async def main():
    
    print("🎭 Testing Joke Agent...")
    joke = await joke_agent("summer vacations")
    print(joke)

if __name__ == "__main__":
    asyncio.run(main())

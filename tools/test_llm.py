import asyncio
from core.llm import send_request

async def main():
    prompt = "Tell me a fun fact about space."
    response = await send_request(prompt)
    print("LLM Response:", response)

if __name__ == "__main__":
    asyncio.run(main())


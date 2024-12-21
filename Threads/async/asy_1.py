import asyncio

async def say_hello():
    print("Hello!")
    await asyncio.sleep(3)
    print("World!")
import asyncio

async def say_hello():
    print("Hello!")
    await asyncio.sleep(3)
    print("Dear")

async def greet():
    return "Hiiii!"

async def main():
    message = await greet()
    print(message)
    await say_hello()


asyncio.run(main())


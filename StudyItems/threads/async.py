import threading
import asyncio

# async def main():
#     task = asyncio.create_task(other_function())
#     print("A")
#     #await asyncio.sleep(1)
#     #await asyncio.sleep(1)
#     #await other_function()
#     print("B")
#     await task

# async def other_function():
#     print("1")
#     await asyncio.sleep(2)
#     print("2")

# asyncio.run(main())

async def main():
    task = asyncio.create_task(other_function())
    #await task
    #return_value = await task
    print("A")
    #await asyncio.sleep(1)
    print("B")
    return_value = await task
    print(f"value returned from other func is {return_value}")

async def other_function():
    print("1")
    await asyncio.sleep(2)
    print("2")
    return 10 


asyncio.run(main())
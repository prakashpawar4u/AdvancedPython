import asyncio

async def long_task():
    print("Long task started.")
    await asyncio.sleep(5)
    print("Long task completed.")

async def main():
    try:
        # Timeout set to 3 seconds, which will cause an exception
        await asyncio.wait_for(long_task(), timeout=3)
    except asyncio.TimeoutError:
        print("The long task timed out!")

asyncio.run(main())
    
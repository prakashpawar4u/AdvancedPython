import asyncio
import time


async def async_task(name, delay):
    print(f'Started {name}')
    await asyncio.sleep(delay)
    print(f'Finished {name} after {delay} seconds')


async def main():
    tasks = [
        async_task("Task 1", 2),
        async_task("Task 2", 5),
        async_task("Task 3", 4),
        

    ]
    await asyncio.gather(*tasks)


start = time.time()
asyncio.run(main())
print(f"Total time: {time.time() - start:.2f} seconds")
import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(1)
    print("Task 1 finished")


async def task2():
    print("Task 2 started")
    await asyncio.sleep(2)
    print("Task 2 encountered an error!")
    raise ValueError("Something went wrong in Task 2.")

async def task3():
    print("Task 3 started.")
    await asyncio.sleep(3)
    print("Task 3 completed.")

    
async def main():
    tasks = [task1(), task2(), task3()]
    for task in tasks:
        try:
            await task
        except Exception as e:
            print(f"An error occurred in a task: {e}")

asyncio.run(main())

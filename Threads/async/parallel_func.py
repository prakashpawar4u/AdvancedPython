import asyncio

async def download_data():
    print("Starting data download...")
    await asyncio.sleep(2)  # Simulate waiting for data
    print("Data download complete!")

async def process_data():
    print("Starting data processing...")
    await asyncio.sleep(1)  # Simulate processing time
    print("Data processing complete!")

async def main():
    # Run download and processing concurrently
    await asyncio.gather(download_data(), process_data())

# Start the asyncio event loop
asyncio.run(main())



# import asyncio

# async def task1():
#     await asyncio.sleep(1)
#     print("Task 1 finished")

# async def task2():
#     await asyncio.sleep(3)
#     print("Task 2 finished")


# async def main():
#     print("Inside main method")

#     await asyncio.gather(task1(), task2())
#     print("After main method")

# asyncio.run(main())
# print("Main caller outside ")

import asyncio

async def download_file(n):
    print(f" Downloading file {n}..")
    await asyncio.sleep(2)
    print(f"File {n} downloaded Successfully")
    return f"file_{n}"

async def main():
    tasks = [download_file(i) for i in range(3)]
    results = await asyncio.gather(*tasks)
    print(results)

asyncio.run(main())


# 👉 async/await in Python is not parallel processing or multithreading.
# It’s single-threaded, single-process, but uses an event loop to switch tasks cooperatively — so it’s concurrent, not parallel.

# Each coroutine cooperates — it yields control back to the loop at each await.
# That’s why this model is called cooperative multitasking (unlike preemptive multitasking in threads).


import asyncio

async def download_file(file_name):
    print(f"Starting download for {file_name}...")
    await asyncio.sleep(2)  # Simulating download time
    print(f"Download for {file_name} completed!")

async def main():
    # Simulating multiple file downloads
    await asyncio.gather(
        download_file("file1.txt"),
        download_file("file2.txt"),
        download_file("file3.txt")
    )

asyncio.run(main())
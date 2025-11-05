import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print("#~" * 30)
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution of {func.__name__} took {execution_time:.4f} seconds")
        return result

    return wrapper


@time_it
def download_file(n):
    print(f"Downloading file {n}..")
    time.sleep(2)  # blocking sleep simulating download
    print(f"File {n} downloaded Successfully")
    return f"file_{n}"

def main():
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(download_file, i) for i in range(3)]
        results = [f.result() for f in as_completed(futures)]
    print(results)

main()

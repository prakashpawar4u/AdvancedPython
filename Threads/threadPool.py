from concurrent.futures import ThreadPoolExecutor

import time

# def task(name):
#     print(f"Task {name} starting")
#     time.sleep(2)
#     print(f"Task {name} Completed")
#     return (f"Result from {name}")

# # task("T1")
# # task("T2")

# with ThreadPoolExecutor(max_workers=3) as executor:
#     future1= executor.submit(task, 'T1')
#     future2 = executor.submit(task, 'T2')
#     future3 = executor.submit(task, 'T3')

#     print(future1.result())
#     print(future2.result())
#     print(future3.result())

#################################
# Using map with ThreadPoolExecutor
#################################

# def task(n):
#     print(f"Task {n} starting")
#     time.sleep(2)
#     return n * 2

# numbers = [1,2,3,4,5]
# with ThreadPoolExecutor(max_workers=3) as executor:
#     results=executor.map(task, numbers)

# print(list(results))


########Using Futures for Asynchronous Execution##########
from concurrent.futures import ThreadPoolExecutor, as_completed


# def task(name):
#     print(f"Task {name} started")
#     time.sleep(2)
#     return f"Task {name} completed"


# with ThreadPoolExecutor(max_workers=3) as executor:
#     futures = [executor.submit(task, n) for n in range(5)]

#     for future in as_completed(futures):
#         print(future.result())


import concurrent.futures


def poll_tl_status():
    print("Polling TL Status")
    time.sleep(5)
    return "TL Status: OK"


def poll_sync_status():
    print("Polling Sync Status")
    time.sleep(2)
    return "Sync Status: OK"


with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:

    futures = {
        executor.submit(poll_tl_status): "TL Status",
        executor.submit(poll_sync_status): "Sync Status",
    }
    try:
        for future in concurrent.futures.as_completed(futures):
            print(futures[future], future.result())
    except Exception as e:
        print(f"Exception: {e}")

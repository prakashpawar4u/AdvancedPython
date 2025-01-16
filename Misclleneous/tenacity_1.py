from Misclleneous.tenacity_1 import retry, stop_after_attempt, wait_fixed


@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def unreliable_func() -> None:
    """
    Attempts to perform an unreliable operation, retrying up to 3 times with a 2-second wait between attempts.

    Raises:
        Exception: If the operation fails after the specified retries.
    """
    print("Trying to perform an unreliable operation ....")
    raise Exception("Operation failed ")


try:
    print("Calling unreliable function")
    unreliable_func()
except Exception as e:
    print("Final Exception after retries: ", e)

import logging
import concurrent.futures
import time


# create logger object
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
log.addHandler(ch)


def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        log.info("#~" * 30)
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        log.info(f"Execution of {func.__name__} took {execution_time:.4f} seconds")
        return result

    return wrapper


@time_it
def cdm_bringup(instance, testline, setup_type):
    """
    Bring up the CDM (Control and Data Module).

    Args:
        instance: The instance of the component to bring up.
        testline: The testline identifier for the current setup.
        setup_type: The setup type (e.g., "cdm1").

    Returns:
        dict: The result of the bringup operation.
    """
    log.info("Bringup started forn CDM ")
    time.sleep(5)
    log.info("CDM bring up is done")
    return {
        "result": "success",
        "error": "",
        "output": "CDM bring up successful.",
        "setup": setup_type,
    }


@time_it
def cucp_bringup(instance, testline, setup_type):
    """
    Bring up the CUCP (Centralized Unit Control Plane).

    Args:
        instance: The instance of the component to bring up.
        testline: The testline identifier for the current setup.
        setup_type: The setup type (e.g., "cu1").

    Returns:
        dict: The result of the bringup operation.
    """
    log.info("Bringup started forn CUCP ")
    time.sleep(2)
    log.info("CUCP bring up is done")
    return {
        "result": "success",
        "error": "",
        "output": "CUCP bring up successful.",
        "setup": setup_type,
    }


@time_it
def cuup_bringup(instance, testline, setup_type):
    """
    Bring up the CUUP (Centralized Unit User Plane).

    Args:
        instance: The instance of the component to bring up.
        testline: The testline identifier for the current setup.
        setup_type: The setup type (e.g., "cu2").

    Returns:
        dict: The result of the bringup operation.
    """

    log.info("Bringup started forn CUUP ")
    time.sleep(12)

    log.info("CUUP bring up is done")
    return {
        "result": "success",
        "error": "",
        "output": "CUUP bring up successful.",
        "setup": setup_type,
    }


@time_it
def du_bringup(instance, testline, setup_type):
    """
    Bring up the DU (Distributed Unit).

    Args:
        instance: The instance of the component to bring up.
        testline: The testline identifier for the current setup.
        setup_type: The setup type (e.g., "du1").

    Returns:
        dict: The result of the bringup operation.
    """
    log.info("Bringup started forn DU ")
    time.sleep(4)
    log.info("DU bring up is done")
    return {
        "result": "success",
        "error": "",
        "output": "DU bring up successful.",
        "setup": setup_type,
    }


@time_it
def ue_bringup(instance, testline, setup_type):
    """
    Bring up the UE (User Equipment).

    Args:
        instance: The instance of the component to bring up.
        testline: The testline identifier for the current setup.
        setup_type: The setup type (e.g., "ue1").

    Returns:
        dict: The result of the bringup operation.
    """
    log.info("Bringup started forn UE ")
    time.sleep(7)
    log.info("UE bring up is done")
    return {
        "result": "success",
        "error": "",
        "output": "UE bring up successful.",
        "setup": setup_type,
    }


if __name__ == "__main__":
    try:
        status_dict = {
            "cdm": False,
            "cucp": False,
            "cuup": False,
            "du": False,
            "ue": False,
        }
        map_function = {
            "cdm": cdm_bringup,
            "cucp": cucp_bringup,
            "cuup": cuup_bringup,
            "du": du_bringup,
            "ue": ue_bringup,
        }

        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures = {
                executor.submit(map_function[key], key, "testline1", f"{key}1"): key
                for key in map_function
            }
            for future in concurrent.futures.as_completed(futures):
                status_dict[futures[future]] = future.result()
    except Exception as e:

        log.error(f"Exception: {e}")
        print(f"Exception: {e}")
    finally:
        print(status_dict)
        log.info(status_dict)
        log.info("Bring up completed")

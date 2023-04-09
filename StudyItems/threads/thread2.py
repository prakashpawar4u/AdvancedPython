import threading
import time


def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count +=1
        print("%s : %s" %(threadName, time.ctime(time.time())))

try:
    print("Inside try block ")
    print_time("Mythread", 1)
    print_time("Mythread2", 2)

    #thread.start_new1(print_time("Mythread", 1))
    print_time("Mythread2", 2)
except:
    print("error unable to start thread")
    
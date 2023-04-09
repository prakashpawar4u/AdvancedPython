from concurrent.futures import thread
import threading
import time
import logging

exitFlag = 0
class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name 
        self.counter = counter 

    
    def run(self):
        print("Starting " + self.name)
        print_time(self.name, 5, self.counter)
        print("Exiting thread",self.name)
    
def print_time(threadName, counter, delay):
    while counter: 
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print(f"{threadName}: {time.ctime()}")
        counter -= 1 


thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)


thread1.start()
thread2.start()

print("Exitting threads")


"""
def thread_func(name,delay):
    logging.info("Thread %s: starting", name)
    time.sleep(delay)
    logging.info("Thread %s: finishing", name)
    #print(f"Thread {name} is finishing")


if __name__ == "__main__":
    format = "%(asctime)s : %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    t1 = threading.Thread(target=thread_func, args=("func1",1))
    t2 = threading.Thread(target=thread_func, args=("func2",3))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    



"""



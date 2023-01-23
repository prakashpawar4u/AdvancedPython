# def mydecorator(func):
#     def wrapper():
#         print("I am decorating your function!!!")
#         func()
#     return wrapper

# #pythonic way of decorator
# @mydecorator
# def helloWorld():
#     print("Hello World!!!")

# #mydecorator(helloWorld())
# helloWorld()


import time
from unittest import result
###
def mydecorator(func):
    def wrapper(*agrgs, **kwargs):
        start = time.time()
        value = func(*agrgs,**kwargs)
        end = time.time()
        fname = func.__name__
        print(f"{fname} took {end - start} seconds to complete!")
        return value
    return wrapper

@mydecorator
def hello_func(x):
    results = 1
    for i in range(1,x):
        results *= i
    return results

hello_func(100000000)

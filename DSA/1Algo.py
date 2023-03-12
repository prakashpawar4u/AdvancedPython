import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {str((end-start)*1000)} milli seconds")
        return result
    return wrapper

@time_it
def fun1(n):
    return n*(n+1)/2
@time_it
def fun2(n):
    sum =0
    for i in range(1,n+1):
        sum = sum + i
    return sum
@time_it
def fun3(n):
    sum=0
    for i in range(1,n+1):
        for j in range(1,i+1):
            sum = sum +1
    return sum

num = 50000

print(fun1(num))
print(fun2(num))
print(fun3(num))

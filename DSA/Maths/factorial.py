def factorial(n):
    res = 1
    for i in range(2, n+1):
        res = res * i
    return res


def factRecursive(n):   
    if n == 0:
        return 1
    return n * factRecursive(n -1)

print(factRecursive(5))

# n = int(input("Enter a number for cal factorial ::"))
# print(factorial(n))

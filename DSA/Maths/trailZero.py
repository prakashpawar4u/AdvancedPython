#Naive Solution
def countZero(n):
    fact = 1
    for i in range(2, n+1):
        fact = fact * i

    res = 0
    print(fact)
    while(fact%10 == 0):
        res += 1
        fact = fact//10
    return res
print(countZero(50))

#optimized way
# def countZero(n):
#     res = 0
#     i = 5
#     while(i<=n):
#         res = res + n//i
#         i = i * 5
#     return res
# print(countZero(500))

#Naive Approach
#Time complexity O(n)
# def checkPrime(n):
#     if n==1:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True

#
# def checkPrime(n):
#     if n==1:
#         return False
#
#     i = 2
#     while(i*i <=n):
#         if n%i == 0:
#             return False
#         i+=1
#     return True

#Super Efficient

def checkPrime(n):
    if n ==1:
        return False
    if n==2 or n==3:
        return True

    if n%2==0 or n%3==0:
        return False
    i=5
    while(i*i<=n):
        if n%i==0 or n%(i+2)==0:
            return False
        i+=6
    return True


print("True") if checkPrime(171) else print("false")
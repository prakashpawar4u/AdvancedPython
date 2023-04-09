# def lcm(a,b):
#     res = max(a,b)
#     while True:
#         if res%a==0 and res%b==0:
#             return res
#         res +=1
#     return res


def gcd(a,b):
    if b ==0:
        return a
    return gcd(b,a%b)
def lcm(a,b):
    return a*b //gcd(a,b)
a = 4
b = 6
print(lcm(a,b))
#Q(axb - max(a,b))

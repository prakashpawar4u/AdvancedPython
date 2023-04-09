#Greatest Common Divisor

# def gcd(a,b):
#     while a != b:
#         if a > b:
#             a = a-b
#         else:
#             b = b-a
#     return a


#optimized
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

if __name__ == "__main__":
    a = 120
    b = 150
    print(gcd(a,b))
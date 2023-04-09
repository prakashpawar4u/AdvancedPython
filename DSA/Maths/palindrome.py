def isPal(n):
    temp = n
    rev = 0

    while temp != 0:
        id = temp % 10
        rev = rev * 10 + id
        temp = temp // 10
    return rev == n

if __name__ == "__main__":
    n = int(input("Enter a num to check if it is palidrome:"))
    print(isPal(n))
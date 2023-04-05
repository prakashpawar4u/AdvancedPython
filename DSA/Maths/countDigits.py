x = int(input("Enter Num :"))
res = 0

while x > 0:
    x = x//10
    res = res + 1

print(f"Count of digit is ::{res}")
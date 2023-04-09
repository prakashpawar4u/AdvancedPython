def comPower(x,n):
    if n==0:
        return 1
    elif n==1:
        return x
    else:
        return x**n
print(comPower(3,4))
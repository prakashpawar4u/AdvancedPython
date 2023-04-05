def sumOfNaturalNo(n):
    sum=n*(n+1)/2
    return sum

    #sn = 1 + 2   + 3   + 4   + 5
    #sn = n + n-1 + n-2 + n-3 + n-4
    #2sn = (n+1) + (n+1) + (n+1) + (n+1) + (n+1)
    #2sn = n*(n+1)
    #sn = n*(n+1)/2

n = int(input("Enter Natural Num:"))
total = sumOfNaturalNo(n)
print(f"Summation of Natural num :: {total}")
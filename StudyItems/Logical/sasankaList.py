l1 = [1,1,1,2,3,4,2,3,3,7,8]
print(f'lenght of list is :: {len(l1)}')

for i in range(len(l1)):
    # print(l1[i], len(l1)-i)
    #for j in range(len(l1)-i):
    for j in range(i+1,len(l1)):
        if l1[i]==l1[j]:
            print(f"{l1[i]} Match found")
    else:
        print()
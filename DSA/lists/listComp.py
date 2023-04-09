def getEvenOdd(l):
    even = [x for x in l if x%2==0]
    odd = [x for x in l if x%2!=0]
    return even, odd

l = [0,3,20,5,15,12,20]
even, odd = getEvenOdd(l)
print(f"EVEN:{type(even)} {even}")
print(f"ODD:{type(odd)} {odd}")


s = "geeksforgeeks"
l1 = [x for x in s if x in "aeiou"]
print(l1)

l2 = ["geeks", 'for', 'geeks']
l3=[x for x in l2 if x.startswith("g")]
print(l3)

l4 = [x*2 for x in range(6)]
print(l4)

l2 = ["geeks", 'ide','goal','for', 'geeks']
l3=[x.upper() for x in l2 if x.startswith("g")]
print(l3)

#set comprehension
l = [10,10,3,20,5,15,12,20]
s1 = {x for x in l if x%2==0}
s2 = {x for x in l if x%2!=0}
print(f"S1 ::{s1}")
print(f"S2 ::{s2}")


#dict comprehension
d = {x:x*x for x in range(6)}
print(d)

d = {x:f"ID{x}" for x in range(6)}
print(d)

l1=[101,102,103]
l2=['one', 'two','three']

dcombo= {l1[x]:l2[x]for x in range(len(l1))}
print(dcombo)

for i in range(len(l1)):
    print(i)


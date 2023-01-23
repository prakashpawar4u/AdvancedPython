import sys
l = []
for i in range(1,90000):
    l.append(i)

#print(l)

# def mygenerator(n):
#     for x in range(n):
#         yield x ** 3

# values = mygenerator(10)
# print(sys.getsizeof(values))
# for x in values:
#     print(x)



def infinite_sequence():
    result = 1
    while True:
        yield result
        result *= 5
values = infinite_sequence()


for x in range(10):
    print(f"{x} & seq ")
    values.next()
# for x in values:
#     print(x)

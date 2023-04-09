from turtle import st


stock_prices= [298, 305, 320, 301, 292]

for i in range(len(stock_prices)):
    if stock_prices[i]==301:
        print(stock_prices[i])

#Look up by value = O(n)

#insert a price at a given index
stock_prices.insert(1, 333)
print(stock_prices)

#n number of swap = O(n)

#delete element at index 1
#remove value = O(n)
stock_prices.remove(333)
print(stock_prices)

#Array DataStructure

Month = ["Jan", 'Feb', "March", "April", "May"]
exp = [2200, 2350, 2600, 2130, 2190]

print(exp[1]-exp[0])
s=0
quarter =[x for x in exp if x < 3] 
print("quarter:", quarter)

for i in range(len(exp)):
    if i <3:
        print(i)
        s+=exp[i]
print(f"Quaterly exp : {s}")



# print()
# for i, j in enumerate(exp):
#     print(i, j)


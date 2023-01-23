class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def __str__(self):
        return f"Account Owner:   {self.owner}\nAccount balance: ${self.balance}"
    
    def deposit(self,dep_amt):
        self.balance+= dep_amt
        print("Amount Creditted:{} ".format(dep_amt))
        print("Current Amount available {}".format(self.balance))
    
    def withdraw(self, wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print("withdrawn amount {}".format(wd_amt))
            print("Current Amount available {}".format(self.balance))
    
        else:
            print("Unable to withdraw, balace left is {}".format(self.balance))


#instantiate the class 
acct1 = Account("Prakash", 100)
#print Obj
print(acct1)

#print balance
print(acct1.balance)

#deposit
acct1.deposit(500)

#withdraw
acct1.withdraw(75)

#withdraw beyond limit
acct1.withdraw(1000)

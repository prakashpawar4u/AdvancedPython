# class Example:
#     def __new__(cls,n):
#         print("New is called ")

#     def __init__(self, n):
#         print("Instance created")
#         print("Num : {}".format(n))
    
#     def get_name(self):
#         print("Inside get method")

#     # def __call__(self):
#     #     print("Instance is call via special method")


# #create object 
# E = Example(10)
# #call method 
# E.get_name()


# #__new__ is the constructor and __init__ is the initializer.
#
# class Demo:
#     def __new__(cls, *args):
#         print("__new__ called")
#         return object.__new__(cls)
#
#     def __init__(self):
#         print("__init__ called")
#
# d = Demo()

class A:
    def __new__(cls, *args):
        print("Inside New Method")
        
    def __init__(self, num):
        print("__init__() call ")
        self.data = num

    def __str__(self):
        print("__str__() call")
        print("Number is {}".format(self.data))

    def __call__(self):
        num = 0
        print("In Call() func")
        print("Adding 10 to the value of data")
        num = self.data + 10
        return num
#Class A declaration

x = A(5)
x.__str__()
y = x()
print("Y is returned from {}".format(y))
#Declaration of another instance
#y = A(20)

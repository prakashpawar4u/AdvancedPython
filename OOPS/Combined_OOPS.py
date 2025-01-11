# class Person:
#     #Class variable
#     # Hidden member of MyClass
#     __hiddenVariable = 10
#     def __init__(self):
#         #instance variable
#         self.A = "Yuan"
#         self.__B = "Private"

#     def printName(self):
#         print(self.A)
#         print(self.__B)

# p = Person()
# #p.printName()
# print(p.A)
# print(p._Person__B)
# print(p._Person__hiddenVariable)
# #print(p.__B)

#
# class Test:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __str__(self):
#         return "From str method of Test: a is %s," \
#                    "b is %s" % (self.a, self.b)
#
#     def __repr__(self):
#         return "Test a:%s b:%s" % (self.a, self.b)
# t=Test(1234, 5678)
# print(t)
# print([t])
# print(t.__repr__())


# class Person(object):
#
#     # Constructor
#     def __init__(self, name):
#         self.name = name
#
#     # To get name
#     def getName(self):
#         return self.name
#
#     # To check if this person is employee
#     def isEmployee(self):
#         return False
#
#
# # Inherited or Sub class (Note Person in bracket)
# class Employee(Person):
#     #function overloading
#     # def getName(self):
#     #     self.name= "Hardcoded"
#     #     return self.name
#
#     # Here we return true
#     def isEmployee(self):
#         return True
#
#
# # Driver code
# emp = Person("Geek1")  # An Object of Person
# print(emp.getName(), emp.isEmployee())
#
# emp1 = Employee("Geek2")  # An Object of Employee
# print(emp1.getName(), emp1.isEmployee())
#
# #issubclass
# print(issubclass(Person, Employee)) #False
# print(issubclass(Employee, Person)) #True
#
# #isinstance
# print(isinstance(emp1, Person))#True
# print(isinstance(emp, Employee))#False


# Python example to show that base
# class members can be accessed in
# derived class using base class name
# class Base(object):
#
#     # Constructor
#     def __init__(self, x):
#         self.x = x
#         self.z = "Zero"
#
#     def printfunc(self):
#         print(self.z)
#
#
# class Derived(Base):
#
#     # Constructor
#     def __init__(self, x, y):
#         Base.x = x
#         self.y = y
#         self.w = "W"
#         Base.z = "Zebra"
#
#     def printXY(self):
#         # print(self.x, self.y) will also work
#         print(Base.x, self.y)
#
#
# # Driver Code
# d = Derived(30, 20)
# d.printfunc()
# print(d.w)
# #print(d.z)
# d.printXY()


# class Base:
#     def __init__(self, x, z):
#         self.x = x
#         self.x = z
#
# class Derived(Base):
#     def __init__(self,x, y, z):
#         self.y = y
#         super(Derived, self).__init__(x,z)
#
#     def printFunc(self):
#         print(f"value of x {self.x} & value of y {self.y }")
#
# d = Derived(4,10, [22345,23565])
# d.printFunc()

# class CSStudent:
#     #class variable
#     __hiddenVariable = "55"
#     _stream = "CSE"
#     def __init__(self, name, roll):
#         self.name = name
#         self.roll = roll
#
#     def printVar(self):
#         print(self._stream, self.name, self.roll)
#
# stu = CSStudent("Prakash", 123)
# stu.printVar()
# #print(stu.stream)
# print(stu._CSStudent__hiddenVariable)
# #print(stu._CSStudent_stream) #cannot be accessed
#
# print("Updating class variable ")
# stu.stream="MEC"
# stu.printVar()
#
#
# print("Updating class variable using class Name only  ")
# CSStudent._stream="MEC"
# print(stu._stream)
# stu.printVar()


# def shout(text):
#     return text.upper()
# print(shout("Hello"))
# yell = shout
#
# print(yell("Prakash"))


# def CU(text):
#     return text.upper()
#
# def DU(text):
#     return text.lower()
#
# def RU(text):
#     return text
# # def __repr__():
# #     return func
# def caller(func):
#     objcreation = func("Creating objects in called method")
#     print(objcreation, func)
#
# caller(CU)
# caller(DU)
# caller(RU)


# def create_adder(x):
#     def adder(y):
#         return x+y
#     return adder
#
# add_15 = create_adder(15)
# print(add_15)
# print(add_15(10))


# #Abstract class
# from abc import ABC, abstractmethod
#
# class Polygon(ABC):
#     @abstractmethod
#     def noofSides(self):
#         pass
#
# class Triangle(Polygon):
#     #overriding abstract method
#     def noofSides(self):
#         print("I have 3 sides")
#
# class Pentagon(Polygon):
#     def noofSides(self):
#         print("I have 5 sides")
# #driver code
# T = Triangle()
# T.noofSides()
#
# P = Pentagon()
# P.noofSides()


# import abc
# class Shape(metaclass=abc.ABCMeta):
#     @abc.abstractmethod
#     def area(self):
#         pass
#
# class Rectangle(Shape):
#     def __init__(self, x, y):
#         self.l = x
#         self.b = y
#
#     def area(self):
#         return self.l * self.b
#
# r = Rectangle(10, 20)
#
# print('area:',r.area())

##########cls method##########
#class methods give us the power to access a method using reference to class itself rather than instance of that class.
class Animal(object):
    #class variable
    count = 1
    def get_count(self):
        return self.count

    @classmethod
    def inc_count(cls):
        cls.count += 1
        return cls()

objA = Animal()
print(objA.get_count())
#print(Animal.get_count())
#TypeError: get_count() missing 1 required positional argument: 'self'

animal = Animal.inc_count()
#animal.get_count()
animal.inc_count()
#animal.get_count()
animal.inc_count()
print(animal.get_count())

##########static method##########
#static methods are like regular functions just with the fact that they belong to a class’s namespace
#As static methods do not take self and cls as parameters, they do not have access to class members and variables

class Example(object):
    def __init__(self,a, b):
        self.a = a
        self.b = b

    def get_item(self):
        print(f"value of A : {self.a} & B : {self.b}")
    @staticmethod
    def just_a_method():
        #print('Access A : ',self.a)
        print("This is static method")
ex = Example('a','b')
ex.just_a_method()
ex.get_item()

##########abstract method##########

#Abstract methods in Python are the methods that are defined
# in the base class, but do not have any implementation. The derived class must override these abstract methods in their definition. Failing to do so will cause NotImplementedError.

from abc import ABC, abstractmethod


class Polygon(ABC):

    @abstractmethod
    def noofsides(self):
        pass


class Triangle(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")

# Driver code
R = Triangle()
R.noofsides()
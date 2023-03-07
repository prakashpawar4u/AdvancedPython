from abc import ABCMeta, abstractstaticmethod
from random import choice

class FactoryDesign(Exception):
    pass

class Iperson(metaclass=ABCMeta):
    @abstractstaticmethod
    def person_method(self):
        print("Person Method invoked")

# Iobj = Iperson()
# Iobj.person_method()

class Student(Iperson):
    def __init__(self):
        self.name = "Basic Student Name"

    def person_method(self):
        print("I am a student")

class Teacher(Iperson):
    def __init__(self):
        self.name = "Basic Teacher Name"
        #print("I am a Teacher")
    
    
    def person_method(self):
        print("I am a Teacher")

# s1 = Student()
# s1.person_method()

# t1= Teacher()
# t1.person_method()

class personFactory():
    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        
        if person_type == "Teacher":
            return Teacher()
        print("Failed to invoke constructor class: Invalid person type: {person_type}")
        raise FactoryDesign("Failed to invoke constructor class: Invalid person type: {}".format(person_type))
        print("Invalid Type")
        return -1

if __name__ == "__main__":
    #print("Hello World!!!!")
    choice = input("What type of person you want to create a obj:")
    person = personFactory.build_person(choice)
    person.person_method()

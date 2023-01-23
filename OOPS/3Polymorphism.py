# class Dog:
#     def __init__(self,name):
#         self.name = name 
    
#     def speak(self):
#         return self.name + "says wooof!!!!"

# class Cat:
#     def __init__(self,name):
#         self.name = name
    
#     def speak(self):
#         return self.name + "says meauun!!!"

# sam = Dog('Sam')
# charlie = Cat("Charlie")

# def pet_speak(pet):
#     print(pet.speak())

# pet_speak(sam)
# pet_speak(charlie)

# print(sam.speak())
# print (charlie.speak())



class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass Must implement abstract method")
    
class Dog(Animal):
    def speak(self):
        return self.name + "Says Woof!!"

class Cat(Animal):
    def speak(self):
        return self.name + "Says Meaun!!"

class Horse(Animal):
    def __init__(self, name):
        print("constructor invoked for Horse:: {}".format(name))
sam = Dog("Sam")
charlie = Cat("Charlie")
chetak = Horse("Chetak")

print(sam.speak())
print(charlie.speak())
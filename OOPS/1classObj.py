# #create empty class

# class Sample:
#     pass

# x= Sample()


# class Dog:
#     def __init__(self, breed):
#         self.breed = breed
    
#     def getBreed(self):
#         print(self.breed)
    
# sam = Dog(breed="Lab")
# print(sam.breed)
# sam.getBreed()
# frank = Dog(breed = "Husky")
# frank.getBreed()


class Dog:
    species = "mammal"

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

sam = Dog("Lab", "Sam")
print(sam.name)
print(sam.species)


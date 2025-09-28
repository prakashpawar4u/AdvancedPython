class Person:
    def __init__(self, name, age, ssn):
        self.name = name           # Public attribute
        self._age = age            # Protected attribute
        self.__ssn = ssn           # Private attribute

    def public_info(self):
        return f"My name is {self.name} and I'm {self._age} years old."

    def get_ssn(self):
        return f"SSN: {self.__ssn}"   # Private accessed within class

    def set_ssn(self, new_ssn):
        self.__ssn = new_ssn

# Creating object
person = Person("Alice", 30, "123-45-6789")

# Public access
print(person.name)           # ✅ Works
print(person.public_info())  # ✅ Works

# Protected access (convention: should not be accessed outside)
print(person._age)           # ⚠️ Works, but not recommended

# Private access
try:
    print(person.__ssn)      # ❌ Will raise AttributeError
except AttributeError as e:
    print("Error accessing __ssn directly:", e)

# Accessing private using name mangling
print(person._Person__ssn)   # ✅ Works (not recommended)

# Using getter/setter for private attribute
print(person.get_ssn())      # ✅ Proper way
person.set_ssn("987-65-4321")
print(person.get_ssn())      # ✅ Updated



# class Person:
#     def __init__(self, name, age, gender):
#         self.__name = name #Private Attribute
#         self.__age = age #Private Attribute
#         self._gender = gender #Protected
    
#     @property
#     def Name(self):
#         return self.__name
    
#     @property
#     def Age(self):
#         return self.__age

#     @staticmethod
#     def myMethod():
#         print("Static Method is invoked ")



# pObj = Person("Prakash", 30, "Male")
# #name = pObj.Name() #Notworking
# print(pObj.Name) #working
# # print(pObj._Person__age)
# print(pObj.Age)
# print(pObj._Person_gender)




# Person.myMethod()
# pObj.myMethod()

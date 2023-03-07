class Person:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender
    
    @property
    def Name(self):
        return self.__name
    
    @Name.setter
    def Name(self, value):
        if value == "Bob":
            self.__name = "Default Name assigned"
        else:
            self.__name = value

    @staticmethod
    def myMethod():
        print("Static Method is invoked ")



pObj = Person("Prakash", 30, "Male")
#name = pObj.Name() #Notworking
print(pObj.Name) #working

#print(pObj.__age) #Notworking
print(pObj._Person__age)

pObj.Name = "Bobd"
print(pObj.Name) #working


Person.myMethod()
pObj.myMethod()
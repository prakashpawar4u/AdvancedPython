"""class Animal:
    def __new__(cls,legs):
        if legs == 2:
            return Biped()
        else:
            return Quadruped()

class Biped:
    def __init__(self):
        print("Initializing 2-legged animal")


class Quadruped:
    def __init__(self):
        print("Initializing 4 legged animal")



anim1 = Animal(legs=4)
print("Obj1 {}".format(anim1))
anim2 = Animal(legs=2)
print("Obj2 {}".format(anim2))

"""

class Devnote(object):
    def __str__(self):
        return "DEVNOTE"
class Dev(object):
    def __new__(arg1):
        return Devnote()
    def __init__(self):
        print("init call")

print(Dev())
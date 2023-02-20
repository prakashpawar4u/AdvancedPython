class A:
    # def __new__(cls,x):
    #     print("Inside new method {}".format(x))

    def __init__(self,x):
        print("inside __init__()")
        self.y = x
    
    def __str__(self):
        print("inside __str__")

    def __call__(self):
        print("Inside __call__")

a = A(5)
a.__str__()
a()

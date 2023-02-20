# class Singleton:
#     __instance = None
#
#     def __new__(cls):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#
#     def dbInstance(self):
#         print("This is db instance")
#
# s1 = Singleton()
# s2 = Singleton()
#
# print(s1 is s2)


#Factory Pattern:


class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing Circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing Rectangle")

class ShapeFactory:
    def create_shape(self, shape_type):
        if shape_type == "Circle":
            return Circle()
        elif shape_type == "Rectangle":
            return Rectangle()







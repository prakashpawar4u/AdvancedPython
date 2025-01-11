# class Iperson():
#     def __init__(self):
#         print("Person Constructor")

#     def new_func(tl_wrapper, cells):
#         """
#         To get the list of the cells from the test mapping for oam cases
#         @Author: AB
#         :param tl_wrapper:
#         :param cells:
#         :return: result cellList
#         """
#         print("New function called ")

# print("Hello World!!!")
# Iobj = Iperson()
# Iobj.new_func(3)


# class Singleton:
#     _instance = None

#     def __new__(cls, *args, **kwargs):
#         print("Init method is invoked")
#         if not cls._instance:
#             cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
#             return cls._instance

# s1 = Singleton()
# print("Obj1 {} is created".format(s1))
# s2 = Singleton()
# print("Obj2 {} is created".format(s2))
# print(s1 is s2)


# class Singleton:
#     __instance = None

#     def __new__(cls):
#         if cls.__instance is None:
#             print("creating.....")
#             cls.__instance = object.__new__(cls)
#         return cls.__instance

# s1 = Singleton()
# s2 = Singleton()

# print(s1)
# print(s2)
# print(s1 is s2)


import yaml


class Config:
    _instance = None
    _data = None

    def __new__(cls, filepath: str):
        if not cls._instance:
            cls._instance = super().__new__(cls)

        if filepath:
            cls._load_config(filepath)

    @classmethod
    def _load_config(cls, filepath: str):
        with open(filepath) as file:
            cls._data = yaml.safe_load(file)

    @classmethod
    def get_config(cls):
        if cls._data is None:
            raise ValueError("Config not loaded")
        return cls._data


filepath = r"C:\Users\prakash.pawar\PycharmProjects\Learnings\GitHub\AdvancedPython\YamlModification\1basic.yaml"
config1 = Config(filepath)
print(config1.get_config())

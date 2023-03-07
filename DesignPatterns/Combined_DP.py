######Singleton Pattern###########
# class Singleton:
#     __instance = None

#     def __new__(cls):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
# s1 = Singleton()
# s2 = Singleton()

# print(s1 == s2)
# print(s1 is s2)



# from abc import ABCMeta, abstractstaticmethod

# class IPerson(metaclass=ABCMeta):

#     @abstractstaticmethod
#     def print_data():
#         """implement in child class"""

# class PersonSingleton(IPerson):
#     __instance = None
#     @staticmethod
#     def get_instance():
#         if PersonSingleton.__instance == None:
#             PersonSingleton("Default Name", 0)
#         return PersonSingleton.__instance
    
#     def __init__(self, name, age):
#         if PersonSingleton.__instance != None:
#             raise Exception("Singleton cannot be instantiated again more than once")
#         else:
#             self.name = name
#             self.age = age
#             PersonSingleton.__instance = self
    
#     @staticmethod
#     def print_data():
#         print(f"Name: {PersonSingleton.__instance.name}, Age: {PersonSingleton.__instance.age}")


# p1 = PersonSingleton("Mike", 30)
# print(p1)
# p1.print_data()

#p2 = PersonSingleton("Bosco", 23)
#   raise Exception("Singleton cannot be instantiated again more than once")
#Exception: Singleton cannot be instantiated again more than once

# p2 = PersonSingleton.get_instance()
# print(p2)
# p2.print_data()


######Factory Pattern###########
# 1st Example
# class Dog:
#     def __init__(self, name):
#         self.name = name

# class Cat:
#     def __init__(self, name):
#         self.name = name

# class AnimalFactory:
#     def create_animal(self, species, name):
#         if species == 'dog':
#             return Dog(name)
#         elif species == 'cat':
#             return Cat(name)

# factory = AnimalFactory()
# dog = factory.create_animal('dog', "Bruno")
# cat = factory.create_animal("cat", "whiskey")


# from abc import ABCMeta, abstractstaticmethod

# class Iperson(metaclass=ABCMeta):
#     @abstractstaticmethod
#     def person_method():
#         """Interface method"""

# class Student(Iperson):
#     def __init__(self):
#         self.name = "Basic Student Name"
    
#     def person_method(self):
#         print("I am a student")


# class Teacher(Iperson):
#     def __init__(self):
#         self.name = "Basic Teacher Name"
    
#     def person_method(self):
#         print("I am a Teacher")

# # s1 = Student()
# # s1.person_method()

# # t1 = Teacher()
# # t1.person_method()

# class PersontFactory(Iperson):
#     @staticmethod
#     def build_person(person_type):
#         if person_type =="Student":
#             return Student()
#         elif person_type == "Teacher":
#             return Teacher()
#         else:
#             print("Invalid Type")
#             return -1

# if __name__ =="__main__":
#     choice = input("What type of person do you want to create?\n")
#     Person = PersontFactory.build_person(choice)
#     Person.person_method()  

#choice = input("Type")


#Example 3
"""
Basic video exporting example
"""

import pathlib
from abc import ABC, abstractmethod


class VideoExporter(ABC):
    """Basic representation of video exporting codec."""

    @abstractmethod
    def prepare_export(self, video_data):
        """Prepares video data for exporting."""

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Exports the video data to a folder."""


class LosslessVideoExporter(VideoExporter):
    """Lossless video exporting codec."""

    def prepare_export(self, video_data):
        print("Preparing video data for lossless export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in lossless format to {folder}.")


class H264BPVideoExporter(VideoExporter):
    """H.264 video exporting codec with Baseline profile."""

    def prepare_export(self, video_data):
        print("Preparing video data for H.264 (Baseline) export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H.264 (Baseline) format to {folder}.")


class H264Hi422PVideoExporter(VideoExporter):
    """H.264 video exporting codec with Hi422P profile (10-bit, 4:2:2 chroma sampling)."""

    def prepare_export(self, video_data):
        print("Preparing video data for H.264 (Hi422P) export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H.264 (Hi422P) format to {folder}.")


class AudioExporter(ABC):
    """Basic representation of audio exporting codec."""

    @abstractmethod
    def prepare_export(self, audio_data):
        """Prepares audio data for exporting."""

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Exports the audio data to a folder."""


class AACAudioExporter(AudioExporter):
    """AAC audio exporting codec."""

    def prepare_export(self, audio_data):
        print("Preparing audio data for AAC export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in AAC format to {folder}.")


class WAVAudioExporter(AudioExporter):
    """WAV (lossless) audio exporting codec."""

    def prepare_export(self, audio_data):
        print("Preparing audio data for WAV export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in WAV format to {folder}.")


class ExporterFactory(ABC):
    """
    Factory that represents a combination of video and audio codecs.
    The factory doesn't maintain any of the instances it creates.
    """

    @abstractmethod
    def get_video_exporter(self) -> VideoExporter:
        """Returns a new video exporter belonging to this factory."""

    @abstractmethod
    def get_audio_exporter(self) -> AudioExporter:
        """Returns a new audio exporter belonging to this factory."""


class FastExporter(ExporterFactory):
    """Factory aimed at providing a high speed, lower quality export."""

    def get_video_exporter(self) -> VideoExporter:
        return H264BPVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()


class HighQualityExporter(ExporterFactory):
    """Factory aimed at providing a slower speed, high quality export."""

    def get_video_exporter(self) -> VideoExporter:
        return H264Hi422PVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()


class MasterQualityExporter(ExporterFactory):
    """Factory aimed at providing a low speed, master quality export."""

    def get_video_exporter(self) -> VideoExporter:
        return LosslessVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return WAVAudioExporter()


def read_factory() -> ExporterFactory:
    """Constructs an exporter factory based on the user's preference."""

    factories = {
        "low": FastExporter(),
        "high": HighQualityExporter(),
        "master": MasterQualityExporter(),
    }
    while True:
        export_quality = input("Enter desired output quality (low, high, master): ")
        if export_quality in factories:
            return factories[export_quality]
        print(f"Unknown output quality option: {export_quality}.")


def main(fac: ExporterFactory) -> None:
    """Main function."""

    # retrieve the exporters
    video_exporter = fac.get_video_exporter()
    audio_exporter = fac.get_audio_exporter()

    # prepare the export
    video_exporter.prepare_export("placeholder_for_video_data")
    audio_exporter.prepare_export("placeholder_for_audio_data")

    # do the export
    folder = pathlib.Path("/usr/tmp/video")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)


if __name__ == "__main__":
    # create the factory
    factory = read_factory()

    # perform the exporting job
    main(factory)

######Proxy Pattern###########

# from abc import ABCMeta, abstractstaticmethod

# class Iperson(metaclass=ABCMeta):
#     def person_method():
#         """Interface method"""
    
# class Person(Iperson):
#     def person_method(self):
#         print("I am a person!!")

# #p1 = Person()
# class ProxyPerson(Iperson):
#     def __init__(self):
#         self.person = Person()
    
#     def person_method(self):
#         print("I am the proxy functionality!")
#         self.person.person_method()

# p1 = Person()
# p1.person_method()

# p2 = ProxyPerson()
# p2.person_method()
######Decorator Pattern###########

######Facade Pattern###########


# from abc import ABCMeta, abstractmethod
#
# class Iperson(metaclass=ABCMeta):
#
#     @abstractmethod
#     def print_data(self):
#         """Implement in child class"""
#
# class PersonSingleton(Iperson):
#     __instance = None
#
#     @staticmethod
#     def get_instance():
#         if PersonSingleton.__instance == None:
#             PersonSingleton("Default Name", 0)
#         return PersonSingleton.__instance
#
#     def __init__(self, name, age):
#         if PersonSingleton.__instance != None:
#             raise Exception("Singleton cannot be instantiated more than once")
#         else:
#             self.name = name
#             self.age = age
#             PersonSingleton.__instance = self
#
#     @staticmethod
#     def print_data():
#         print(f"Name: {PersonSingleton.__instance.name} Age: {PersonSingleton.__instance.age}")
#
# p = PersonSingleton("Mike", 30 )
# print(p)
# p.print_data()
#
#
# p2 = PersonSingleton.get_instance()
# print(p2)
# p2.print_data()


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





# class Singleton:
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, "_instance"):
#             cls._instance = super().__new__(cls, *args, **kwargs)
#         return cls._instance
#
# obj1 = Singleton()
# print("Object -1 ==> ", obj1)
# obj1.data = 10
#
# obj2 = Singleton()
# print("Object -2 ==> ", obj2)
# print(obj2.data)
#
# obj2.data = 20
# print("After modification ",obj2.data)
#


#Factory Pattern:


# class Shape:
#     def draw(self):
#         pass
#
# class Circle(Shape):
#     def draw(self):
#         print("Drawing Circle")
#
# class Rectangle(Shape):
#     def draw(self):
#         print("Drawing Rectangle")
#
# class ShapeFactory:
#     def create_shape(self, shape_type):
#         if shape_type == "Circle":
#             return Circle()
#         elif shape_type == "Rectangle":
#             return Rectangle()
#
#






# Regular Ball Super Ball

# class Ball(object):
#     def __init__(self, ball_type="regular"):
#         self.ball_type = ball_type

# Color Ghost

# import random
# class Ghost(object):
#     colors = ["white", "yellow", "purple", "red"]
#     def __init__(self, color=None):
#         self.color = random.choice(self.colors)

# Basic subclasses - Adam and Eve

# def God():
#     Adam = Man("Adam")
#     Eve = Woman("Eve")
#     return [Adam, Eve]

# class Human():
#     pass

# class Man(Human):
#     def __init__(self, name):
#         self.name = name

# class Woman(Human):
#     def __init__(self, name):
#         self.name = name

# Classy Classes

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.info=f"{str(self.name)}s age is {int(self.age)}"

# Building Spheres

# import math

# class Sphere(object):
#     def __init__(self, radius, mass):
#         self.radius = radius
#         self.mass = mass
    
#     def get_radius(self):
#         return self.radius
    
#     def get_mass(self):
#         return self.mass
    
#     def get_volume(self):
#         return round((4/3)*math.pi*self.radius**3, 5)
    
#     def get_surface_area(self):
#         return round(4*math.pi*self.radius**2, 5)
    
#     def get_density(self):
#         volume = Sphere.get_volume(self)
#         return round(self.mass/volume, 5)

# Python's Dynamic Classes #1

# def class_name_changer(cls, new_name):
#     if not new_name:
#         raise Exception("No empty name")
#     elif not new_name[0].isupper():
#         raise Exception("No uppercase letter")
#     elif not new_name.isidentifier():
#         raise Exception("No illegal chars")
#     elif new_name[0].isdigit():
#         raise Exception("No number at the beginning")
#     else: 
#         cls.__name__ = new_name


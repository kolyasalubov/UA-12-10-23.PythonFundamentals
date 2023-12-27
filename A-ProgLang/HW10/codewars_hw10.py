#I. Ball-super-ball

# class Ball(object):
#     def __init__(self, ball_type="regular"):
#         self.ball_type = ball_type

#######################################

#II. Color-ghost

# import random

# class Ghost(object):
#     def __init__(self):
#         self.color = random.choice(["white", "yellow", "purple", "red"])

#######################################

#III. Basic-subclasses-Adam-and-Eve

# class Human:
#     def __init__(self, name):
#         self.name = name

# class Man(Human):
#     def __init__(self, name):
#         super().__init__(name)
#         self.gender = 'Male'

# class Woman(Human):
#     def __init__(self, name):
#         super().__init__(name)
#         self.gender = 'Female'

# def God():
#     # Creating instances of Man and Woman
#     adam = Man("Adam")
#     eve = Woman("Eve")

#     # Returning an array containing objects (Adam and Eve)
#     return [adam, eve]

# # Testing the implementation
# creation = God()
# for human in creation:
#     print(f"{human.name} - {human.gender}")

#######################################

#V. Building Spheres

# import math

# class Sphere:
#     def __init__(self, radius, mass):
#         self.radius = radius
#         self.mass = mass

#     def get_radius(self):
#         return self.radius

#     def get_mass(self):
#         return self.mass

#     def get_volume(self):
#         volume = (4/3) * math.pi * self.radius**3
#         return round(volume, 5)

#     def get_surface_area(self):
#         surface_area = 4 * math.pi * self.radius**2
#         return round(surface_area, 5)

#     def get_density(self):
#         density = self.mass / self.get_volume()
#         return round(density, 5)

# ball = Sphere(2, 50)
# print(ball.get_radius())        
# print(ball.get_mass())          
# print(ball.get_volume())        
# print(ball.get_surface_area())  
# print(ball.get_density())      

#######################################

#VI. Dynamic Classes

# def class_name_changer(cls, new_name):
#     if not new_name[0].isupper() or not new_name.isalnum():
#         raise ValueError("Invalid class name. It should start with an uppercase letter and consist of alphanumeric characters.")

#     cls.__name__ = new_name

#     return cls

# class MyClass:
#     pass

# class_name_changer(MyClass, "UsefulClass")
# print(MyClass.__name__)  

# class_name_changer(MyClass, "SecondUsefulClass")
# print(MyClass.__name__)  

#######################################
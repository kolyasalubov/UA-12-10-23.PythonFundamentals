import random
import re

# task 1
#Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
#If no arguments are given, ball objects should instantiate with a "ball type" of "regular."


class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type

# task2
#Create a class Ghost
#Ghost objects are instantiated without any arguments.
#Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated

import random

class Ghost:
    def __init__(self):
       ghost_colors = ["white", "yellow", "purple", "red"]
       self.color = random.choice(ghost_colors)

# task3
#According to the creation myths of the Abrahamic religions, Adam and Eve were the first Humans to wander the Earth.
#You have to do God's job.
# The creation method must return an array of length 2 containing objects (representing Adam and Eve).
# The first object in the array should be an instance of the class Man.
# The second should be an instance of the class Woman. Both objects have to be subclasses of Human.
# Your job is to implement the Human, Man and Woman classes.

def God():
    man = Man('Adam')
    woman = Woman('Eva')
    return [man, woman]

class Human:
    def __init__(self, name):
        self.name = name

class Man(Human):
    def __init__(self, name):
        super().__init__(name)

class Woman(Human):
    def __init__(self, name):
        super().__init__(name)



# task4
#Your task is to complete this Class, the Person class has been created.
# You must fill in the Constructor method to accept a name as string and an age as number,
# complete the get Info property and getInfo method/Info getter which should return johns age is 34


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = f"{self.name}s age is {self.age}"

# task5
# Now that we have a Block let's move on to something slightly more complex: a Sphere.


from math import pi
class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
        self.volume = 4*pi * self.radius**3 / 3
        self.surface = 4*pi* self.radius**2
    def get_radius(self):
        return self.radius
    def get_mass(self):
        return self.mass
    def get_volume(self):
        return round(self.volume,5)
    def get_surface_area(self):
        return round(self.surface,5)
    def get_density(self):
        return round(self.mass/self.volume, 5)


# task6
# Dynamic Classes

import re
def class_name_changer(cls, new_name):
    if re.match(r'^[A-Z][a-zA-Z0-9-_]*$', new_name):
        cls.__name__ = new_name
    else:
        raise Exception('Invalid Class Name')
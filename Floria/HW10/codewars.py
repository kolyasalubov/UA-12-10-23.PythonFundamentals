###1

#Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
#If no arguments are given, ball objects should instantiate with a "ball type" of "regular."

class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type


ball1 = Ball()
ball2 = Ball("super")

print(ball1.ball_type)
print(ball2.ball_type)


###2

#Create a class Ghost
#Ghost objects are instantiated without any arguments.
#Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated

import random

class Ghost:
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])
        pass


###3

#According to the creation myths of the Abrahamic religions, Adam and Eve were the first Humans to wander the Earth.

#You have to do God's job. The creation method must return an array of length 2 containing objects (representing Adam and Eve).
#The first object in the array should be an instance of the class Man. The second should be an instance of the class Woman.
#Both objects have to be subclasses of Human. Your job is to implement the Human, Man and Woman classes.

class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

def God():
    return [Man(), Woman()]


###4

#Your task is to complete this Class, the Person class has been created.
#You must fill in the Constructor method to accept a name as string and an age as number,
#complete the get Info property and getInfo method/Info getter which should return johns age is 34

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = f"{name}s age is {age}"


###5

#

def class_name_changer(cls, new_name):
    if new_name[0] == str.upper() and new_name.isalnum():
        cls.__name__ = new_name
        return cls.__name__


import random
import re

# 1
# Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
# If no arguments are given, ball objects should instantiate with a "ball type" of "regular."


class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type

# 2
# Create a class Ghost.
# Ghost objects are instantiated without any arguments.
# Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated


class Ghost(object):
    def __init__(self):
        self.colors = ['white', 'yellow', 'red', 'purple']
        self.color = random.choice(self.colors)

# 3
# According to the creation myths of the Abrahamic religions, Adam and Eve were the first Humans to wander the Earth.
# You have to do God's job.
# The creation method must return an array of length 2 containing objects (representing Adam and Eve).
# The first object in the array should be an instance of the class Man.
# The second should be an instance of the class Woman. Both objects have to be subclasses of Human.
# Your job is to implement the Human, Man and Woman classes.


class Human:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Human: {self.name}"


class Man(Human):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"Man: {self.name}"


class Woman(Human):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"Woman: {self.name}"


class God:
    def __getitem__(self, index):
        if index == 0:
            return Man("Adam")
        elif index == 1:
            return Woman("Eve")

    def __len__(self):
        return 2

# 4
# Your task is to complete this Class, the Person class has been created.
# You must fill in the Constructor method to accept a name as string and an age as number,
# complete the get Info property and getInfo method/Info getter which should return johns age is 34


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = f"{self.name}s age is {self.age}"

# 5
# Now that we have a Block let's move on to something slightly more complex: a Sphere.


class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = float(radius)
        self.mass = float(mass)
        self.volume_sphere = None  # Initialize to None

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        if self.volume_sphere is None:
            self.calculate_volume()
        return round(self.volume_sphere, 5)

    def get_surface_area(self):
        return round(4 * 3.14159 * self.radius**2, 5)

    def get_density(self):
        if self.volume_sphere is None:
            self.calculate_volume()
        return round(self.mass / self.volume_sphere, 5)

    def calculate_volume(self):
        self.volume_sphere = (4/3) * 3.14159 * self.radius**3

# 6 Timmy's quiet and calm work has been suddenly stopped by his project manager (let's call him boss) yelling:
# - Who named these classes?! Class MyClass? It's ridiculous! I want you to change it to UsefulClass!
# Tim sighed, he already knew it's going to be a long day.
# Few hours later, boss came again:
# Much better - he said - but now I want to change that class name to SecondUsefulClass, and went off.
# Although Timmy had no idea why changing name is so important for his boss,
# he realized, that it's not the end, so he turned to you, his guru,
# to help him and asked you to prepare some function, which could change name of given class.
# Note: Proposed function should allow only names with alphanumeric chars (upper & lower letters plus ciphers),
# but starting only with upper case letter. In other case it should raise an exception.
# Disclaimer: there are obviously betters way to check class name than in example cases,
# but let's stick with that, that Timmy yet has to learn them.


def class_name_changer(class_obj, new_name):
    if not re.match("^[A-Z][a-zA-Z0-9]*$", new_name):
        raise ValueError("Invalid class name")
    class_obj.__name__ = new_name

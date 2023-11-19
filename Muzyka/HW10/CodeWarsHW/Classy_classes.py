"""
Your task is to complete this Class, the Person class has been created.
You must fill in the Constructor method to accept a name as string and an age as number,
complete the get Info property and getInfo method/Info getter which should return johns age is 34
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def info(self):
        return f"{self.name}s age is {self.age}"

    def get_info(self):
        return f"{self.name}s age is {self.age}"


john = Person("John", 34)

print(john.info)

print(john.get_info())

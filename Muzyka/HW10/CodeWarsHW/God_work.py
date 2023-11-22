"""
You have to do God's job. The creation method must return an array of length 2 containing objects (representing Adam and Eve).
The first object in the array should be an instance of the class Man. The second should be an instance of the class Woman.
Both objects have to be subclasses of Human. Your job is to implement the Human, Man and Woman classes.
"""

class Human:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Man(Human):
    def __init__(self, name):
        super().__init__(name, gender='male')


class Woman(Human):
    def __init__(self, name):
        super().__init__(name, gender='female')


def God():
    adam = Man("Adam")
    eve = Woman("Eve")
    return [adam, eve]


adam_and_eve = God()

for person in adam_and_eve:
    print(f"Name: {person.name}, Gender: {person.gender}")

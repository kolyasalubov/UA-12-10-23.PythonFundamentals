import random

"""
Create a class Ghost
Ghost objects are instantiated without any arguments.
Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated
"""

class Ghost:
    def __init__(self):
        self.color = random.choice(['white', 'yellow', 'purple', 'red'])

    def get_color(self):
        return self.color


ghost1 = Ghost()
ghost2 = Ghost()

print(ghost1.get_color())
print(ghost2.get_color())

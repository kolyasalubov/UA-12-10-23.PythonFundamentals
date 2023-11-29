class Human:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Welcome, {self.name}!")

    @classmethod
    def species(cls):
        return "Homosapiens"

    @staticmethod
    def message():
        return "Something"


human = Human("John")
human.welcome()
print(human.species())
print(Human.message())
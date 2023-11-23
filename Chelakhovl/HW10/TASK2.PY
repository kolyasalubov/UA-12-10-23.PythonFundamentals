class Human:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f"Hello, {self.name}!")

    def species(self):
        print(f"{self.name} is a species of Homosapiens.")

    @staticmethod
    def staticmethod():
        return "Homosapiens is the most numerous and widespread species of primate."


person = Human("John")
person.hello()
person.species()
print(Human.staticmethod())
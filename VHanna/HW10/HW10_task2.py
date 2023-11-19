class Human:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        return f"Hello, {self.name}!"

    def species(self):
        return f"{self.name} is a Homosapiens."

    @staticmethod
    def arbitrary_message():
        return "This is a static message"

person1 = Human("Ann")
print(person1.welcome())
print(person1.species())
print(Human.arbitrary_message())
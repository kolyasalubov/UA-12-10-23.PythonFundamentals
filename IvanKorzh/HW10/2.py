class Human:
    def __init__(self, name):
        self.name = name

    def great(self):
        print(f"Hello, {self.name}!")

    @classmethod
    def species(cls):
        print("You are homosapiens!")

    @staticmethod
    def message():
        print("Some message")


result = Human("Ivan")
result.great()
result.species()
result.message()

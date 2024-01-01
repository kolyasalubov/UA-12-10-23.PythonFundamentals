class Human:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Hello, {self.name}!")

    @classmethod
    def species_info(cls):
        return "Welcome to the world of human!"

    @staticmethod
    def arbitrary_message():
        return "Happy New Year and Merry Christmas!!!"


if __name__ == "__main__":
    person = Human("Maria")
    person.welcome()

    print(Human.species_info())
    print(Human.arbitrary_message())

class Human:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Hello, {self.name}!")

    @classmethod
    def species_info(cls):
        return "I am a Homosapiens."

    @staticmethod
    def arbitrary_message():
        return "I really love my computer"  # произвольное сообщение


if __name__ == "__main__":
    person = Human("John")
    person.welcome()

    print(Human.species_info())
    print(Human.arbitrary_message())

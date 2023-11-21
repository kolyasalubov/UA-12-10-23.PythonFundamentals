class Human:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello {}\n".format(self.name))

    @classmethod
    def info(cls):
        cls.species = "Homosapiens"
        print("Human class is a {} scpecies\n".format(cls.species))

    @staticmethod
    def message():
        print("Humans are monkeys, but with less hair on their skin\n")

human_1 = Human("Oleg")

human_1.greet()
human_1.info()
human_1.message()

print(human_1.greet)
print(human_1.info)
print(human_1.message)
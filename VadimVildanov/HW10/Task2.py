class Human:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hi {}\n".format(self.name))

    @classmethod
    def information(cls):
        cls.species = "Homosapiens"
        print("Human class is a {} species\n".format(cls.species))

    @staticmethod
    def sms():
        print("You're Homosapiens dude")


human_first = Human("Vadim")

human_first.greet()
human_first.information()
human_first.sms()

print(human_first.greet)
print(human_first.information)
print(human_first.sms)
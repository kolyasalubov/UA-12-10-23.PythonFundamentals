class Human:
    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        return f"Hello, {self.name}! Welcome!"

    @classmethod
    def hum_info(cls):
        return f"I am a species of {cls.__name__}, specifically Homosapiens."

    @staticmethod
    def message():
        return "This is a static method. It can be called without creating an instance of the class."

person = Human("Mariana")
print(person.welcome_message())

print(Human.hum_info())

print(Human.message())
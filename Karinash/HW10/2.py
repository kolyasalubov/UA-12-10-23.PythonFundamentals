class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        return f"Welcome, {self.name}!"

    @classmethod
    def get_species(cls):
        return f"I am a species of {cls.species}"

    @staticmethod
    def arbitrary_message():
        return "This is a static method with an arbitrary message"


# Example usage:
person = Human("John")
print(person.welcome_message())  # Output: Welcome, John!
print(Human.get_species())  # Output: I am a species of Homosapiens
print(Human.arbitrary_message())  # Output: This is a static method with an arbitrary message

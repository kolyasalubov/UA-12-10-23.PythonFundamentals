class Human:
    def __init__(self, name):
        self.name = name

    def display_greeting(self):
        return f"Hello, my name is {self.name}."

    @classmethod
    def species_info(cls):
        return f"This is a {cls.__name__}."

    @staticmethod
    def random_message():
        return "This is a static method returning a random message."

# Example usage
person1 = Human("John")
person2 = Human("Alice")

print(person1.display_greeting())  # Outputs "Hello, my name is John."
print(person2.display_greeting())  # Outputs "Hello, my name is Alice."

print(Human.species_info())  # Outputs "This is a Human."

print(Human.random_message())  # Outputs a random message from the static method.
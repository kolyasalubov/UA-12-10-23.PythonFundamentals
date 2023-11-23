class Human:
    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        return f"Hello, {self.name}! Welcome to the human race."

    @classmethod
    def species_info(cls):
        return f"{cls.__name__} is a species of Homosapiens."

    @staticmethod
    def arbitrary_message():
        return "This is a static method. It can be called on the class or an instance, but it doesn't have access to instance-specific data."


person = Human("Jack")


# Instance method
print(person.welcome_message()) 


# Class method
print(Human.species_info())  

# Static method
print(Human.arbitrary_message())  

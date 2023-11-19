import random


messages = ["Nice day to learn a something new!",
            "Blablabla", 
            "Two Jews once meet and...",
            "Hey, Boss! Where is my salary?"]
random_message = print(random.choice(messages))


class Human:
    species = "Homosapiens"  

    def __init__(self, name):
        self.name = name  

    def greeting(self):
        return print(f"Hello, {self.name}! Welcome!")

    @classmethod
    def get_species(cls):
        return print(cls.species)

    @staticmethod
    def get_random_message():
        return random_message
    

person1 = Human("Liubov Koliasa")
person2 = Human("Dmytro")

h = Human
person1.greeting()
person1.get_species()
h.get_random_message()
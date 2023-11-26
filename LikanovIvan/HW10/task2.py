class Human():
    species = 'Homosapiens'
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f'Hello there, {self.name}')
    
    @classmethod
    def homo(cls):
        print(f'Humans are {cls.species}. Here i have access only to class variables')
    
    @staticmethod
    def arbitary():
        print(f'Here I can write only arbitary message without variables used before')


man = Human('John')

man.welcome()
man.homo()
man.arbitary()
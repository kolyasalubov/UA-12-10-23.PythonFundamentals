class Human:
    def __init__(self,name:str) -> None:
        self.name=name

    def greeting(self):
        return f'Hello {self.name}'
    @classmethod
    def species(cls):
        return 'This species is Homosapiens'
    
    @staticmethod
    def arbit(*args):
        print(f'arbitrary message and arbitrary parameters: {args}')

human = Human('Vlad')
print(human.greeting())
print(human.species())
print(Human.species())
print(Human.arbit('asd',12,43,32,4))
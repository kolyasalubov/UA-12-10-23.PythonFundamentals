class Employee:
    'Class Employee'
    counter = 0
    def __init__(self,name,salary) -> None:
        self.salary = salary
        self.name = name
        Employee.counter+=1
    @classmethod
    def printing_quantity(cls):
        '''Prints quantity of employees'''
        print(f'Total number of employees: {cls.counter}')

    def info(self):
        '''Info about employees'''
        print(f'This employee has name: {self.name} and salry: {self.salary}')
from pprint import pprint
A = Employee('Vlad',300)
B = Employee('Bogdan',400)
pprint('Employee info: ')
pprint(Employee.__name__)
pprint(Employee.__dict__)
pprint(Employee.__base__)
pprint(Employee.__module__)
pprint(Employee.__doc__)
pprint('==========')
pprint('Object info: ')

pprint(object.__name__)
pprint(object.__dict__)
pprint(object.__base__)
pprint(object.__module__)
pprint(object.__doc__)

class Employee:
    """
    Employee class stores the data about employees, 
    which include name and salary of the person

    Also, the class counts the amount of its instances
    """
    _counter = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee._counter += 1
    
    def show_info(self):
        print(f"Name: {self.name}; Salary: {self.salary}.\n")
    
    def total():
        print(f"There are {Employee._counter} members of this class")


human_1 = Employee("Sam Smith", 2000)
human_2 = Employee("John Doe", 2500)

human_1.show_info()
human_2.show_info()

Employee.total()

print(Employee.__base__)
# print(Employee.__dict__) 
print(Employee.__dict__.keys())     # concise form of class namespaces
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)


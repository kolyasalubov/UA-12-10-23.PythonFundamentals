class Employee:
    counter = 0

    def __init__(self, name, salary):
        Employee.counter += 1
        self.name = name
        self.salary = salary

    @staticmethod
    def count_employee():
        print(f"Total count employee: {Employee.counter}")

    def total_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")


obj1 = Employee("Ivan", 20000)
obj2 = Employee("Piter", 10000)
obj3 = Employee("Joe", 50000)

obj1.total_info()
obj1.count_employee()
obj2.total_info()
obj2.count_employee()
obj3.total_info()
obj3.count_employee()

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)

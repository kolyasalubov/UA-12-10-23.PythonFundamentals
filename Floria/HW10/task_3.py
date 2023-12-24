class Employee:
    num_of_emps = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.num_of_emps += 1

    def display_employee(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def display_total_employees(cls):
        print(f"Total Employees: {cls.num_of_emps}")

print(f"Base classes: {Employee.__bases__}")
print(f"Class namespace: {Employee.__dict__}")
print(f"Class name: {Employee.__name__}")
print(f"Module name: {Employee.__module__}")
print(f"Documentation: {Employee.__doc__}")

employee1 = Employee("John", 50000)
employee2 = Employee("Jane", 60000)

employee1.display_employee()
employee2.display_employee()

Employee.display_total_employees()
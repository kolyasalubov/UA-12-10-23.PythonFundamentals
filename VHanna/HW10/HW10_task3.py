class Employee:
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1
    
    def employees_details(self):
        print(f"Employee Name: {self.name}, Salary: {self.salary} $")
    
    @classmethod
    def count_employees(cls):
        print(f"Total Employees: {cls.total_employees}")
    
employee1 = Employee("Emily Smith", 1000)
employee2 = Employee("Emma Williams", 2000)
employee3 = Employee("Jones Johnson", 3000)

employee1.employees_details()
employee2.employees_details()
employee3.employees_details()
Employee.count_employees()

print(f"\nBase classes: {Employee.__bases__}\nClass namespace: {Employee.__dict__}\nClass name: {Employee.__name__}\nModule name: {Employee.__module__}\nDocumentation: {Employee.__doc__}")

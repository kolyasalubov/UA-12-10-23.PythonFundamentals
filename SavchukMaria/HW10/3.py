class Employee:
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    def display_employee_info(self):
        print(f"Employee Name: {self.name}, Salary: ${self.salary}")

    @classmethod
    def display_total_employees(cls):
        print(f"Total Employees: {cls.total_employees}")


print(f"Base classes: {Employee.__bases__}")
print(f"Class namespace: {Employee.__dict__}")
print(f"Class name: {Employee.__name__}")
print(f"Module name: {Employee.__module__}")
print(f"Documentation: {Employee.__doc__}")
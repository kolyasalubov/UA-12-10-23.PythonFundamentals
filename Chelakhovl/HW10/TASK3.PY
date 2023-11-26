class Employee:
    employee_total = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_total += 1

    def employee_info(self):
        print(f"Name: {self.name}, Salary: {self.salary} $")

    @classmethod
    def employee_count(cls):
        print(f"Total Employees: {cls.employee_total}")


employee1 = Employee("Agent K", 5000)
employee2 = Employee("Agent J", 6000)

employee1.employee_info()
employee2.employee_info()

Employee.employee_count()

print(f"\nBase class: {Employee.__base__}")
print(f"Namespace: {Employee.__dict__}")
print(f"Class name: {Employee.__name__}")
print(f"Module name: {Employee.__module__}")
print(f"Documentation: {Employee.__doc__}")

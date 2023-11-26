class Employee:
    
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
        Employee.total_employees += 1

    def display_info(self):
        
        print(f"Employee Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def display_total_employees(cls):
        
        print(f"Total Employees: {cls.total_employees}")


employee1 = Employee("Alice", 50000)
employee2 = Employee("Bob", 60000)


employee1.display_info()
employee2.display_info()


Employee.display_total_employees()


print(f"Base Classes: {Employee.__bases__}")
print(f"Class Namespace: {Employee.__dict__}")
print(f"Class Name: {Employee.__name__}")
print(f"Module Name: {Employee.__module__}")
print(f"Documentation: {Employee.__doc__}")

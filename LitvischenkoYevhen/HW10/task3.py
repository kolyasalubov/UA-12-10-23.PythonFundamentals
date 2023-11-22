class Employee:
    """
    Each employee has characteristics such as name and salary
    """
    #count employees
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        # Increment the total count of employees
        Employee.total_employees += 1

    def display_info(self):
        # display information about each employee
        print(f"Employee Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def display_total_employees(cls):
        # Class method to print count of employees
        print(f"Total Employees: {cls.total_employees}")


employee1 = Employee("John Doe", 50000)
employee2 = Employee("Joe Maier", 60000)

# Display inforo for each employee
employee1.display_info()
employee2.display_info()

# Display count of employees
Employee.display_total_employees()

# Display information about the class
print(f"\nClass Base: {Employee.__base__}")
print(f"Class Namespace: {Employee.__dict__}")
print(f"Class Name: {Employee.__name__}")
print(f"Module Name: {Employee.__module__}")
print(f"Documentation: {Employee.__doc__}")
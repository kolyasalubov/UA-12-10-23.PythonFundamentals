class Employee:
    # Class variable to keep track of the total number of employees
    total_employees = 0

    def __init__(self, name, salary):
        # Instance variables
        self.name = name
        self.salary = salary
        # Increment the total number of employees
        Employee.total_employees += 1

    def display_employee_info(self):
        print(f"Employee Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def display_total_employees(cls):
        print(f"Total Employees: {cls.total_employees}")

# Display information about the class and its attributes
print("Base Classes:", Employee.__base__)
print("Class Namespace:", Employee.__dict__)
print("Class Name:", Employee.__name__)
print("Module Name:", Employee.__module__)
print("Documentation:", Employee.__doc__)

# Example usage
employee1 = Employee("John Doe", 50000)
employee2 = Employee("Alice Smith", 60000)

employee1.display_employee_info()
employee2.display_employee_info()

Employee.display_total_employees()
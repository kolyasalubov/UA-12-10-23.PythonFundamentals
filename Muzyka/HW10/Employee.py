class Employee:
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

        Employee.total_employees += 1

    def display_employee_info(self):
        print(f"employee name: {self.name}, salary: {self.salary}")

    @classmethod
    def display_total_employees(cls):
        print(f"Total number of employees: {cls.total_employees}")


if __name__ == "__main__":
    employee1 = Employee("Kolia Muzyka", 10000)
    employee2 = Employee("Alina Papish", 15000)

    employee1.display_employee_info()
    employee2.display_employee_info()

    Employee.display_total_employees()

    print("Base classes:", Employee.__bases__)
    print("Class namespace:", Employee.__dict__)
    print("Class name:", Employee.__name__)
    print("Module name:", Employee.__module__)
    print("Doc:", Employee.__doc__)

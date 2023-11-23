from pprint import pprint


class Employee:
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    def displey_employee_VS_salary(self):
        print(f"Name: {self.name}, Salary is: {self.salary}$")

    def displey_employee_count(cls):
        print(f"Total emloyees: {Employee.employee_count}")
        # print(f"Total emloyees: {cls.employee_count}")
        


print(Employee.__base__)
pprint(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
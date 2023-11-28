class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

        def show_info(self):
            print(f"Name: {self.name}; Salary: {self.salary}.\n")

        def total():
            print(f"There are {Employee._counter} members of this class")

    human_1 = Employee("Vadim Vildanov", 3500)
    human_2 = Employee("Vlad Vildanov", 6700)

    human_1.show_info()
    human_2.show_info()

    Employee.total()

    print(Employee.__base__)
    # print(Employee.__dict__)
    print(Employee.__dict__.keys())
    print(Employee.__name__)
    print(Employee.__module__)
    print(Employee.__doc__)

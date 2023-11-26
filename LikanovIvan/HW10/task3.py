class Employee(object):
    total_workers = 0
    def __init__(self,name,salary):
        self.name = name.capitalize()
        self.salary = salary
        Employee.total_workers +=1
        self.worker_id = Employee.total_workers
    def info(self):
        print(f'{self.worker_id}) Name: {self.name}; Salary: {self.salary}')
    
    @classmethod
    def total_employees(cls):
        print(f'Total Employees: {Employee.total_workers}')

emp1 = Employee("John", 50000)
emp2 = Employee("ann", 45000)
emp3 = Employee('Diego', 65000)
emp1.info()
emp2.info()
emp3.info()
Employee.total_employees()
            
    
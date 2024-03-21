class Employee:
    """This is an Employee class.  
    """
    eployee_counter = 0
    def __init__(self, name, assessment, salary): 
        self.name = name
        self.assessment = assessment
        self.salary = salary
        Employee.eployee_counter += 1
    
    def personal_info(self):
        print(f"Worker {self.name} has salary {self.salary}$ Asessment is {self.assessment}.")
        
    @classmethod
    def amount_of_employee(cls):
        print(f"The total amount of employees is {Employee.eployee_counter}")
        
    def fire(self):
        if self.assessment.lower() == "bad":
            Employee.eployee_counter -= 1
            print(f"Employee {self.name} was fired because assessment is {self.assessment}")
        else:
            print(f"Employee {self.name} was not fired because assessment is {self.assessment}")
    
class ExampleChild(Employee):
    def __init__(self):
        super().__init__()
    

# використав атрибут __doc__
print(f"__doc__: {Employee.__doc__}")


worker_1 = Employee("Ilya Shtefan", "Good", 7000)
worker_1.personal_info()

# використав атрибут __dict__
print(f"__dict__: {worker_1.__dict__}")

worker_2 = Employee("Pahsa Kopanez", "Good", 6750)
worker_2.personal_info()


worker_3 = Employee("Bill Afton", "Bad", 2000)
worker_3.personal_info()

Employee.amount_of_employee()
    
worker_2.fire()
Employee.amount_of_employee()

worker_3.fire()
Employee.amount_of_employee()

# використав атрибут __base__
print(f"__base__: {ExampleChild.__base__}")


# __module__ - не зовсім підходить до цього коду
# __name__ - не зовсім підходить до цього коду
class Human():
    def __init__(self, name):
        self.name = name
    
    def greetin(self):
        print(f"Hello {self.name}!")

    def species(self):
        print(f"{self.name} is homosapiens")

    @staticmethod
    def static_method():
        print("Call static method")


a = Human('Den')
a.greetin()
a.species()
a.static_method()
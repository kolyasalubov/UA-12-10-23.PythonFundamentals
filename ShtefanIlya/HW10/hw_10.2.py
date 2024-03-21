
class Human:
    human_counter = 0
    not_human_counter = 0
    def __init__(self, name, human = "?"):
        self.name = name
        self.human = human
    
    def welcome(self):
        print(f"Welcome {self.name}!")
            
    @classmethod
    def is_it_human(cls, name, human):
        if human.lower() == "human":
            print(f"This species is homosapiens by name {name}")
            Human.human_counter += 1
        else:
            print(f"This species is not homosapiens, but it has name {name}")
            Human.not_human_counter += 1
    
    @staticmethod
    def random_msg():
        print("Just static mathod)")
        
    def __del__(self):
        if self.human.lower() == "human":
            Human.human_counter -= 1
             
        else:
            Human.not_human_counter -= 1
            
            
    

obj_1 = Human("Frank", "Human")
obj_1.welcome()
Human.is_it_human(obj_1.name, obj_1.human)

obj_2 = Human("Max", "Dog")
obj_2.welcome()
Human.is_it_human(obj_2.name, obj_2.human)

print(f"Human counter: {Human.human_counter}")
print(f"Not human counter: {Human.not_human_counter}")
print("\n")

del(obj_1)

print(f"Human counter: {Human.human_counter}")
print(f"Not human counter: {Human.not_human_counter}")
print("\n")

del(obj_2)

print(f"Human counter: {Human.human_counter}")
print(f"Not human counter: {Human.not_human_counter}")
print("\n")









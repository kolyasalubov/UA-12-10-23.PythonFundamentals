class Polygon:

    def __init__(self, num_of_sides):
        self.num_of_sides = num_of_sides
        self.sides = [0 for i in range(num_of_sides)]
    
    def input_sides(self):
        for i in range(self.num_of_sides):
            try:
                value = float(input(f"Enter {i+1} side: "))
                while value <= 0 and isinstance(value, float) is True:
                    print("Only positive number allowed!\n")
                    value = float(input(f"Enter {i+1} side: "))
            except ValueError:
                print("Enter only float digits")
                break
            else:
                self.sides[i] = value

    
    def display_sides(self):
        for i in range(self.num_of_sides):
            print(f"{i+1} side: {round(self.sides[i], 3)}")

class Rectangle(Polygon):
    
    def __init__(self):
        super().__init__(2)
    
    def find_area(self):
        super().input_sides()
        a, b = self.sides
        area = a*b
        print(f"The area of the rectangle is {round(area, 3)}\n")

class Triangle(Polygon):

    def __init__(self):
        super().__init__(3)
    
    def find_area(self):
        super().input_sides()
        a, b, c = self.sides
        s = (a+b+c)/2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print(f"The area of the triangle is {round(area, 3)}\n")

while True:
    print("1 - rectangle\n2 - triangle\n0 - exit\n")
    value = input("Choose figure: ")
    match value:
        case "1":
            rectan = Rectangle()
            rectan.find_area()
        case "2":
            trian = Triangle()
            trian.find_area()
        case "0":
            print("Shutting down program... ")
            break
        case _:
            print("Wrong command!\n")
            continue
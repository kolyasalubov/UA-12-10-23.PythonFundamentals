class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
    def inputSides(self):
        self.sides =[int(input("Enter side " + str(i+1) + " : ")) for i in range(self.n)]
    def dispSides(self):
        for i in range(self.n):
            print("Side", i+1, "is", self.sides[i])

class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)
    def findArea(self):
        a, b = self.sides
        print(f'The area of the rectangle is {a*b}')


#added area of triangle with checking its existence
class Triangle(Polygon):
    def __init__(self):
        super().__init__(3) 
    def findArea(self):
        a, b, c = self.sides
        x = max(a,b,c)
        if x < a+b+c - x:
            s = (a + b + c) / 2
            area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
            print(f'The area of the triangle is {int(round(area,0))}')
        else:
            print("Triangle with this sides cannot exist")




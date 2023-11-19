class Polygon():
    def __init__(self, n_sides):
        self.n = n_sides
        self.sides = [int(input(f"Enter side {i+1} : ")) for i in range(self.n)]

    def perimeter(self):
        if len(self.sides) > 2: 
            per = sum(x for x in self.sides)
            print(f"Perimeter of polygon : {per}")
        else:
            print(f"it is no polygon")

class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 2)
    
    def square(self):
        a, b = self.sides
        area = a*b
        print(f"Area of rectangle : {area}")

t = Rectangle()
t.square()
t.perimeter()

a = Polygon(5)
a.perimeter()


    
    
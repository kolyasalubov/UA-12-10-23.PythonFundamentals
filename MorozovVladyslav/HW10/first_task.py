class Polygon:
    pass

class Rectangle(Polygon):
    def __init__(self,side1,side2) -> None:
        self.side1 = side1
        self.side2 = side2

    def area(self):
        return self.side1*self.side2
    
rect = Rectangle(3,5)
print(rect.area())
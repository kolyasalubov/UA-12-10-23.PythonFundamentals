class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def get_perimeter(self):
        return sum(self.sides)

class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__([length, width, length, width])
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width
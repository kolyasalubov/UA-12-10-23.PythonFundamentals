class Polygon:
    def __init__(self, sides):
        if any(side <= 0 for side in sides):
            raise ValueError("All sides must be positive numbers")

        self.sides = sides

    def display_info(self):
        print(f"A polygon with sides: {self.sides}")


class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__([length, width, length, width])
        self.length = length
        self.width = width

    def find_square(self):
        return self.length * self.width

    def display_info(self):
        super().display_info()
        print(f"The length of the rectangle: {self.length}")
        print(f"The width of the rectangle: {self.width}")
        print(f"Area of the rectangle: {self.find_square()}")


# Example of use
try:
    sides_polygon = [3, 4, 5, 6]
    polygon = Polygon(sides_polygon)
    polygon.display_info()
except ValueError as e:
    print(e)

try:
    rectangle = Rectangle(4, 5)
    rectangle.display_info()
except ValueError as e:
    print(e)
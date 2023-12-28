class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_sides(self):
        print(f"A polygon with {self.sides} sides")


class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(4)
        self.length = length
        self.width = width

    def calculate_square(self):
        return self.length * self.width


# Example usage:
rectangle = Rectangle(5, 8)
rectangle.display_sides()  # Output: A polygon with 4 sides
print(f"Square of the rectangle: {rectangle.calculate_square()}")

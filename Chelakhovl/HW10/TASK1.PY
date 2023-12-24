class Polygon:
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.sides = []

    def add_side(self, side):
        self.sides.append(side)

    def perimeter(self):
        return sum(self.sides)

    def area(self):
        return 0.5 * self.sides[0] * self.sides[1]


class Rectangle(Polygon):
    def __init__(self):
        super().__init__(4)
        self.input_sides()

    def input_sides(self):
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        self.add_side(length)
        self.add_side(width)
        self.add_side(length)
        self.add_side(width)

    def find_square(self):
        return self.sides[0] * self.sides[1]


rectangle = Rectangle()
print(f"Rectangle perimeter: {rectangle.perimeter()}")
print(f"Square of the rectangle: {rectangle.find_square()}")

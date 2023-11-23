class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def get_number_of_sides(self):
        return self.sides


class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(4)
        self.length = length
        self.width = width

    def find_square(self):
        return self.length * self.width


# Example of using the classes
if __name__ == "__main__":
    rectangle = Rectangle(5, 10)

    print("Number of sides of the rectangle:", rectangle.get_number_of_sides())
    print("Area of the rectangle:", rectangle.find_square())

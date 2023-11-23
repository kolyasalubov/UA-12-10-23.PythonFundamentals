class Polygon:
    def __init__(self, points, sides):
        self.sides = sides

    def get_area(self):
        pass


class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__([
            (0, 0),
            (width, 0),
            (width, height),
            (0, height),], 4)
        self.width = width
        self.height = height

    def get_area_rectangle(self):
        return self.width * self.height


result = Rectangle(10, 20)
print(result.get_area_rectangle())

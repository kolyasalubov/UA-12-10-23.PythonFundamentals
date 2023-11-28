class Polygon:
    def init(self, sides):
        self.sides = sides

    def get_num_sides(self):
        return len(self.sides)

    def get_perimeter(self):
        return sum(self.sides)


class Rectangle(Polygon):
    def init(self, length, width):
        super().init([length, width, length, width])

    def get_area(self):
        return self.sides[0] * self.sides[1]
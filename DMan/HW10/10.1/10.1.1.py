class Polygon:
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.sides = [0 for i in range(num_sides)]

    def input_sides(self):
        self.sides = [float(input(f"Enter side {i+1}: "))
                      for i in range(self.num_sides)]

    def display_sides(self):
        for i in range(self.num_sides):
            print(f"Side {i+1} is {self.sides[i]}")


class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)

    def find_area(self):
        area = self.sides[0] * self.sides[1]
        print("area of rectangle is ", area)


r = Rectangle()
r.input_sides()
r.display_sides()
r.find_area()
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
# r.input_sides()
# r.display_sides()
r.find_area()

# class Poligon:
#     def __init__(self, num_of_sides):
#         self.n = num_of_sides
#         self.sides = [0 for i in range(num_of_sides)]

#     def inputSides(self):
#         self.sides = [float(input("Enter side " + str(i + 1) +" : "))
#                       for i in range(self.n)]

#     def dispSides(self):
#         for i in range(self.n):
#             print("Side", i+1, "is", self.sides[i])



# class Poligon:
#     def __init__(self, num_of_side):
#         self.num_of_side = num_of_side
#         self.sides = [0 for i in range(num_of_side)]

#     def findArea(self):
#        for i in range(self.num_of_side):
#             self.sides.append(0)

#     def inputSides(self):
#         for i in range(self.num_of_side):
#             user_input = float(input("Enter your side"))
#             self.sides[i] = user_input

#     def disprides (self):
#         print(self.sides)

# class Rectangle(Poligon):
#     def __init__(self):
#         super().__init__(2)

#     def findArea(self):
#         if len(self.sides) == self.num_of_side: 
#           a, b = self.sides
#           print('The area of the rectangle is %0.2f' % (a * b))

# print(Rectangle.findArea(3))   

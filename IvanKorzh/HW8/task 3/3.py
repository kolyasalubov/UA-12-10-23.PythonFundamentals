import area_of_rectangle
import area_of_triangle
import area_of_circle

user_input = input("What area of you want to find?\nrectangle, triangle or circle?\n")
if user_input == "rectangle":
    area_of_rectangle.area_rectangle()
elif user_input == "triangle":
    area_of_triangle.area_triangle()
elif user_input == "circle":
    area_of_circle.area_circle()
else:
    print("area of this figure can't calculated")

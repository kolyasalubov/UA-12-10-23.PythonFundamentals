from areas import *

change = input("Enter area you need? \n rectangle, triangle, circle ? \n")

if change == "rectangle":
    length = int(input("Enter length rectangle: "))
    width = int(input("Enter width rectangle: "))
    print("Area your rectangle is: ", area_rectangle(length, width))

elif change == "triangle":
    base = int(input("Enter base triangle: "))
    height = int(input("Enter height triangle: "))
    print("Area your triangle is: ", area_triangle(base, height))

elif change == "circle":
    radius = int(input("Enter radius circle: "))
    print("Area your circle is: ", area_circle(radius))
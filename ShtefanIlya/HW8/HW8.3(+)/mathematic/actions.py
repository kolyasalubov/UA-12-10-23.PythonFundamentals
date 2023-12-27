from math import pi, pow  
from time import sleep as sl

def action(act):
    
    def rectangle():
        print("Area of rectangle: ")
        side_a = int(input("Enter side a: "))
        side_b = int(input("Enter side b: "))
        res =  side_a * side_b
        print(f"S = {res}")
        
    def triangle():
        print("Area of triangle: ")
        side_a = int(input("Enter side a: "))
        height_h = int(input("Enter height h: "))
        res = 0.5 * side_a * height_h
        print(f"S = {res}")
        
    def circle():
        print("Area of circle: ")
        radius_r = int(input("Enter radius r: "))
        res = pi * pow(radius_r, 2)
        print(f"S = {round(res, 2)}")
        pass
    
    if act == "rectangle":
        rectangle()
    elif act == "triangle":
        triangle()
    elif act == "circle":
        circle()
    else:
        print("There is no such command!")
        sl(1)
        print("Try again!")
        
    
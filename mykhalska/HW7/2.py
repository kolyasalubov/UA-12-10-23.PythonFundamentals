# 7.2
import math

def count_rect_area(a,b) :
    """ 
    This function accepts two integers (width and length of rectangle)
    count the area of given rectangle and return it
    """
    rect_area = a*b
    return rect_area

def count_triangle_area(a,h) :
    """ 
    This function accepts two integers (length and hight of triangles side)
    count the area of given triangle and return it
    """
    triangle_area = 0.5*a*h 
    return triangle_area

def count_circle_area(r) :
    """ 
    This function accepts one integer (radius of the circle)
    count the area of given circle and return it
    """
    PI = math.pi
    circle_area = round(PI*r**2, 4)
    return circle_area

print("Hi! Choose your figure: \n1.Rectangle \n2.Triangle \n3.Circle")
m = int(input("Choose the number:"))
if m > 3:
    print(f"Sorry, there's no option {m}, try one more time!")
elif m == 1 :
    a = float(input("Enter width of the rectangle: "))
    b = float(input("Enter length of the rectangle: "))
    c = count_rect_area(a,b)
    print(f"Area of this rectengle is {c}")
elif m == 2 :
    a = float(input("Enter hight of the triangle: "))
    h = float(input("Enter length of the triangle: "))
    c = count_triangle_area(a,h)
    print(f"Area of this triangle is {c}")
elif m == 3 :
    r = float(input("Enter radius of the circle: "))
    c = count_circle_area(r)
    print(f"Area of this circle is {c}")
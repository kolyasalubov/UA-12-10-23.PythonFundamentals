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
    circle_area = round(PI*pow(r, 2), 4)
    return circle_area

import math
# 7.1
def return_largest (a, b) :
    """This function accepts two integers and return largest of them"""
    return a if a > b else b 

# 7.2
def count_rect_area(a,b) :
    """ 
    This function accepts two integers (widghs and lenght of rectangle)
    count the area of given rectangle and return it
    """
    area = a*b
    return area

def count_triangle_area(a,h) :
    """ 
    This function accepts two integers (length and hight of triangles side)
    count the area of given triangle and return it
    """
    area = 0.5*a*b 
    return area

def count_circle_area(r) :
    """ 
    This function accepts one integer (radius of the circle)
    count the area of given circle and return it
    """
    PI = math.pi
    area = round(PI*r**2, 4)
    return area

w = count_circle_area(4)
print(w)
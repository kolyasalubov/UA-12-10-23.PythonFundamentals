from math import pi
def area_triangle(height,side):
    '''Calculates triangle area with height and side'''
    return height*side*0.5

def area_rectangle(side1,side2):
    '''Calculates rectangle are'''
    return side1*side2


def area_circle(radius):
    '''Calcuates circle area'''
    return pi* radius*2

def areas(input_):
    '''Decides what function to call'''
    input_ = input_.lower()
    
    match input_:
        case "triangle":
            height = int(input('Enter height of your triangle:'))
            side = int(input('Enter side on which height lie:'))
            print(area_triangle(height,side))
        case "rectangle":
            side1 = int(input("ENter length of first side:"))
            side2 = int(input("Enter your second side:"))
            print(area_rectangle(side1,side2))
        case "circle":
            radius = int(input('Enter your radius:'))
            print(area_circle(radius))
        case _:
            print('Enter the correct  name of the figure')
input_ = input("Enter name of figure")
areas(input_)

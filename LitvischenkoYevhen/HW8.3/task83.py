from area import *

while True :
    print('\n *************************************')
    print("1 . Calculate area of rectangle")
    print("2 . Calculate area of triangle")
    print("3 . Calculate area of circle")
    print("'q' - Exit")
    chois = input("Enter your chois: ")
    match chois:
        case '1':
            print("Calculate area of rectangle")
            print("Area of rectangle = ", area_rectangle(int(input("Enter side 1 :")), int(input("Enter side 2 :"))))
        case '2':
            print("Calculate area of triangle")
            print("Area of triangle = ", area_triangle(int(input("Enter base :")), int(input("Enter higth :"))))
        case '3':
            print("Calculate area of circle")
            print("Area of circle = ", area_circle(int(input("Enter radius :"))))
        case 'q'|'Q':
            break
        case _ :
            print("Wrong chois, try again")
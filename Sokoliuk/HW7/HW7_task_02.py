def rectange_area(length, width):
    return length * width

def triangle_area(base, heigh):
    return (base*heigh)/2

def circle_area(radius):
    PI = 3.14
    return radius**2 * PI

while True:
    print("""
    Hello there! 
    What would you like to choose:
    1 - calculate the rectangle area
    2 - calculate the triangle area
    3 - calculate the circle area
    4 - exit the program
    """)
    action_num = int(input("Enter action number: "))
    match action_num:
        case 1:
            length = float(input("Enter the Length of the rectangle: "))
            width = float(input("Enter the Width of the rectangle: "))
            print(f"The area of the rectange is {rectange_area(length, width):.3f}")
        case 2:
            base = float(input("Enter the Base of the triangle: "))
            heigh = float(input("Enter the Heigh of the triangle: "))
            print(f"The area of the triangle is {triangle_area(base, heigh):.3f}")
        case 3:
            radius = float(input("Enter the Radius of the circle: "))
            print(f"The area of the circle is {circle_area(radius):.3f}")
        case 4:
            print("Goodbye!")
            break
        case _:
            print("Unknown command!\n")
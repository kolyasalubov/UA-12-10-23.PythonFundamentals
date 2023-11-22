<<<<<<< HEAD
import re

def valid_password(password):
    
    if 6 <= len(password) <= 16:
        
        if re.search("[a-z]", password):
            
            if re.search("[A-Z]", password):
                
                if re.search("[0-9]", password):
                    
                    if re.search("[$#@]", password):
                        return True
                    else:
                        print("Password must contain at least one character from [$, #, @].")
                else:
                    print("Password must contain at least one digit [0-9].")
            else:
                print("Password must contain at least one uppercase letter [A-Z].")
        else:
            print("Password must contain at least one lowercase letter [a-z].")
    else:
        print("Password must be between 6 and 16 characters.")

    return False


user_password = input("Enter your password: ")
if valid_password(user_password):
    print("Password is valid.")
else:
    print("Password is not valid.")
=======
import math
from 

def calculate_rectangle_area(length, width):
    return length * width

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_circle_area(radius):
    return math.pi * radius**2

def main():
    print("Choose a shape to calculate the area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    print("4. Exit")

    choice = int(input("Enter your choice (1, 2, 3 or 4): "))

    if choice == 1:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        r_area = area.cra(length, width)
        print(f"The area of the rectangle is: {r_area}")

    elif choice == 2:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = calculate_triangle_area(base, height)
        print(f"The area of the triangle is: {area}")

    elif choice == 3:
        radius = float(input("Enter the radius of the circle: "))
        area = calculate_circle_area(radius)
        print(f"The area of the circle is: {round(area, 2)}")
    
    elif choice ==4:
        print("Goodbye!")
        pass

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

main()
>>>>>>> 34a86bcb2ab2c00deda47a8e680ddd54940f1303

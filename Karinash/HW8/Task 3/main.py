from geometry import rectangle_area, triangle_area, circle_area

def main():
    print("Choose a figure to calculate the area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    choice = input("Enter the number corresponding to your choice: ")

    if choice == '1':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        result = rectangle_area(length, width)
        print(f"The area of the rectangle is: {result}")
    elif choice == '2':
        base = float(input("Enter the base length of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        result = triangle_area(base, height)
        print(f"The area of the triangle is: {result}")
    elif choice == '3':
        radius = float(input("Enter the radius of the circle: "))
        result = circle_area(radius)
        print(f"The area of the circle is: {result}")
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()

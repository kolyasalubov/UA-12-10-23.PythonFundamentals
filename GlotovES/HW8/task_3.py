import geometry_calculator

def main():
    print("Choose a figure to calculate the area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    print("4. Exit")

    choice = int(input("Enter your choice (1, 2, 3 or 4): "))

    if choice == 1:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = geometry_calculator.calculate_rectangle_area(length, width)
        print(f"The area of the rectangle is: {area}")

    elif choice == 2:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = geometry_calculator.calculate_triangle_area(base, height)
        print(f"The area of the triangle is: {area}")

    elif choice == 3:
        radius = float(input("Enter the radius of the circle: "))
        area = geometry_calculator.calculate_circle_area(radius)
        print(f"The area of the circle is: {area}")

    elif choice == 4:
        print("Goodbye!")
        


    else:
        print("Invalid choice. Please enter 1, 2, 3 or 4.")

if __name__ == "__main__":
    main()

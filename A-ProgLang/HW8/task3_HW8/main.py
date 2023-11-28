import areas

def main():
    print("Select a shape to calculate the area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    choice = input("Your choice: ")

    if choice == '1':
        a = float(input("Enter the length of the rectangle (a): "))
        b = float(input("Enter the width of the rectangle (b): "))
        result = areas.rectangle_area(a, b)
        print(f"Area of the rectangle: {result}")
    elif choice == '2':
        a = float(input("Enter the length of the triangle base (a): "))
        h = float(input("Enter the height of the triangle (h): "))
        result = areas.triangle_area(a, h)
        print(f"Area of the triangle: {result}")
    elif choice == '3':
        r = float(input("Enter the radius of the circle (r): "))
        result = areas.circle_area(r)
        print(f"Area of the circle: {result}")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()


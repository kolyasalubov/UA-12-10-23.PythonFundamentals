class Polygon:
    # In this way, you can take 2 separate inputs from user on console
    # Writ 2 inputs in 2 separate lines
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))

    # Now we are using the formula to calculate the Area
    Area = width * height

    # after calculating, simple print it in string
    print("Area of rectangle = " + str(Area))



class Rectangle(Polygon):
    pass


print(Rectangle)
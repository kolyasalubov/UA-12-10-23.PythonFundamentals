def area_of_retraingle():

    """this function calculates area of retraingle by its sides"""
   
    lenght = float(input("Enter the lenght of retraigle:  "))
    width = float(input("Enter the wedth of retraigle:  "))
    area = lenght * width
    return print(area)

def area_of_traingle():

    """this function calculates area of traingle by its height and base"""

    height = float(input("Enter the height of traigle:  "))
    base = float(input("Enter the base of retraigle:  "))
    area = height * base / 2
    return print(area)

def area_of_circle():

    """this function calculates area of circle by its radius"""

    radius = float(input("Enter the radius:  "))
    area = 3.14 * radius ** 2
    return print(area)


print("Сhoose the number of your geometric figure:")
print("1. Rectangle\n2. Traingle\n3. Circle")
choice = int(input("Enter number of your geometric figure: "))

if choice == 1:
    print("Your choice is retraingle.")
    area_of_retraingle()
elif choice == 2:
    print("Your choice is traingle.")
    area_of_traingle()
elif choice == 3:
    print("Your choice is circle.")
    area_of_circle()
else:
    print("invalid input")


    
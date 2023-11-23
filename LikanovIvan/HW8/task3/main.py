from areas import *

while True:
    figure = input("Input a figure, which area you want to know (circle, triangle, rectangle): \t")
    if figure.lower() == 'triangle': print(f'Area of your {figure} is:', tri_area(int(input("Enter the height: \t")), int(input("Enter the side: \t")))); break 
    elif figure.lower() == "circle":
        print(f'Area of your {figure} is:', cir_area(int(input('Enter the radius: \t'))))
        break
    elif figure.lower() == 'rectangle':
        side_a = int(input('Enter the first side: \t'))
        side_b = int(input('Enter the second side: \t'))
        print(f'Area of your {figure} is: {rec_area(side_a, side_b)}')
        break
    else: print("Your input is incorrect.\nTry again!")
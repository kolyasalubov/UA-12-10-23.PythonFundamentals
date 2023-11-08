import random

list_of_numbers = []

for i in range(0, 10):
    list_of_numbers.append(random.randint(1, 100))
    i += 1

print(f"List initialized\n{list_of_numbers}\n")

def change_to_float(list_of_numbers):
    float_list = []
    for number in list_of_numbers:
        number = float(number)
        float_list.append(number)
    return print(f"It's done! Float numbers in a list:\n{float_list}\n")

change_to_float(list_of_numbers)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in my_list:
    if number % 2 == 0:
        print("Even number: ", int(number))
    elif number % 3 == 0:
        print("Odd number: ", int(number))
    else:
        print("numbers that are not divisible by 2 and 3: ", int(number))




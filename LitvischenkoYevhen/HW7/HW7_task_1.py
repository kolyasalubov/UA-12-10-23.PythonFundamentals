def largest_number(number_1, number_2):
    if number_1 < number_2:
        return number_2
    elif number_1 > number_2:
        return number_1
    else:
        print("numbers are equal")
        return None
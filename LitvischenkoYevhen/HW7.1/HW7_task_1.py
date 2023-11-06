def largest_number(number_1, number_2):
    """
    return largest number of two numbers
    if equal - retern first number
    """
    if number_1 < number_2:
        return number_2
    elif number_1 > number_2:
        return number_1
    else:
        return number_1


number_compare_1  = int(input("Enter first compare number :"))
number_compare_2  = int(input("Enter second compare number :"))
print("Largest number is : ", largest_number(number_compare_1, number_compare_2))

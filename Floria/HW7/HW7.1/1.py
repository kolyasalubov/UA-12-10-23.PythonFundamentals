def largest_number(num_1, num_2):
    """Return the largerst number of two"""
    if num_1 < num_2:
        return num_2
    elif num_1 > num_2:
        return num_1
    else:
        return num_1


number_1  = int(input("Enter the first number :"))
number_2  = int(input("Enter the second number :"))
print("Largest number: ", largest_number(number_1, number_2))
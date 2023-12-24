def largest_number(num_1, num_2):
    """Return the largerst number of two"""
    if num_1 < num_2:
        return num_2
    elif num_1 == num_2:
        return ("numbers are equal")
    else:
        return num_1


num_1 = int(input("Enter the first number :"))
num_2 = int(input("Enter the second number :"))
print("Largest number: ", largest_number(num_1, num_2))
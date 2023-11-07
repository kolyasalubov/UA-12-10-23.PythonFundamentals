#Multiples of 3 or 5
def sum_of_condition(num):
    """
    if the number is negative, return 0.
    returns the sum of all the multiples of 3 or 5
    """
    if num < 0 :
        return 0
    return sum([x for x in range(1, num) if (x%3 == 0) or (x%5 == 0)])


input_number = int(input("Enter the number : "))
print("", sum_of_condition(input_number))
def largest_number(first, second):
    if first == second:
        return "They are both equal"
    if first > second:
        return f"The largest number is {first}"
    else:
        return f"The largest number is {second}"


first_number = int(input("Enter first number:\n"))
second_number = int(input("Enter second number:\n"))
print(largest_number(first_number, second_number))

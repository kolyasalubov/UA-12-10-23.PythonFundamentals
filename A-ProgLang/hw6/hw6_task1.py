even_num_divide_2 = [item for item in range(1,11) if item%2 == 0]
print("\nEven numbers that are divisible by 2: ",even_num_divide_2)
odd_num_divide_3 = [item for item in range(1,11) if item%3 == 0]
print("Odd numbers, which are divisible by 3: ",odd_num_divide_3)
num_not_divide_2_3 = [item for item in range(1,11) if item%2 != 0 and item%3 != 0]
print("Numbers that are not divisible by 2 and 3: ", num_not_divide_2_3)
print()
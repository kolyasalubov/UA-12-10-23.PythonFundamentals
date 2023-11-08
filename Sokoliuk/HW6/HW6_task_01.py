numbers = list(range(1, 11))
ls_even, ls_odd, ls_other = [], [], []

ls_even = [number for number in numbers if number % 2 == 0]
print("Even numbers that divisible by 2: ", ls_even)

ls_odd = [number for number in numbers if number % 3 == 0]
print("Odd numbers, which are divisible by 3: ", ls_odd)

ls_other = [number for number in numbers if number % 3 and number % 2 != 0]
print("Numbers that are not divisible by 2 and 3: ", ls_other)

# for number in numbers:
#     if number % 2 == 0:
#         ls_even.append(number)
#     elif number % 3 == 0:
#         ls_odd.append(number)
#     else:
#         ls_other.append(number)
# print("Even numbers that divisible by 2: ", ls_even)
# print("Odd numbers, which are divisible by 3: ", ls_odd)
# print("Numbers that are not divisible by 2 and 3: ", ls_other)
even_list = []
odd_list = []
last_list = []
for i in range(1, 11):
    if i % 2 == 0:
        even_list.append(i)
    if i % 3 == 0 and i % 2 != 0:
        odd_list.append(i)
    if i % 2 != 0 and i % 3 != 0:
        last_list.append(i)
print(f"Even numbers that are divisible by 2:\n{even_list}")
print(f"Odd numbers that are divisible by 3:\n{odd_list}")
print(f"Numbers that are not divisible by 2 and 3:\n{last_list}")

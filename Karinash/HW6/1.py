# Task 1
divisible_by_2 = []
divisible_by_3 = []
not_divisible_by_2_or_3 = []

for num in range(1, 11):
    if num % 2 == 0:
        divisible_by_2.append(num)
    if num % 3 == 0 and num % 2 != 0:
        divisible_by_3.append(num)
    if num % 2 != 0 and num % 3 != 0:
        not_divisible_by_2_or_3.append(num)

print("Numbers divisible by 2:", divisible_by_2)
print("Odd numbers divisible by 3:", divisible_by_3)
print("Numbers not divisible by 2 and 3:", not_divisible_by_2_or_3)

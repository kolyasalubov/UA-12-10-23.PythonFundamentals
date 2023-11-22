even_res = []
odd_res = []
other_res = []

for i in range(1,11):
    if i % 2 == 0:
        even_res.append(i)
    elif i % 2 != 0 and i % 3 == 0:
        odd_res.append(i)
    elif i % 2 != 0 and i % 3 != 0:
        other_res.append(i)

print(f'Your list of even numbers that are divisible by 2: {even_res}')
print(f'Your list of odd numbers that are divisible by 3: {odd_res}')
print(f'Your list of numbers that are not divisible by 2 and 3: {other_res}')
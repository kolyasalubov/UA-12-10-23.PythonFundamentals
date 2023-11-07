l1 = [i for i in range(1,11) if i%2 == 0]
print(f"Divisible by 2: {l1}")

l2 = [i for i in range(1,11) if i%3 == 0 and i%2 ==1]
print(f"Odd numbers that are divisible by 3: {l2}")

l3 = [i for i in range(1,11) if i%2 != 0 and i%3 != 0]
print(f"Numbers that are not divisible by 2 and 3: {l3}")




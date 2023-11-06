print('Even numbers that are divisible by 2 :', [x for x in range(1, 11) if x%2 == 0])
print('Odd numbers that are divisible by 3 :', [x for x in range(1, 11) if x%3 == 0])
print('Numbers that are not divisible by 2 and 3:', [x for x in range(1, 11) if (x%3 != 0) and (x%2 !=0)])

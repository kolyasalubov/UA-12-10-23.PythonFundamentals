a_1=[]
for i in range(1,11):
    if i%2 == 0:
        a_1.append(i)
print(f'Even numbers that are divisible by 2: {a_1}')

#Dictionary comprehension
numbers_1={i for i in range(1,11) if i%2 == 0}
print(numbers_1)

a_2=[]
for i in range(1,11):
    if i%3 == 0:
        a_2.append(i)
print(f'Odd numbers, which are divisible by 3: {a_2}')

#Dictionary comprehension
numbers_2={i for i in range(1,11) if i%3 == 0}
print(numbers_2)

a_3=[]
for i in range(1,11):
    if i%2 != 0 and i%3 != 0:
        a_3.append(i)
print(f'Numbers that are not divisible by 2 and 3: {a_3}')

#Dictionary comprehension
numbers_3={i for i in range(1,11) if i%2 != 0 and i%3 != 0}
print(numbers_3)

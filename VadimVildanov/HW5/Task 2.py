# number_fibonacci = int(input("Enter your limit: "))
# variable_1 = 0
# variable_2 = 1
# variable_3 = variable_2
# count = 1
# while count <= number_fibonacci:
#     variable_1, variable_2 = variable_2, variable_3
#     variable_3 = variable_1 + variable_2
#     print(variable_3, end=" ")
#     count += 1
# print()

n = int(input('enter some number from fibonacci list= '))

fibonacci_numbers = [0, 1]

for i in range(2,n):
 fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])
print(f'there are some numbers from fibanacci till that you entered {n},\n {fibonacci_numbers}')


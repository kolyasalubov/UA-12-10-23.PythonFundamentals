def largest_num(num1:int,num2:int) -> int:
    if num1 > num2: return int(num1)
    else: return int(num2)

num_1 = int(input("Enter your first number: \t"))
num_2 = int(input("Enter your second number: \t"))
print(f'Your largest number is:\t{largest_num(num_1,num_2)}')



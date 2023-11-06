number = int(input("Input number "))
factorial = 1 

if number < 0:
    print('Please add positive number')
elif number == 0:
    print(f'Factorial of {number} is {factorial}')
else:
    f_part_number = [] 
    for i in range(1, number+1):
        factorial *= i
        f_part_number.append(str(i))

    f_part_number_list = " * ".join(f_part_number)
    print(f'The factorial of {number}: {number}! = {f_part_number_list} = {factorial}')
    
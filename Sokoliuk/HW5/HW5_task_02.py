while True:
    input_number = input("Enter up to what number you want to make a fibonacci sequence: ")
    if input_number.isdigit():
        input_number = int(input_number)
        counter = 0
        num_1 = 0
        num_2 = 1
        if input_number < 0:
            print("Please, enter 0 or more, less is impossible\n")
            continue
        elif input_number == 0:
            print("Your sequense:", num_1) 
        elif input_number == 1:
            print("Your sequense:", num_1, num_2)
        else:
            print("Your sequense: ")
            while counter < input_number:
                print(num_1, end = "  ")
                num_sum = num_1 + num_2
                num_1 = num_2
                num_2 = num_sum
                counter += 1
        break
    else:
        print("Enter only a positive digit!\n")



# n = int(input('enter some number from fibonacci list= '))

# fibonacci_numbers = [0, 1]

# for i in range(2, n+1):
#     fibonacci_numbers.append(fibonacci_numbers[i-1] + fibonacci_numbers[i-2])

# print (fibonacci_numbers)
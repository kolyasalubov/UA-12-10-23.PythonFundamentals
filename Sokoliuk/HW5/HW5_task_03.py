while True:
    input_number = input("Enter the number you want to calculate: ")
    if input_number.isdigit():
        input_number = int(input_number)
        factorial = 1
        if input_number == 0:
            print(f"The factorial of {input_number}! = {factorial}")
        else:
            counter = 1
            while counter <= input_number:
                factorial *= counter
                print(f"The factorial of {counter}! = {factorial}")
                counter += 1    
        break
    else:
        print("Enter only a digit!\n")



# input_number = int(input("Input natural number: "))

# fact = 1

# if input_number == 1 or input_number == 0:
#     print("Factorial {}! =".format(input_number), fact)
# elif input_number < 0:
#     print("Factorial non positive number don't exist")
# else:
#     for item in range(1,input_number + 1):
#         fact *= item
#         print("Factorial {}! =".format(item), fact)
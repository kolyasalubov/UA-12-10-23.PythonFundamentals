print("Hello, to start a program press one of the folowing:\n \
1 to print Fibonaci numbers;\n \
2 to calculate the factorial;\n \
3 to exit a program.\n")

while True:
    value = input("What would you like to choose? ")
    if value.isdigit():
        match value:
            case "1":
                while True:
                    input_number = input("Enter up to what number you want to make a fibonacci sequence: ")
                    if value.isdigit():
                        input_number = int(input_number)
                        counter = 0
                        num_1 = 0
                        num_2 = 1
                        if input_number <= 0:
                            print("Please, enter 1 or more, 0 or less is impossible\n")
                        elif input_number == 1:
                            print("Your sequense:", num_1)
                        else:
                            print("Your sequense: ")
                            while counter < input_number:
                                print(num_1, end = "  ")
                                num_sum = num_1 + num_2
                                num_1 = num_2
                                num_2 = num_sum
                                counter += 1
                        print("\n")
                        break
                    else:
                        print("Enter only a digit!\n")
            case "2":
                while True:
                    input_number = input("Enter the number you want to calculate: ")
                    if input_number.isdigit():
                        input_number = int(input_number)
                        if input_number == 0:
                            factorial = 1
                        else:
                            counter = 1
                            factorial = 1
                            while counter <= input_number:
                                factorial *= counter
                                counter += 1
                        print("The factorial of your number is ", factorial)
                        break
                    else:
                        print("Enter only a digit!\n")
            case "3":
                print("\nGoodbye!\n")
                break
            case _:
                print("Unknown command! Try again\n")
    else:
        print("Please, type only what is asking\n")
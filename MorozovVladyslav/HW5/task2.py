def fibonacci_(until_number):
    first_number = 0
    second_number = 1
    print(0)
    for i in range(until_number):
        if  second_number>until_number:
            break
        print(second_number)
        first_number,second_number = (second_number,first_number+second_number)
fibonacci_(21)
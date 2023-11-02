entered_number = input('Enter number: ')
first_digit = int(entered_number[0])
second_digit = int(entered_number[1])
third_digit = int(entered_number[2])
forth_digit = int(entered_number[3])

product_ = first_digit*second_digit*third_digit*forth_digit
print(product_)
#Інша варіація

entered_number = int(entered_number)
first_digit = entered_number%10
second_digit = (entered_number//10)%10
third_digit = (entered_number//100)%10
forth_digit = (entered_number//1000)%10
print(first_digit,second_digit,third_digit,forth_digit)
product_ = first_digit*second_digit*third_digit*forth_digit
print(product_)
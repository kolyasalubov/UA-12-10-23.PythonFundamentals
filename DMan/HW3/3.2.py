user_number = input("Write please a four-digit number ")
digit1 = user_number[0]
digit2 = user_number[1]
digit3 = user_number[2]
digit4 = user_number[3]  

mutiplying_numbers = int(digit1)*int(digit2)*int(digit3)*int(digit4)

print("Product of the the digits of this number is:", mutiplying_numbers)
print("Revers order of this number is:", user_number[::-1])
#print("revers order of your number is:", digit4, digit3, digit2, digit1)
print("Sorted number is:", sorted(user_number))


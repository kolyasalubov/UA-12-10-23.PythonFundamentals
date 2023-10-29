last_number = int(input("Inpust last number "))

#First two fibonacci numbers
f_number_1, f_number_2 = 0, 1
print(f_number_1)
print(f_number_2)

while f_number_1 + f_number_2 <= last_number:
    f_number_next = f_number_1 + f_number_2
    print(f_number_next)
    f_number_1, f_number_2 = f_number_2, f_number_next
    
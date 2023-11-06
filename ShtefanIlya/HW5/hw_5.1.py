length_of_list = int(input("Enter a length: "))
i = 0
int_l = []
while i < length_of_list:
    char = input(f"Try#{i+1} enter any number: ")
    if char.lstrip('-').isdigit():
        int_l.append(int(char))
        i += 1
    else:
        print(f"Char \"{char}\" is not number! Try again.")

print(f"The list of integer elements {int_l}")

float_l = []
for el in int_l:
    print(float(el))
    float_l.append(float(el))
print(f"The list of integer elements {float_l}")


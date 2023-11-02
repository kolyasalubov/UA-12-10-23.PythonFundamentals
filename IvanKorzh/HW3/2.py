number = int(input("Enter 4-digit natural number:"))
st_number = str(number)
count = 1
for element in st_number:
    count *= int(element)
print(f"It is product of the digits of number: {count}")
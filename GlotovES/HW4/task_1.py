temp_c = float(input("Enter the temperature in Celsius: "))

if temp_c > -273.15:
    temp_f = (temp_c * 9/5) + 32
    print(f"{temp_c}C is equivalent to {temp_f}F")
else:
    print("Error: Temperature bellow absolute zero(-273.15C)")
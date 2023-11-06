celsius_input= float(input("Enter temperature in celsius: "))

convert_to_fahrenheit = float((celsius_input*9/5)+32)
absolute_zero= -abs(273.15)
if celsius_input<absolute_zero:
    print(f'{celsius_input}  is below absolute zero')

else:
    print(f'{celsius_input}°C is equivalent to {convert_to_fahrenheit}°F')
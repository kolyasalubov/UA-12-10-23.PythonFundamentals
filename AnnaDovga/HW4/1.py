print('Enter the temperature in Celsius ', end = '')
temper_C = float(input())
if temper_C < -273.15:
    print('Error: Temperature below absolute zero')
else:
    print('Temperature in Fahrenheit ', temper_C * (9 / 5) + 32)

    
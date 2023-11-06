temperature_celsius = float(input("Enter the temperature in Celsius:"))

if temperature_celsius > -273.15:
    temperature_fahrenheit = (temperature_celsius * 9/5) + 32
    print(f'{temperature_celsius}\u2103\u0020 is equivalent to {temperature_fahrenheit}\u2109')
else: 
    print('Error: Temperature below absolute zero (-273.15\u2103\u0020)')

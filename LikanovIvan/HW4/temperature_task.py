try:
    c = float(input('Enter temperature in Celcius (not less than -273.15°С):\t'))
    if c > -273.15:
        f = (c*9/5)+32
        print(f'{c}°C is equivalent to {f}°F')
    else:
        print('Temperature below absolute zero (-273.15°C)')
except ValueError:
    print('ValueError: not correct data type')

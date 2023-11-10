celsius = float(input("Enter the temperature in Celsius: "))

if celsius >= -273.15:
    fahrenheit = (celsius * 9/5) + 32

    print(f"{celsius}°C is equivalent to {fahrenheit:.2f}°F")
else:
    print("Error: Temperature below absolute zero (-273.15°C)")

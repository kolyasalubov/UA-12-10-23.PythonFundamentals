print("Enter the temperature in Celsius: ")

temperature = float(input())
if temperature < -273.15:
    print("Temperature below absolute zero (-273.15°C)")
else:
    print("Enter the temperature in Fahrenheit: ", temperature * (9/5) + 32)

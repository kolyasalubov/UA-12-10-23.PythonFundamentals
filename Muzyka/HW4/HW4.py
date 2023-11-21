# Prompt the user to enter a temperature in Celsius
celsius = float(input("Enter the temperature in Celsius: "))

# Check if the entered temperature is below absolute zero
if celsius < -273.15:
    print("Error: Temperature below absolute zero (-273.15°C)")
else:
    # Convert Celsius to Fahrenheit using the formula
    fahrenheit = (celsius * 9/5) + 32

    # Print the converted temperature in Fahrenheit
    print(f"{celsius}°C is equivalent to {fahrenheit}°F")

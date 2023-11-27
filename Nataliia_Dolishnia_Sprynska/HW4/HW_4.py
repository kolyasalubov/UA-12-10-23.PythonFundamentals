def celsius_to_fahrenheit(celsius):
    if celsius < -273.15:
        print(f"Error: Temperature below absolute zero ({celsius}°C)")
    else:
 
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equivalent to {fahrenheit}°F")

celsius_input = float(input("Enter the temperature in Celsius: "))

celsius_to_fahrenheit(celsius_input)

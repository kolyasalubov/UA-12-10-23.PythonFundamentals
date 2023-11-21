user_temperature_celsius = float(input("Enter the temperature in degrees Celsius: "))
if user_temperature_celsius < -273.15:
    print("Error: Temperature below absolute zero (-273.15°C)")
else:
    fahrenheit_temperature = (user_temperature_celsius * 9/5+32)
    print(f"{user_temperature_celsius}°C is equivalent to {fahrenheit_temperature:.2f}°F")
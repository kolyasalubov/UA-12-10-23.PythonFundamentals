celsius = float(input("Enter the temperature in Celsius: "))

if celsius < -273.15:
        print("Error: Temperature below absolute zero (-273.15°C)")
else:
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius :.2f}°C is equivalent to {fahrenheit :.2f}°F")
    

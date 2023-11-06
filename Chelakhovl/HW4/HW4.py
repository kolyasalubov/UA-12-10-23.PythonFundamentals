Celsius = float(input("Enter a temperature in Celsius: "))
Fahrenheit = (Celsius * 9/5) + 32

if Celsius <= -273.15:
    print("Error: Temperature below absolute zero '-273.15°C'")
else:
    print (f"{Celsius}°C is equivalent to {Fahrenheit}°F")
    
    
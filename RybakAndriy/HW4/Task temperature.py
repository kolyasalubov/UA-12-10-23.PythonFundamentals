temperature = float(input("Enter the temperture in Celsius:"))
if temperature < -273.15:
    print("Error: Temperature below absolute zero (-273.15°C)")
else:
    F = (temperature * 9/5) + 32    
    print(f"{temperature}°C is equivalent to {F}°F")

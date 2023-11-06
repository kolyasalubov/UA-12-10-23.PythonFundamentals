C = int(input("Enter the temperature in Celsius:"))
F = (C * (9/5)) + 32
if F < -273.15:
    print("Error: Temperature below absolute zero(-273.15°C)")
else:
    print(f"{C}° is equivalent to {F}°F")

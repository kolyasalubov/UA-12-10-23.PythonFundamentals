while True:

    cel=int(input("Hi! Enter the temperature in Celsius: "))

    if cel < -273.15:
        print("Error: Temperature below absolute zero (-273.15°C)")
    else: 
        fahren=int((cel*9/5)+32)
        print(f"{cel}°C is equivalent to {fahren}°F")
    
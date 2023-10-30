celsius = float(input("input temp °C: "))

if celsius < -273.15:
    print("wrong: temp is low (-273.15°C)")
else:
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C equivalently {fahrenheit}°F")
# Temperature converter
celsius = int(input("Enter the temperature in Celsius: "))
fahrenheit = (celsius * 9/5)+32
if celsius>= -273.15 :
    print(celsius,"°C is equivalent to ", fahrenheit, "°F")
else :
    print("Error: Temperature below absolute zero (-273.15 °C)")
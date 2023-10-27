C = float(input("Enter temperature in degrees Celsius to convert "))
Fahrenheit = 9 * C / 5 + 32

if C > -273.15: 
    print("{}°C is equvalent to {}°F".format(C, Fahrenheit))
elif C == 273.15:
    print("The temperature is absolute zero")
else: 
    print("Error! Temperature below absolute zero (-273.15°C)")

exit
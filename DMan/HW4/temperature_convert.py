C = float(input("Enter temperature in Celsius to convert"))
Fahrenheit = 9 * C / 5 + 32

message = "{}°C is equvalent to {}°F".format(C, Fahrenheit) 

while Fahrenheit <= -273.15: 
    print(message)

    match 
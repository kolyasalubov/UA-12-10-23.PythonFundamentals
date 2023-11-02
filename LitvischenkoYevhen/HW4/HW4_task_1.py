def convert_fahrenheit(temp_c):
#check fo valid input data    
    try:
        temp_c = float(temp_c)
    except ValueError:
        return "Errore: Not valid input temperature"
#check absolute zero
    if temp_c < -273.15 :
        return "Error: Temperature below absolute zero (-273.15°C)"
    else:
#conver temperature        
        temp_f = temp_c*9/5+32
        return f"{temp_c}°C is equivalent to {temp_f:.2f}°F"

#cycle input data until enter q
while True:
    temp  = input("Enter the temperature in Celsius or 'Q' to quit: ")
    if temp.lower() == 'q':
        break
    else:
        print(convert_fahrenheit(temp))
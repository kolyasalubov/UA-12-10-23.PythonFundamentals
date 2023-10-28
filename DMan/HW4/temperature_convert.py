print("1. Celcius\n2. Fahrenheit\n3. Kelvin")
choice = int(input("Select measurement scale number "))

match choice:
    case 1:
        c = float(input("Enter temperature in degrees Celsius to convert "))
        f= 1.8*c+32
        k= c+273.15

        if c > -273.15: 
            print("{:.2F}°C = {:.2F}°F".format(c, f))
            print("{:.2F}°C = {:.2F}°K".format(c, k)) #так буде мати кращий вигляд?
        elif c == 273.15:
            print("The temperature is absolute zero")
        elif c < -273.15: 
            print("Error! Temperature below absolute zero (-273.15°C)")
        else:
            print("Invalid input")

    case 2:
        print("Convert from Fahrenheit to Celcius and Kelvin")
        f = float(input("Enter temperature in degrees Fahrenheit to convert "))
        c = (f-32)/1.8 
        k = (f+459.67)/1.8

        if f > -459.67 : 
            print("{:.2F}°F = {:.2F}°C\n{:.2F}°F = {:.2F}°K".format(f, c, f, k)) #чи так буде краще?
        elif f == -459.67:
            print("The temperature is absolute zero")
        elif f < -459.67: 
            print("Error! Temperature below absolute zero (-459.67°F)")
        else:
            print("Invalid input")
       
    case 3:
        print("Convert from Kelvin to Celcius and Fahrenheit")
        k = float(input("Enter temperature in degrees Kelvin to convert "))
        c = k-273.15
        f = 1.8*k-459.67

        if k > 0: 
            print("{:.2F}°K = {:.2F}°C\n{:.2F}°K = {:.2F}°F".format(k, c, k, f))
        elif k == 0:
            print("The temperature is absolute zero")
        elif k < 0: 
            print("Error! Temperature below absolute zero (-273.15°C)")
        else:
            print("Invalid input")

    case _: 
        print("There is no such scale")
        
exit
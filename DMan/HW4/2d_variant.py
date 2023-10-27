print("1. Celcius\n2. Fahrenheit\n3. Kelvin")
choice = int(input("Select measurement scale number"))

if choice == 1:
    print("Convert from Celcius to Fahrenheit and Kelvin")    
    c1 = float(input("Enter temperature in degrees Celsius "))
    f1= 1.8*c1+32
    k1= c1+273.15
    print("{}°C is equvalent to {}°F".format(c1, f1))
    print("{}°C is equvalent to {}°K".format(c1, k1))  #так краще вигляд буде?

elif choice == 2:
    print("Convert from Fahrenheit to Celcius and Kelvin")
    f2 = float(input("Enter temperature in degrees Fahrenheit"))
    c2 = (f2-32)/1.8 
    k2 = (f2+459.67)/1.8
    print("{}={}°C\n{}={}°K".format(f2, c2, f2, k2)) #чи так?

elif choice == 3:
    print("Convert from Kelvin to Celcius and Fahrenheit")
    k3 = float(input("Enter temperature in degrees Kelvin"))
    c3 = k3-273.15
    f3 = 1.8*k3-459.67
    print("{}={}°C\n{}={}°K".format(k3, c3, k3, f3))

else:
    print("Error! Invalid input") 



    
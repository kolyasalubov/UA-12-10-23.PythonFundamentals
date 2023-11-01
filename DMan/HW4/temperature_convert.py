# print("1. Celcius\n2. Fahrenheit\n3. Kelvin")
# choice = int(input("Select measurement scale number "))
            #cycle   
while True:
     print("1. Celcius\n2. Fahrenheit\n3. Kelvin")
     choice = int(input("Select measurement scale number "))
            #convert from celsius
     match choice:
         case 1:
             print("Press 'q' to finish")
             c = input("Enter temperature in degrees Celsius to convert ")
             if c == "q":
                 break
             else:
                 c = float(c)
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
#convert from Fahrenheit
         case 2:
             print("Press 'q' to finish")
             f = input("Enter temperature in degrees Fahrenheit to convert ")
             if f == "q":
                 break
             else:
                f = float(f)
                c = (f-32)/1.8 
                k = (f+459.67)/1.8

                if f > -459.67 : 
                    print("{0:.2F}°F = {1:.2F}°C\n{0:.2F}°F = {2:.2F}°K".format(f, c, k)) #чи так буде краще?
                elif f == -459.67:
                    print("The temperature is absolute zero")
                elif f < -459.67: 
                    print("Error! Temperature below absolute zero (-459.67°F)")
                else:
                    print("Invalid input")
#convert from Kelvin       
         case 3:
             print("Press 'q' to finish")
             k = input("Enter temperature in degrees Kelvin to convert ")
             if k =="q":
                 break
             else:
                k = float(k)
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
#error
         case _: 
             print("There is no such scale")

exit()
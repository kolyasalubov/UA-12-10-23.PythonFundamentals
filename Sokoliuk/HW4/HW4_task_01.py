print("Program for americans (Temperature converter)\n")
print("If you want to stop the program, type 'stop'\n")

while True:
    cel = input("Enter the temperature in Celsius: ")
    if cel == "stop":
        break
    try:
        cel = float(cel)
        if cel < -273.15:
            print("Error: Temperature below absolute zero (-273.15)")
        else:
            fahr = (cel * 9/5) + 32
            print(f"{cel}°C is equal to {fahr}℉")
    except ValueError:
        print("The program works only with numbers!\n")

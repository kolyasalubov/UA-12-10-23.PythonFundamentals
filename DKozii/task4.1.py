celcium = float(input("Enter temperature in celcium"))
fahrenheit = (celcium*9/5+32)
if celcium <= -273.15:
   print("temperature is apsolutely zero")
else:
   print("temperature in fahrenheit is", fahrenheit)

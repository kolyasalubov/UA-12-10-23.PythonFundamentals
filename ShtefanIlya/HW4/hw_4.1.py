temperature_c = float(input("Enter a temperature in °C: "))
temperature_f = (temperature_c * 9/5) + 32
absolute_zero = -273.15
if temperature_f < absolute_zero:
    print(f"""Error!\nYou had entered an {temperature_c} °C.
That means that temperature is less then absolute zero {absolute_zero} in °F.
""")
elif temperature_f == absolute_zero:
    print(f"""You had entered an {temperature_c} °C, this is {temperature_f} in°F.
That is an absolute zero {absolute_zero} in °F.
""")
else:
    print(f"You had entered an {temperature_c} °C, that is {temperature_f} in °F.")


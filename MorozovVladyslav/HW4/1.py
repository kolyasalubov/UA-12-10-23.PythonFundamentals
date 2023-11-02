input_ = int(input('Enter temperature: '))


if input_< - 273.15:
    raise ValueError("Temperature below absolute zero (-273.15°C)")
else:
    temperature = int(((input_*(1.8))+32))

print(temperature)
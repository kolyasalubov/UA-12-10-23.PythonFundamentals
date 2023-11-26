import module

figure = input('Enter your figure: ')

match figure.lower():
    case 'circle':
        result = module.area_of_circle(int(input('Enter your radius: ')))
    case 'rectangle':
        result = module.area_of_rectangle(int(input('Enter your  first side: ')),int(input('ENter your second side: ')))
    case 'triangle':
        result = module.area_of_triangle(int(input('Enter your  side: ')),int(input('ENter your height: ')))

print(result)

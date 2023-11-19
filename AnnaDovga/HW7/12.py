#from math import pi

# Підкажіть, де правильно визивати бібліотеку math
# на початку програми чи в тілі функціі, якщо
# вона необхідна тількі в тілі однієї функції

def rect(a, b):
    '''
    Return area of rectangle
    '''
    
    print('Area of rectangle: ', int(a) * int(b))

def trian(a, b):
    '''
    Return area of triangle
    '''
    
    print('Area of triangle: ', int(a) * int(b) / 2)

def circle(a):
    '''
    Return Aria of circle
    '''
    
    from math import pi
    print('Area of circle: ', int(a) * int(a) * pi)

figure = int(input('Choice rectangle - 1, triangle - 2 or circle - 3 '))
if figure == 1:
    print('Side lengths:')
    rect(input('first side: '), input('second side: '))
elif figure == 2:
    print('Altitude and side triangle: ')
    trian(input('altitude: '), input('side: '))
elif figure == 3:
    circle(input('Radius: '))
else:
    print('This figure is missing')

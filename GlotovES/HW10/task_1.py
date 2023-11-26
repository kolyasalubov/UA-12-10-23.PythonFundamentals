class polygon():
    def __init__(self, length, width):
        self.length = length
        self.width = width

class rectangle(polygon):
    
    def cra(self):
        '''
        Calculate rectangle area
        '''
        area = length * width
        return area
    

length = int(input("Input length of rectangle: "))
width = int(input("Input width of rectangle: "))
print(f"Rectangle area is {rectangle(length, width).cra()}")

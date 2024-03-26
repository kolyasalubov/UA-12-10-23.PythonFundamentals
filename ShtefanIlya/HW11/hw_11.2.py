class IncorrectDay(Exception):
    def __init__(self, data):
        self.data = data
    
    def __str__(self):
        return repr(f"Error: {self.data}")



def validate_data(number):
    match number:
        case 1:
            return "Monday"
        
        case 2:
            return "Tuesday"
        
        case 3:
            return "Wednesday"
        
        case 4:
            return "Thursday"
        
        case 5:
            return "Friday"
        
        case 6:
            return "Saturday"
        
        case 7:
            return "Sanday"
        
        case _:
            raise IncorrectDay("There is no such day")

try:
    day = int(input("Enter the day of week: "))
    validate_data(day)
    
except ValueError as e:
    e = "Error: Here is must be only nymbers from 1 to 7."
    print(e)

except IncorrectDay as e:
    print(e)
    
else:
    print(f"You choose day {day}, so it is a {validate_data(day)}")

finally:
    if 1 <= day <= 7:
        print("Program was ended successfully")
    else:
        print("Program was not ended successfully")
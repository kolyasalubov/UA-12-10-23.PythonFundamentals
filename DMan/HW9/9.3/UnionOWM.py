import tkinter as tk
from tkinter import *
from pyowm import OWM
from config import *
from langid import classify


owm = OWM(key)
mgr = owm.weather_manager()

root = Tk()
root.geometry('800x600')
root.title("Weather Application")

def get_weather():

    """"
    The weather in the selected city is calculated and 
    displayed in Ukrainian and English languages
    """

    city = entry_field.get()
    observation = mgr.weather_at_place(city)
    w = observation.weather
    detect_language = classify(city)

    if detect_language[0] == 'uk':
        weather_info = (f"Хманість y місті {city}\n 
                       {w.detailed_status}\n"
                       f"Температура дорівнює 
                       {round(w.temperature('celsius')['temp'], 2)}°C"
                       f"\nШвидкicть вітру станове {w.wind()['speed']}"
                        "км/год\n"
                       f"Вологість повітрю станове {w.humidity}")
    elif detect_language[0] == 'en':
        weather_info = (f"Conditions of {city} city\n: 
                       {w.detailed_status}\n"
                       f"Temperature is {round(w.temperature('celsius')
                                                ['temp'], 2)}"
                       "°C" f"\nWind speed is {w.wind()['speed']} 
                       km/hour\nHumidity "
                       f"of the air is {w.humidity}")
    else:
        weather_info = ("Invalid input/Неправільне введення")
        
    label['text'] = weather_info



frame = tk.Frame(root, bg = "deep sky blue", bd = 5)
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75,
             relheight = 0.1, anchor = 'n')

lower_frame = tk.Frame(root, bg = 'gold', bd = 10)
lower_frame.place(relx = 0.5, rely = 0.25, relwidth = 0.75,
                  relheight = 0.6, anchor = 'n')

label = tk.Label(lower_frame, font = ('Courier', 12))
label.place(relx = 0, rely = 0, relwidth =1 , relheight = 1)

entry_field = tk.Entry(frame, font = ('Courier', 12))
entry_field.place(relx = 0, rely = 0, relwidth = 0.65, relheight = 1)

button = tk.Button(frame, 
                    text = "Get Weather", 
                    bg = "gray", fg = "white", 
                    font = ('Courier', 8), 
                    command = lambda: get_weather())
button.place(relx = 0.7, rely = 0, relwidth = 0.3, relheight = 1)




root.mainloop()
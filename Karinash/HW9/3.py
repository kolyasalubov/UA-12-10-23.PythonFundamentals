from pyowm import OWM
import tkinter as tk
from tkinter import font

API_KEY = 'ef2206ff5da67de63306d0b143e20872'

def get_weather():
    location = entry_field.get()
    try:
        observation = mgr.weather_at_place(location)
        w = observation.weather

        weather_info = f'Detailed Status: {w.detailed_status}\nWind: {w.wind()}\nHumidity: {w.humidity}\nTemperature: {w.temperature("celsius")}\nRain: {w.rain}\nHeat Index: {w.heat_index}\nClouds: {w.clouds}'

        label['text'] = weather_info
    except Exception as e:
        label['text'] = f"Error: {str(e)}"

owm = OWM(API_KEY)
mgr = owm.weather_manager()

HEIGHT = 350
WIDTH = 450

root = tk.Tk()
root.title("Weather Application")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=get_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()

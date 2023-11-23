import tkinter as tk
from tkinter import font
from pyowm import OWM

HEIGHT = 550
WIDTH = 550

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

API_KEY = 'ef2206ff5da67de63306d0b143e20872'

def get_weather():
    city = entry_field.get()  
    owm = OWM(API_KEY)
    mgr = owm.weather_manager()
    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather
        detailed = w.detailed_status
        wind = w.wind()
        humidity = w.humidity
        temperature = w.temperature('celsius')
        weather_info = (
            f"Weather Details: {detailed}\n"
            f"Wind Speed: {wind['speed']} m/s\n"
            f"Humidity: {humidity}%\n"
            f"Temperature: {temperature['temp']}°C"
        )
        label.config(text=weather_info)
    except Exception as e:
        label.config(text=f"Error: {e}")

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

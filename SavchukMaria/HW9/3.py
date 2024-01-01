import tkinter as tk
from pyowm import OWM


HEIGHT = 350
WIDTH = 450
API_KEY = 'ef2206ff5da67de63306d0b143e20872'  # this is test API key

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()


def weather_info(weather_list):
    info_string = ""
    for element in weather_list:
        if type(element) == dict:
            for key, value in element.items():
                info_string = info_string + str(key) + ": " + str(value) + "\n"
        else:
            info_string = info_string + str(element) + "\n"

    return label.configure(text=info_string)


def get_weather():
    owm = OWM(API_KEY)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(entry_field.get())
    w = observation.weather
    weather_list = [w.detailed_status,
                    w.wind(),
                    w.humidity,
                    w.temperature('celsius'),
                    w.rain,
                    w.heat_index,
                    w.clouds]
    return weather_info(weather_list)


frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Times New Roman', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="white",
                   font=('Courier', 8),
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Arial', 14), anchor="nw", justify="left")
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
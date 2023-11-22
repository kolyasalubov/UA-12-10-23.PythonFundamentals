import tkinter as tk
from tkinter import font
from Muzyka.HW9.chapter3.OWM import Weather

HEIGHT = 500
WIDTH = 600

root = tk.Tk()

weather = Weather()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

def update_label_text():
    if hasattr(weather, 'result'):
        text = "\n".join([f"{key}: {value}" for key, value in weather.result.items()])
        label.config(text="")
        label.config(text=text, wraplength=400)
    else:
        label.config(text="")

button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="white",
                   font=('Courier', 8),
                   command=lambda: [weather.get_weather(entry_field.get()), update_label_text()])
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 10), justify='left')
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()

import tkinter as tk
from OWM import get_weather

HEIGHT = 350
WIDTH = 450


def click_on_button():
    label.delete(tk.END)
    result = get_weather(entry_field.get())
    label.insert(tk.END, f"Status:{result.detailed_status}\n")
    label.insert(tk.END, f"Speed:{result.wind()['speed']}м/с\n")
    label.insert(tk.END, f"Humidity:{result.humidity}%\n")
    label.insert(tk.END, f"Temperature:{result.temperature('celsius')['temp']}°C\n")
    label.insert(tk.END, f"Temperature minimum and maximum:{result.temperature('celsius')['temp_min']}°C - {result.temperature('celsius')['temp_max']}°C\n")
    label.insert(tk.END, f"Rain:{result.rain if result.rain != {} else 'Without rain'}\n")
    label.insert(tk.END, f"Heat index:{result.heat_index}\n")
    label.insert(tk.END, f"Clouds:{result.clouds}%")


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()



frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)


root.mainloop()


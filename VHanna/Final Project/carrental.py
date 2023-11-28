from tkinter import *
import tkinter.messagebox
import sqlite3
from datetime import datetime

def calculate_rent_cost(pick_up_date, drop_off_date):
    cost_of_day = 42
    cost_for_month = 45

    days_difference = (drop_off_date - pick_up_date).days
    full_months = (drop_off_date.year - pick_up_date.year) * 12 + (drop_off_date.month - pick_up_date.month)

    rent_cost = 0
    if full_months > 0:
        rent_cost += (full_months - 1) * cost_for_month 
        rent_cost += (30 - pick_up_date.day) * cost_of_day  
        rent_cost += drop_off_date.day * cost_of_day  
    elif days_difference > 0:
        rent_cost = days_difference * cost_of_day

    return max(0, rent_cost)

def save(event):
    city, address, name, phone_number = ent1_city.get(), ent2_adress.get(), ent3_name.get(), ent4_phone.get()
    length = len(phone_number)

    if city and address and name and phone_number:
        if length >= 10:
            pick_up_date = datetime.strptime(f"{var1_pickupd.get()} {var2_pickupm.get()}", "%d %B")
            pick_up_time = datetime.strptime(f"{var5_uphour.get()}:{var6_upminute.get()}", "%H:%M")
            drop_off_date = datetime.strptime(f"{var3_dropofd.get()} {var4_dropofm.get()}", "%d %B")
            drop_off_time = datetime.strptime(f"{var7_offhour.get()}:{var8_offminute.get()}", "%H:%M")

            pickup_date_str = pick_up_date.strftime("%d %B")
            pickup_time_str = pick_up_time.strftime("%H:%M:%S")
            dropoff_date_str = drop_off_date.strftime("%d %B")
            dropoff_time_str = drop_off_time.strftime("%H:%M:%S")

            car, purpose = var9_car.get(), rad0.get()

            rent_cost = calculate_rent_cost(pick_up_date, drop_off_date)

            conn = sqlite3.connect('rentcar.db')
            with conn:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO rentcar (city, address, name, phone_number, PickupDate, PickupTime, DropoffDate, DropoffTime, purpose, rent_cost, car) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                               (city, address, name, phone_number, pickup_date_str, pickup_time_str, dropoff_date_str, dropoff_time_str, purpose, rent_cost, car))
            conn.commit()
            message = "Success! You have been registered! Rent cost is: $" + str(rent_cost)
            title = "result".title()
            tkinter.messagebox.showinfo(title, message)
        else:
            message = "Wrong phone number"
            title = "result".title()
            tkinter.messagebox.showinfo(title, message)
    else:
        message = "Do not leave any empty fields"
        title = "result".title()
        tkinter.messagebox.showinfo(title, message)

def readdb(q, conn):
    cursor1 = conn.cursor()
    cursor1.execute('SELECT * FROM rentcar')

    for row in cursor1.fetchall():
        if row[3] == q:
            inf1, inf2, inf3, inf4, inf5, inf6, inf7, inf8, inf9, inf10, inf11 = row
            message = f"Name: {inf3}\nCity: {inf1}\nAddress: {inf2}\nPhone Number: {inf4}\nPickup Date: {inf5}\nPickup Time: {inf6}\nDropoff Date: {inf7}\nDropoff Time: {inf8}\nPurpose: {inf9}\nRent Cost: {inf10}\nCar: {inf11}"
            title = "result".title()
            tkinter.messagebox.showinfo(title, message)

def find(event):
    root2 = Tk()
    root2.title("Find")
    root2.geometry('400x200')

    def on_find_button_click():
        q = ent.get()
        connn = sqlite3.connect('rentcar.db')
        with connn:
            readdb(q, connn)

    lab = Label(root2, text="Enter client's number:", font="Arial 15")
    lab.place(x=10, y=10)
    
    ent = Entry(root2, width=25, bd=3)
    ent.place(x=210, y=15)
    
    close = Button(root2, text=" Close ", font="Arial 20", bg="firebrick2", command=root2.destroy)
    close.place(x=270, y=130)
    
    find_button = Button(root2, text="Find", font="Arial 20", bg="dodgerblue", command=on_find_button_click)
    find_button.place(x=170, y=130)

    root2.mainloop()

root = Tk()
root.title("Car Hire – Search, Compare & Save")
root.geometry('1100x600')

img  = PhotoImage(file="header-img.png")
ima = Label(root,image=img) 
ima.place(x=0,y=0, relwidth=1, relheight=1) 
ima.image = img

Startlabel = Label(root, text="Welcome to the Car Renting system!", font="Fixedsys 17 italic")
Startlabel.place(x = 500, y = 0)

lab = Label(root, text="City", font="Arial 15")
lab.place(x=10, y=0)
ent1_city = Entry(root,width=30,bd=3)
ent1_city.place(x=150, y=5)

lab = Label(root, text="Address", font="Arial 15")
lab.place(x=10, y=40)
ent2_adress = Entry(root,width=30,bd=3)
ent2_adress.place(x=150, y=45)

lab = Label(root, text="Full name", font="Arial 15")
lab.place(x=10, y=80)
ent3_name = Entry(root,width=30,bd=3)
ent3_name.place(x=150, y=85)

lab = Label(root, text="Phone number", font="Arial 15")
lab.place(x=10, y=120)
ent4_phone = Entry(root,width=30,bd=3)
ent4_phone.place(x=150, y=125)

lab = Label(root,text="<<More details>>", font="Helvetica 15")
lab.place(x=170, y=160)

lab = Label(root, text="Pick-up Date:", font="Arial 15")
lab.place(x=10, y=190)
mainframe = Frame(root)
mainframe.place(x=10,y=220)
var1_pickupd = StringVar(root)
var1_pickupd.set('Day')
choices = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
option1 = OptionMenu(mainframe,var1_pickupd,*choices)
option1.grid(row=1, column=1)

mainframe = Frame(root)
mainframe.place(x=75,y=220)
var2_pickupm=StringVar(root)
var2_pickupm.set('Month')
choices = ['January','February','March','April','May','June','July','August','September','October','November','December']
option2 = OptionMenu(mainframe,var2_pickupm,*choices)
option2.grid(row=1, column=1)

lab = Label(root, text="Drop-off Date:", font="Arial 15")
lab.place(x=310, y=190)
mainframe = Frame(root)
mainframe.place(x=310,y=220)
var3_dropofd=StringVar(root)
var3_dropofd.set('Day')
choices = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
option3 = OptionMenu(mainframe,var3_dropofd,*choices)
option3.grid(row=1, column=1)

mainframe = Frame(root)
mainframe.place(x=375,y=220)
var4_dropofm = StringVar(root)
var4_dropofm.set('Month')
choices = ['January','February','March','April','May','June','July','August','September','October','November','December']
option4 = OptionMenu(mainframe,var4_dropofm,*choices)
option4.grid(row=1, column=1)

lab = Label(root, text="Time:", font="Arial 14")
lab.place(x=10, y=260)
mainframe = Frame(root)
mainframe.place(x=10,y=290)
var5_uphour = StringVar(root)
var5_uphour.set('Hour')
choices = ['07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
option5 = OptionMenu(mainframe,var5_uphour,*choices)
option5.grid(row=1, column=1)
mainframe = Frame(root)
mainframe.place(x=80,y=290)
var6_upminute = StringVar(root)
var6_upminute.set('Minute')
choices = ['00','15','30','45']
option6 = OptionMenu(mainframe,var6_upminute,*choices)
option6.grid(row=1, column=1)

lab = Label(root, text="Time:", font="Arial 14")
lab.place(x=310, y=260)
mainframe = Frame(root)
mainframe.place(x=310,y=290)
var7_offhour = StringVar(root)
var7_offhour.set('Hour')
choices = ['07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
option7 = OptionMenu(mainframe,var7_offhour,*choices)
option7.grid(row=1, column=1)
mainframe = Frame(root)
mainframe.place(x=380,y=290)
var8_offminute=StringVar(root)
var8_offminute.set('Minute')
choices = ['00','15','30','45']
option8 = OptionMenu(mainframe,var8_offminute,*choices)
option8.grid(row=1, column=1)

mainframe = Frame(root)
mainframe.place(x=380,y=350)
var9_car = StringVar(root)
var9_car.set('Car')
choices = ['Kia Sedona (Mini Van)','Ford F150 (Pickup)','Chevy Silverado (Pickup)','Toyota RAV4 (SUV)','Ford Focus','Hyundai Accent','Hyundai Santa Fe (SUV)','Nissan Versa','Toyota Yaris','Mitsubishi Mirage','Volkswagen Jetta','Chevrolet Cruze','Hyundai Elantra']
option4 = OptionMenu(mainframe,var9_car,*choices)
option4.grid(row=1, column=1)

lab = Label(root, text="Purpose of rental", font="Arial 14")
lab.place(x=10, y=350)
rad0 = StringVar()
rad0.set(1)
Radiobutton(root,text="Business", font="Arial 9", variable=rad0,value="Business").place(x=210, y=354)
Radiobutton(root,text="Leisure", font="Arial 9", variable=rad0,value="Leisure").place(x=290, y=354)

lab = Label(root, text="No credit card fees", font="Arial 10 italic")
lab.place(x=10, y=405)
lab = Label(root, text="No amendment fees", font="Arial 10 italic")
lab.place(x=10, y=425)
lab = Label(root, text="24/7 phone support", font="Arial 10 italic")
lab.place(x=10, y=445)
lab = Label(root, text="Longer you take, less you pay", font="Arial 10 italic")
lab.place(x=10, y=465)

close = Button(root, text=" Close ",font="Arial 20",bg="firebrick2", command=root.destroy)
close.place(x=630,y=440)
newbutton1 = Button(root,text="Register", font="Arial 20",bg="white")
newbutton1.place(x=421,y=440)
newbutton1.bind('<Button-1>',save)
fin = Button(root,text="Find",font="Arial 20",bg="dodgerblue")
fin.place(x=550,y=440)
fin.bind('<Button-1>',find)

root.mainloop()

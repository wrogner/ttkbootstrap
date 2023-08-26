#!/usr/bin/env python3

""" 08_date_entry.py

Date Entry

:author:	wolf
:created:	2023.08.26
"""


import tkinter as tk
import ttkbootstrap as tbs
from ttkbootstrap.constants import *
from datetime import date
from ttkbootstrap.dialogs import Querybox  # floating date entry box

app = tbs.Window(themename="cosmo")
app.title("TTK Bootstrap!")
app.iconbitmap("img/favicon.ico")
app.geometry("500x350")

# define command functions
def get_date_entered():
    label_1.config(text=f"You picked: {date_1.entry.get()}")

def get_querybox_date():
    calendar = Querybox()   # Querybox takes no arguments
    date_selected = calendar.get_date(title='Pick a date', firstweekday=0, startdate=date.today())
    label_1.config(text=f"You picked: {date_selected}")
    # how to change the value of date_1?

# define GUI
date_1 = tbs.DateEntry(firstweekday=0, startdate=date.today())
date_1.pack(pady=50)


button_1 = tbs.Button(text="Get Date", bootstyle="outline", command=get_date_entered)
button_1.pack(pady=20)

button_2 = tbs.Button(text="Set Date", command=get_querybox_date)
button_2.pack(pady=20)

label_1 = tbs.Label(text="Pick something")
label_1.pack(pady=20)

app.mainloop()

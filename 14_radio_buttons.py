#!/usr/bin/env python3

""" 14_radio_buttons.py

Radio buttons

:author:	wolf
:created:	2023.09.15
"""


import tkinter as tk
import ttkbootstrap as tbs
from ttkbootstrap.constants import *


app = tbs.Window(themename="cosmo")
app.title("TTK Bootstrap!")
app.iconbitmap("img/favicon.ico")
app.geometry("500x450")

def clicker():
    label_1.config(text=f"You Selected: {my_topping.get()}")

# create radio button list
toppings= ["Pepperoni", "Cheese", "Veggie"]

my_topping = tbs.StringVar()

for topping in toppings:
    tbs.Radiobutton(bootstyle="danger",
                    variable=my_topping,
                    text=topping,
                    value=topping,
                    command=clicker).pack(pady=20)

button_1 = tbs.Button(text="Click Me!", command=clicker)
button_1.pack(pady=20)

# INFO: this does not work as we cannot access label_1 in clicker any more (AttributeError: 'NoneType' object has no attribute 'config')
# label_1 = tbs.Label(text="You Selected: ").pack(pady=20)
label_1 = tbs.Label(text="You Selected: ")
label_1.pack(pady=20)

# create radio button buttons

rb_1 = tbs.Radiobutton(bootstyle="info toolbutton",
                       variable=my_topping,
                       text="Radio Button 1",
                       value="Radio Button 1",
                       command=clicker)
rb_1.pack(pady=20)

# INFO: if you later want to reassign attributes, pack separately
# INFO: else, pack inline

rb_2 = tbs.Radiobutton(bootstyle="info toolbutton  outline",
                       variable=my_topping,
                       text="Radio Button 2",
                       value="Radio Button 2",
                       command=clicker).pack(pady=20)

app.mainloop()
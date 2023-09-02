#!/usr/bin/env python3

""" 10_menu_buttons.py

Menu buttons

:author:	wolf
:created:	2023.09.02
"""


import tkinter as tk
import ttkbootstrap as tbs
from ttkbootstrap.constants import *


app = tbs.Window(themename="cosmo")
app.title("TTK Bootstrap!")
app.iconbitmap("img/favicon.ico")
app.geometry("500x350")

def stuff(x):
    menu_button_1.config(bootstyle=x)
    label_1.config(text=f"You selected: {x}")

# create the menu button
menu_button_1 = tbs.Menubutton(text="Things!")
menu_button_1.pack(pady=50)

# create basic menu
menu_1 = tbs.Menu(menu_button_1)

# items in menus
item_var = tbs.StringVar()
for x in ["primary", "secondary", "success", "danger", "info", "outline primary", "outline secondary"]:
    menu_1.add_radiobutton(label=x, variable=item_var, command=lambda x= x: stuff(x))

# associate menu with menu button
menu_button_1['menu'] = menu_1

label_1 = tbs.Label()
label_1.pack(pady=40)



app.mainloop()
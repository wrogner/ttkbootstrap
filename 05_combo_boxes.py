#!/usr/bin/env python3

""" 05_combo_boxes.py

TTKbootstrap combo boxes
:author:	wolf
:created:	2023.08.19
"""

import tkinter as tk
import ttkbootstrap as tbs
from ttkbootstrap.constants import *

app = tbs.Window(themename="cosmo")
app.title("TTK Bootstrap!")
app.iconbitmap("img/favicon.ico")
app.geometry("500x350")

# define functions
def clicker():
    label_1.config(text=f"You clicked on {combo_1.get()}!")

def click_bind(e):
    label_1.config(text=f"You clicked on {combo_1.get()}!")

def reset(e):
    label_1.config(text="Hello World!")

# create label
label_1 = tbs.Label(app, text="Hello World!", font=(".AppleSystemUIFont", 18))
label_1.pack(pady=30)

# create dropdown options
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# create combo
combo_1 = tbs.Combobox(app, bootstyle="default", values=days,)
combo_1.current(0)
combo_1.pack(pady=20)
# bind the combo box
combo_1.bind("<<ComboboxSelected>>", click_bind)
combo_1.bind("<Return>", reset)

# create button
button_1 = tbs.Button(app, text="Click Me!", command=clicker, bootstyle="danger")
button_1.pack(pady=20)

app.mainloop()

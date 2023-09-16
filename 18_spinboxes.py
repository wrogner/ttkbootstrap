#!/usr/bin/env python3

""" 18_spinboxes.py

Spinboxes

:author:	wolf
:created:	2023.09.16
"""


import tkinter as tk
import ttkbootstrap as tbs
from ttkbootstrap.constants import *


app = tbs.Window(themename="cosmo")
app.title("TTK Bootstrap!")
app.iconbitmap("img/favicon.ico")
app.geometry("500x350")

def get_spinner():
    label_1.config(text=spinner_1.get())

spin_list = ["John", "April", "Bob", "Mary"]

spinner_1 = tbs.Spinbox(font=(".AppleSystemUIFont", 18),
                        from_=0, to=10,
                        values=spin_list,   # replaces from_ to
                        state="readonly",
                        command=get_spinner)
# spinner_1.pack(pady=20)
spinner_1.set(spin_list[0])
spinner_1.pack(pady=20)

button_1 = tbs.Button(style="success", text="Get value by clicking!", command=get_spinner)
button_1.pack(pady=20)

label_1 = tbs.Label(text="", font=(".AppleSystemUIFont", 18))
label_1.pack(pady=20)
app.mainloop()
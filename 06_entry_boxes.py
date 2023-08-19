#!/usr/bin/env python3

""" 06_entry_boxes.py

Entry boxes

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

def click():
    label_1.config(text=f"You typed: {entry_1.get()}")

entry_1 = tbs.Entry(bootstyle="success", font=(".AppleSystemUIFont", 18), foreground="red", width=25, show="*")
entry_1.pack(pady=50)

button_1 = tbs.Button(text="Click Me!", bootstyle="danger outline", command=click)
button_1.pack(pady=20)

label_1 = tbs.Label(text="")
label_1.pack(pady=20)

app.mainloop()
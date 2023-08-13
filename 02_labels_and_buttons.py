#!/usr/bin/env python3

""" 02_labels_and_buttons.py

First app with some function added

:author:	wolf
:created:	2023.08.13
"""

import tkinter as tk
import ttkbootstrap as tbs
from ttkbootstrap.constants import *


app = tbs.Window(themename="cosmo")
app.title("TTK Bootstrap!")
app.iconbitmap("img/favicon.ico")
app.geometry("500x350")

# function for the button
counter = 0
def changer():
    global counter
    counter += 1
    if counter % 2 == 0:
        label_1.config(text="Hello World!")
    else:
        label_1.config(text="Goodbye World!")


# label
label_1 = tbs.Label(text="Hello World!", font=(".AppleSystemUIFont", 32), bootstyle="default")
label_1.pack(pady=50)

# button
button_1 = tbs.Button(text="Click Me!", bootstyle="default", command=changer)
button_1.pack(pady=20)

app.mainloop()
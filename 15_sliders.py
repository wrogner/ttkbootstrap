#!/usr/bin/env python3

""" 15_sliders.py

Sliders

:author:	wolf
:created:	2023.09.15
"""


import tkinter as tk
import ttkbootstrap as tbs
from ttkbootstrap.constants import *


app = tbs.Window(themename="cosmo")
app.title("TTK Bootstrap!")
app.iconbitmap("img/favicon.ico")
app.geometry("500x350")

def scaler(event):
    label_1.config(text=f"{int(scale_1.get())}%")

scale_1 = tbs.Scale(bootstyle="primary",
                    length=200,
                    orient="horizontal",
                    from_=0,
                    to=100,
                    command=scaler,
                    # state="disabled",
                    )
scale_1.pack(pady=50)

label_1 = tbs.Label(font=(".AppleSystemUIFont", 18))
label_1.pack()

app.mainloop()
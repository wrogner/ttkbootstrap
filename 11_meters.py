#!/usr/bin/env python3

""" 11_meters.py

Meters

:author:	wolf
:created:	2023.09.03
"""


import tkinter as tk
import ttkbootstrap as tbs
from ttkbootstrap.constants import *


app = tbs.Window(themename="cosmo")
app.title("TTK Bootstrap!")
app.iconbitmap("img/favicon.ico")
app.geometry("500x550")

global counter
counter = 20

def clicker():
    global counter
    # TODO: this logic sucks
    meter_1.configure(amountused=counter)
    counter += 5
    if counter > 100: counter = 0
    button_1.configure(text=f"Click Me {meter_1.amountusedvar.get()}")

def step_up():
    # global counter
    # counter += 5
    # if counter > 100:
    #     counter = 0
    # meter_1.configure(amountused=counter)

    # INFO: step handles delta strangely
    meter_1.step(10)


def step_down():
    # global counter
    # counter -= 5
    # if counter < 0:
    #     counter = 100
    # meter_1.configure(amountused=counter)

    # INFO: step does not handle negatives properly
    meter_1.step(-10)

# for full parameter list -> https://ttkbootstrap.readthedocs.io/en/latest/api/widgets/meter/
meter_1 = tbs.Meter(bootstyle="danger",
                    subtext="TKinter learned",
                    # subtextfont="-size 20",
                    interactive=True,
                    textright="%",
                    # textleft="whatever",
                    textfont="-size 20",
                    # metertype="semi",
                    meterthickness=20,
                    stripethickness=10,
                    # wedgesize=20,
                    # metersize=300,
                    # padding=50,
                    amountused=counter,
                    # amounttotal=120,
                    )
meter_1.pack(pady=50)

button_1 = tbs.Button(text="Click Me 5", command=clicker)
button_1.pack(pady=20)

button_2 = tbs.Button(text="Step Up", command=step_up)
button_2.pack(pady=20)

button_3 = tbs.Button(text="Step Down", command=step_down)
button_3.pack(pady=20)

app.mainloop()
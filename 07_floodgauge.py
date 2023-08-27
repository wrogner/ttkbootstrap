#!/usr/bin/env python3

""" 07_floodgauge.py

Floodgauge examples

:author:	wolf
:created:	2023.08.23
"""


import tkinter as tk
import ttkbootstrap as tbs
from ttkbootstrap.constants import *

app = tbs.Window(themename="cosmo")
app.title("TTK Bootstrap!")
app.iconbitmap("img/favicon.ico")
app.geometry("500x450")

def starter():
    gauge_1.start()

def stopper():
    gauge_1.stop()

def incrementer():
    gauge_1.step(10)
    label_1.config(text=f"Position: {gauge_1.variable.get()}")

gauge_1 = tbs.Floodgauge(bootstyle="default", font=(".AppleSystemUIFont", 18),
                         mask="Pos: {}%", maximum=100, value=0,
                         # orient="vertical" # fill bottom up
                         orient="horizontal",
                         mode="determinate")
gauge_1.pack(pady=50, fill=X, padx=30)

button_start = tbs.Button(text="Start", bootstyle="danger outline", command=starter)
button_start.pack(pady=20)

button_stop = tbs.Button(text="Stop", bootstyle="danger outline", command=stopper)
button_stop.pack(pady=20)

button_increment = tbs.Button(text="Increment", bootstyle="danger outline", command=incrementer)
button_increment.pack(pady=20)

label_1 = tbs.Label(text="Position: ")
label_1.pack(pady=20)

app.mainloop()
#!/usr/bin/env python3

""" 13_progress_bars.py

Progress bars

:author:	wolf
:created:	2023.09.09
"""


import tkinter as tk
import ttkbootstrap as tbs
from ttkbootstrap.constants import *
import time                 # used for auto


app = tbs.Window(themename="cosmo")
app.title("TTK Bootstrap!")
app.iconbitmap("img/favicon.ico")
app.geometry("500x350")

def start():
    progress_1.start(10)
    label_1.config(text=progress_1["value"])

def stop():
    current_progress = progress_1["value"]
    label_1.config(text=current_progress)
    progress_1.stop()
    progress_1.config(value=current_progress)

def auto():
    global app
    for _ in range(5):
        increment()
        app.update()        # update_idletasks() as suggested in the tutorial does not work
        time.sleep(1)

def increment():
    # progress_1.step(20)   # restarts at 100
    if progress_1["value"] < 100:
        progress_1["value"] += 20
    else:
        progress_1["value"] = 0
    # get current value
    label_1.config(text=progress_1["value"])

progress_1 = tbs.Progressbar(bootstyle="success striped",
                             maximum=100,
                             value=0,
                             length=300,
                             mode="determinate",        # indeterminate goes up and down
                             )
progress_1.pack(pady=40)

frame_1 = tbs.Frame()
frame_1.pack(pady=20)

button_1 = tbs.Button(frame_1, text="Increment 20", command=increment)
button_1.grid(column=0, row=0, padx=10)

button_2 = tbs.Button(frame_1, text="Start", command=start)
button_2.grid(column=1, row=0, padx=10)

button_3 = tbs.Button(frame_1, text="Stop", command=stop)
button_3.grid(column=2, row=0, padx=10)

button_4 = tbs.Button(frame_1, text="Auto", command=auto)
button_4.grid(column=3, row=0, padx=10)

label_1 = tbs.Label(text="", font=(".AppleSystemUIFont", 18))
label_1.pack(pady=20)

app.mainloop()
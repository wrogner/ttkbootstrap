#!/usr/bin/env python3

""" 09_labels_and_frames.py

Create frames and some things about labels

:author:	wolf
:created:	2023.08.27
"""


import tkinter as tk
import ttkbootstrap as tbs
from ttkbootstrap.constants import *

app = tbs.Window(themename="cosmo")
app.title("TTK Bootstrap!")
app.iconbitmap("img/favicon.ico")
app.geometry("500x350")


def button_clicked():
    pass

frame_1 = tbs.Frame(app, bootstyle="light")         # omit bootstyle to get invisible frames
frame_1.pack(pady=40)

entry_1 = tbs.Entry(frame_1, font=(".AppleSystemUIFont", 18))
entry_1.pack(pady=20, padx=20)

button_1 = tbs.Button(frame_1, text="CLICK ME!", bootstyle="outline", command=button_clicked)
button_1.pack(pady=20, padx=20)

label_1 = tbs.Label(app, text="Hello there!", font=(".AppleSystemUIFont", 18), bootstyle="dark")
label_1.pack(pady=20)

app.mainloop()

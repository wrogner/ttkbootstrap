#!/usr/bin/env python3

""" 23_scrolled_frame.py

Scrolled frames

:author:	wolf
:created:	2023.09.18
"""


import tkinter as tk
import ttkbootstrap as tbs
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame


app = tbs.Window(themename="cosmo")
app.title("TTK Bootstrap!")
app.iconbitmap("img/favicon.ico")
app.geometry("500x350")

scroll_frame_1 = ScrolledFrame(autohide=True, style="dark")
scroll_frame_1.pack(pady=20, padx=20, fill=BOTH, expand=YES)

for i in range(1, 21):
    tbs.Button(scroll_frame_1, text=f"Button {i}").pack(pady=20)

app.mainloop()
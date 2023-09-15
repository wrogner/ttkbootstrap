#!/usr/bin/env python3

""" 16_scrollbars.py

Scroll bars

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

frame_1 = tbs.Frame()
frame_1.pack(pady=20)


# vertical scrollbar
scroll_y = tbs.Scrollbar(master=frame_1, orient="vertical", style="round")
scroll_y.pack(side="right", fill="y")

# horizontal scrollbar
scroll_x = tbs.Scrollbar(master=frame_1, orient="horizontal", style="round")
scroll_x.pack(side="bottom", fill="x")


text_1 = tk.Text(master=frame_1, width=30, height=25,
                 yscrollcommand=scroll_y.set,
                 xscrollcommand=scroll_x.set,
                 wrap="none", font=(".AppleSystemUIFont", 18))
text_1.pack()

scroll_y.config(command=text_1.yview)
scroll_x.config(command=text_1.xview)

app.mainloop()
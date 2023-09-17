#!/usr/bin/env python3

""" 21_color_chooser.py

Color chooser

:author:	wolf
:created:	2023.09.16
"""


import tkinter as tk
import ttkbootstrap as tbs
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs.colorchooser import ColorChooserDialog


app = tbs.Window(themename="cosmo")
app.title("TTK Bootstrap!")
app.iconbitmap("img/favicon.ico")
app.geometry("500x350")

def color_chooser():
    cc = ColorChooserDialog()
    cc.show()
    color = cc.result
    if color:
        # result attributes: .hex, .rgb, .hsl
        label_1.config(text=color.rgb)
        app.config(background=color.hex)
    else:
        label_1.config(text="No color selected")

button_1 = tbs.Button(text="Click Me!", command=color_chooser)
button_1.pack(pady=40)

label_1 = tbs.Label(text="", font=(".AppleSystemUIFont", 18))
label_1.pack(pady=20)

app.mainloop()
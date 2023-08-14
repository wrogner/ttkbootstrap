#!/usr/bin/env python3

""" 04_resizing_buttons.py

Resize buttons

This requires to create a style

:author:	wolf
:created:	2023.08.14
"""

import tkinter as tk
import ttkbootstrap as tbs
from ttkbootstrap.constants import *

app = tbs.Window(themename="cosmo")
app.title("TTK Bootstrap!")
app.iconbitmap("img/favicon.ico")
app.geometry("500x350")

# style
style = tbs.Style()
# styles need to be named according to the bootstyle attributes !!!
style.configure("success.Outline.TButton", font=(".AppleSystemUIFont", 28))

# you need not add outline to bootstyle
# you have to add the custom style using the style parameter
button_1 = tbs.Button(text="Hello World!", bootstyle="success", style="success.Outline.TButton", width=20)
button_1.pack(pady=40)

app.mainloop()
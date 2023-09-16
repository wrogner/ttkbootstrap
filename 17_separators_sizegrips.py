#!/usr/bin/env python3

""" 17_separators_sizegrips.py

Separators and size grips

:author:	wolf
:created:	2023.09.16
"""


import tkinter as tk
import ttkbootstrap as tbs
from ttkbootstrap.constants import *


app = tbs.Window(themename="cosmo")
app.title("TTK Bootstrap!")
app.iconbitmap("img/favicon.ico")
app.geometry("500x350")

label_1 = tbs.Label(text="Label 1")
label_1.pack(pady=40)

sep_1 = tbs.Separator()
sep_1.pack(fill="x", padx=40)

label_2 = tbs.Label(text="Label 2")
label_2.pack(pady=40)

# size grip, not required in MacOS
# size_grip_1 = tbs.Sizegrip(style="danger")
# size_grip_1.pack(anchor="se", fill="both", expand=True)

app.mainloop()
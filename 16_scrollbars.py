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



app.mainloop()
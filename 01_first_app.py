#!/usr/bin/env python3

""" 01_first_app.py

First App using ttkbootstrap

:author:	wolf
:created:	2023.08.13
"""

import tkinter as tk
import ttkbootstrap as tbs
from ttkbootstrap.constants import *

app = tbs.Window()

button_1 = tbs.Button(app, text="Button 1", bootstyle=SUCCESS)
button_1.pack(side=LEFT, padx=5, pady=10)

button_2 = tbs.Button(app, text="Button 2", bootstyle=(INFO, OUTLINE))
button_2.pack(side=LEFT, padx=5, pady=10)

app.mainloop()
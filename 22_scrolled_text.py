#!/usr/bin/env python3

""" 22_scrolled_text.py

Scrolled text

:author:	wolf
:created:	2023.09.17
"""


import tkinter as tk
import ttkbootstrap as tbs
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledText      # required to get all attributes

app = tbs.Window(themename="cosmo")
app.title("TTK Bootstrap!")
app.iconbitmap("img/favicon.ico")
app.geometry("500x350")

# tbs.ScrolledText does not provide full featureset
# refer to source code for explanation
scroll_text_1 = tbs.ScrolledText(height=5, width=70, wrap=WORD, tabs=4)
scroll_text_1.pack(pady=20, padx=20)

scroll_text_2 = ScrolledText(height=5, width=70, wrap=WORD, autohide=True, padding=20)
scroll_text_2.pack()

app.mainloop()
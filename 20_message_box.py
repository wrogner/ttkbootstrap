#!/usr/bin/env python3

""" 20_message_box.py

Message boxes

:author:	wolf
:created:	2023.09.16
"""


import tkinter as tk
import ttkbootstrap as tbs
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox


app = tbs.Window(themename="cosmo")
app.title("TTK Bootstrap!")
app.iconbitmap("img/favicon.ico")
# app.iconbitmap(default="img/favicon.ico")
app.geometry("500x350")

def message_box():
    # yesno, yesnocancel, ok (returns None), okcancel, show_info, show_error, show_question, show_warning
    # none returned by closing dialog
    # md = Messagebox.yesno("Display some message here", "MB Title")
    # md = Messagebox.ok("Display some message here", "MB Title")
    # md = Messagebox.okcancel("Display some message here", "MB Title")

    md = Messagebox.retrycancel("Display some message here", "MB Title")
    # if md == "No":
    #     print("No")
    # else:
    #     print("Yes")
    label_1.config(text=f"You clicked {md}")

button_1 = tbs.Button(text="Click Me!", command=message_box)
button_1.pack(pady=40)

label_1 = tbs.Label(text="", font=(".AppleSystemUIFont", 18))
label_1.pack(pady=20)

app.mainloop()
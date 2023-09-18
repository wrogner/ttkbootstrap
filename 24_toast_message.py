#!/usr/bin/env python3

""" 24_toast_message.py

Toast message

:author:	wolf
:created:	2023.09.18
"""


import tkinter as tk
import ttkbootstrap as tbs
from ttkbootstrap.constants import *
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.icons import Icon, Emoji


app = tbs.Window(themename="cosmo")
app.title("TTK Bootstrap!")
app.iconbitmap("img/favicon.ico")
app.geometry("500x350")

toast_1 = ToastNotification(title="Alarm!",
                            message="This is an alarm going off",
                            duration=5000,                  # duration of 0 = infinite (you have to click the thing)
                            alert=True,                     # get a blip
                            position=(100, 30, "ne"),       # x / y -> shift to center
                            icon=Emoji.get("RAISED HAND")   # icon can be set to show emojis
                            )

def raise_alarm():
    toast_1.show_toast()

button_1 = tbs.Button(text="Alarm!", command=raise_alarm)
button_1.pack(pady=40)

app.mainloop()
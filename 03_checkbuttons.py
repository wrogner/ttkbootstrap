#!/usr/bin/env python3

""" 03_checkbuttons.py

Check buttons

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


# action function
def checker():
    if var_1.get() == 1:
        label_1.config(text="Uncheck the checkbutton")
    else:
        label_1.config(text="Check the checkbutton")

# this function prints a StringVar
def test():
    print("in test")
    if var_5a.get():
        print(var_5a.get())

# label
label_1 = tbs.Label(text="Click the checkbutton below", font=(".AppleSystemUIFont", 32))
label_1.pack(pady=(40, 10))     # 40 from top, 10 below

# checkbutton
var_1 = tk.IntVar()
my_check = tbs.Checkbutton(bootstyle="primary", text="Check me out",
                           variable=var_1, onvalue=1, offvalue=0, command=checker)
my_check.pack(pady=10)

# toolbutton
var_2 = tk.IntVar()
my_check_2 = tbs.Checkbutton(bootstyle="danger, toolbutton", text="ToolButton!!",
                             variable=var_2, onvalue=1, offvalue=0)
var_2.set(1)
my_check_2.pack(pady=20)

# outline toolbutton
var_3 = tk.IntVar()
my_check_3 = tbs.Checkbutton(bootstyle="danger, toolbutton, outline", text="Outlined ToolButton!!",
                             variable=var_3, onvalue=1, offvalue=0)
my_check_3.pack(pady=20)

# round toggle button
var_4 = tk.IntVar()
my_check_4 = tbs.Checkbutton(bootstyle="success, round-toggle", text="Round toggle",
                             variable=var_4, onvalue=1, offvalue=0)
my_check_4.pack(pady=10)

# square toggle button
var_5 = tk.IntVar()
var_5a = tk.StringVar()

my_check_5 = tbs.Checkbutton(bootstyle="primary, square-toggle", text="Square toggle",
                             variable=var_5, onvalue=1, offvalue=0, command=test)
my_check_5.pack(pady=10)

var_5a.set("value")


app.mainloop()
#!/usr/bin/env python3

""" 12_notebooks.py

Notebooks

:author:	wolf
:created:	2023.09.03
"""


import tkinter as tk
import ttkbootstrap as tbs
from ttkbootstrap.constants import *


app = tbs.Window(themename="cosmo")
app.title("TTK Bootstrap!")
app.iconbitmap("img/favicon.ico")
app.geometry("500x350")

notebook_1 = tbs.Notebook(bootstyle="light")
notebook_1.pack(pady=20)

frame_1 = tbs.Frame(master=notebook_1)
frame_2 = tbs.Frame(master=notebook_1)

label_1 = tbs.Label(master=frame_1, text="My Awesome Label!", font=(".AppleSystemUIFont", 18))
label_1.pack(pady=20)

text_1 = tbs.Text(master=frame_1, width=70, height=10)
text_1.pack(pady=10, padx=10)

button_1 = tbs.Button(master=frame_1, text="Click Me!", bootstyle="outline danger")
button_1.pack(pady=20)

label_2 = tbs.Label(master=frame_2, text="This is Tab 2", font=(".AppleSystemUIFont", 18))
label_2.pack(pady=20)

# add frames to notebook
notebook_1.add(frame_1, text="Tab One")
notebook_1.add(frame_2, text="Tab Two")


app.mainloop()
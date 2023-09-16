#!/usr/bin/env python3

""" 19_treeview.py

Treeview

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

# define columns
columns = ("first_name", "last_name", "email")

# create treeview
tree_1 = tbs.Treeview(style="dark",
                      columns=columns,
                      show="headings",
                      # padding=20,
                      height=15)
tree_1.pack(pady=40, padx=40)

# define headings
tree_1.heading("first_name", text="First Name")
tree_1.heading("last_name", text="Last Name")
tree_1.heading("email", text="Email")

# create sample data
contacts = []
for n in range(1,20):
    contacts.append((f"First {n}", f"Last {n}", f"email{n}@address.com"))

# add data to treeview
for contact in contacts:
    tree_1.insert("", "end", values=contact)


app.mainloop()
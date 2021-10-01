# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 07:55:38 2021

@author: enzoa
"""

from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title('Check boxes')
root.geometry("400x200")

# drop down boxes

#  listas são mais fáceis de editar depois
OPTIONS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thrusday",
    "Friday",
    "Saturday"
    ]

def show():
    label = Label(root, text=clicked.get()).pack()

# variável para receber o valor
clicked = StringVar()
clicked.set(OPTIONS[0]) # valor inicial

# menu
drop = OptionMenu(root, clicked, *OPTIONS)
drop.pack()

# botão para mostrar a ação
button = Button(root, text="Show Selection", command=show)
button.pack()

root.mainloop()
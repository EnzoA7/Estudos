# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 15:07:56 2021

@author: enzoa
"""

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Check boxes')
root.geometry("400x400")

def show():
    label = Label(root, text=var.get()).pack()

# precisa declarar uma variável para passar para a check box
# padrão box -> desmarcado = 0 -- marcado = 1
var = IntVar()

c = Checkbutton(root, text="Check this box, I dare you!", variable=var)
c.pack()


button = Button(root, text="Show selection", command=show)
button.pack()

root.mainloop()

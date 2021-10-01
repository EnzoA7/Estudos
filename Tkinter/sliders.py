# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 21:32:55 2021

@author: enzoa
"""

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Sliders')
root.geometry("400x400")

vertical = Scale(root, from_=0, to=400)
vertical.pack()

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

label = Label(root, text=horizontal.get()).pack()

def slide():
    label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get())) 


btn = Button(root, text="Click Me!", command=slide).pack()

root.mainloop()

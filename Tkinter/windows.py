# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 20:01:06 2021

@author: enzoa
"""

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

# Janela
root = Tk()
# título
root.title('Images')
# ícone
root.iconbitmap('C:/Users/enzoa/Dev/Spyder notebooks/Estudos/Tkinter/icon.ico')


def open():
    global img
    top = Toplevel()
    top.title('My second window')
    top.iconbitmap('C:/Users/enzoa/Dev/Spyder notebooks/Estudos/Tkinter/icon.ico')
    img = ImageTk.PhotoImage(Image.open("Geofluxo.jpeg"))
    label = Label(top, image=img).pack()
    btn2 = Button(top, text='close windows', command=top.destroy).pack()

btn = Button(root, text="Open second window", command=open).pack()

root.mainloop()
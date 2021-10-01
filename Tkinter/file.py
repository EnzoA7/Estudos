# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 23:27:13 2021

@author: enzoa
"""

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

# Janela
root = Tk()
# título
root.title('Images')
# ícone
root.iconbitmap('C:/Users/enzoa/Dev/Spyder notebooks/Estudos/Tkinter/icon.ico')

FILE_TYPES = (("png files", "*.png"),("all files", "*.*"))

# Comando
def open():
    global img
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=FILE_TYPES)
    label = Label(root, text=root.filename).pack()
    img = ImageTk.PhotoImage(Image.open(root.filename))
    img_label = Label(image=img).pack()


# Botão
btn = Button(root, text="Open File", command=open)
btn.pack()

root.mainloop()

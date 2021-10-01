# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 19:42:54 2021

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

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.showinfo("This is my Poup!", "Hello World!")
    Label(root, text=response).pack()
    # if response == 'yes':
    #     Label(root, text="You clicked yes").pack()
    # else:
    #     Label(root, text="You clicked no").pack()


Button(root, text='Popup', command=popup).pack()


root.mainloop()

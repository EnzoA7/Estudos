# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 21:00:48 2021

@author: enzoa
"""

from tkinter import *
from PIL import ImageTk, Image

# Janela
root = Tk()
# título
root.title('Images')
# ícone
root.iconbitmap('C:/Users/enzoa/Dev/Spyder notebooks/Estudos/Tkinter/icon.ico')

# Imagem
img1 = ImageTk.PhotoImage(Image.open('as_vert_cor.jpg'))
img2 = ImageTk.PhotoImage(Image.open('Geofluxo.jpeg'))
img3 = ImageTk.PhotoImage(Image.open('as_vert_cor.jpg'))

image_list = [img1, img2, img3]

status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

label = Label(image=img1)
label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global label
    global button_forward
    global button_back
    
    label.grid_forget()
    label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))
    
    if image_number == len(image_list):
        button_forward = Button(root, text=">>", state=DISABLED)
    
    label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    return

def back(image_number):
    global label
    global button_forward
    global button_back
    
    label.grid_forget()
    label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

    
    return



# Botão

button_back = Button(root, text="<<", command=back, state=DISABLED)
button_quit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)


# Status
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()
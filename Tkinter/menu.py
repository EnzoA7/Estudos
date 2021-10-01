# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:19:17 2021

@author: enzoa
"""

from tkinter import *

root = Tk()
root.title('Menu')
root.geometry("400x400")


# Comandos
def our_command():
    label = Label(root, text="Você clicou em um Menu Dropdown").pack()

def file_new():
    hide_all_frames()
    file_new_frame.pack(fill='both', expand=1)
    label = Label(file_new_frame, text="Você clicou em um novo menu >>> novo").pack()


def edit_cut():
    hide_all_frames()    
    edit_cut_frame.pack(fill='both', expand=1)
    label = Label(edit_cut_frame, text="Você clicou em um novo menu >>> cortar").pack()
    

def hide_all_frames():
    file_new_frame.pack_forget()
    edit_cut_frame.pack_forget()


# Menu
menu = Menu(root)
root.config(menu=menu) # associa à janela o menu

# menu arquivo
file_menu = Menu(menu, tearoff=0)
menu.add_cascade(label='Arquivo', menu=file_menu)
file_menu.add_command(label='New...', command=file_new)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit)

# menu editar
edit_menu = Menu(menu, tearoff=0)
menu.add_cascade(label='Editar', menu=edit_menu)
edit_menu.add_command(label='Cut', command=edit_cut)
edit_menu.add_command(label='Copy', command=our_command)

# menu opções
option_menu = Menu(menu, tearoff=0)
menu.add_cascade(label='Opções', menu=option_menu)
option_menu.add_command(label='Find', command=our_command)
option_menu.add_command(label='Find next', command=our_command)

# cria alguns quadros
file_new_frame = Frame(root, width=400, height=400, bg='red')
edit_cut_frame = Frame(root, width=400, height=400, bg='blue')

root.mainloop()

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 08:46:12 2021

@author: enzoa
"""


from tkinter import *

root = Tk()
root.title('Paineis')
root.geometry("400x400")

# Paineis
panel_1 = PanedWindow(bd=4, relief='raised', bg='red')
panel_1.pack(fill=BOTH, expand=1)
left_label = Label(panel_1, text='Painel Esquerdo')
panel_1.add(left_label) # em paineis sempre se adiciona

panel_2 = PanedWindow(panel_1, orient=VERTICAL, bd=4, relief='raised', bg='blue')
panel_1.add(panel_2) 
top = Label(panel_2, text="Painel Topo")
panel_2.add(top)
bottom = Label(panel_2, text="Painel Inferior")
panel_2.add(bottom)


root.mainloop()

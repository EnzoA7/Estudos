# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 21:17:57 2021

@author: enzoa
"""

from tkinter import *
from tkinter import ttk # modulo com o tab

root = Tk()
root.title('tabs')
root.geometry("500x500")

# notebooks abrigam as tabs
notebook = ttk.Notebook(root)
notebook.pack(pady=15)

def hide():
    notebook.hide(1)

def show():
    notebook.add(frame_2, text='Red Tab')

def navigate():
    notebook.select(1)

frame_1 = Frame(notebook, width=500, height=500, bg='blue')
frame_2 = Frame(notebook, width=500, height=500, bg='red')

frame_1.pack(fill='both', expand=1)
frame_2.pack(fill='both', expand=1)

notebook.add(frame_1, text='Blue Tab')
notebook.add(frame_2, text='Red Tab')

# Esconde uma tab
button_1 = Button(frame_1, text="Hide Tab 2", command=hide).pack(pady=10)
# Apresenta uma tab
button_2 = Button(frame_1, text="Show Tab 2", command=show).pack(pady=10)
# Navega por tab
button_3 = Button(frame_1, text="Ir para a Tab 2", command=navigate).pack(pady=10)


root.mainloop()

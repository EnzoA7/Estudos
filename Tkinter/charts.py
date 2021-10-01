# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 20:03:37 2021

@author: enzoa
"""

from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title('Check boxes')
root.geometry("400x200")

def graph():
    house_prices = np.random.normal(2000000, 25000, 5000)
    plt.hist(house_prices, 50)
    plt.show()

button = Button(root, text="Graph It", command=graph)
button.pack()

root.mainloop()
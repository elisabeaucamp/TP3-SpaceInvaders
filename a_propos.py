#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 17:30:19 2020

@author: lemarie
"""

from tkinter import Tk, Label

def about():
    about_window=Tk()
    about_window.title("A propos de notre jeux")
    txt_lbl=Label(about_window, text="A propos:\n\nQu'est ce qu'il est cool ce jeux !\n\nJ'ai envie d'y jouer toute la night")
    txt_lbl.pack(padx=100,pady=100)
    about_window.mainloop()
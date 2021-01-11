#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 15:48:34 2021

@author: lemarie
"""

from tkinter import Tk, Canvas, Button, PhotoImage, Frame, Menu, Label
from a_propos import about
from game import game


def accueil(MaFenetre,width,height):
    """MENU PRINCIPAL"""
    Frame_accueil = Frame(MaFenetre,relief='groove',bg='grey')
    titre = Label(Frame_accueil,bg='grey',font="Verdana 10",text='Bienvenue sur Space invader')
    titre.pack(padx=100,pady=20)
    #Création d'un bouton Quitter
    BoutonQuitter = Button(Frame_accueil,width=10,height=1,text='Quitter',command=MaFenetre.destroy)
    BoutonQuitter.pack(pady=20)
    #Création d'un bouton Start
    BoutonStart = Button(Frame_accueil,width=10,height=1,text ='Lancer le jeux',command=lambda:game(MaFenetre,Frame_accueil,width,height))
    BoutonStart.pack(pady=20)
    #ajout de la frame sur la fenêtre
    Frame_accueil.pack()
    
    #Création d'un menu
    mainmenu = Menu(Frame_accueil)
    menu = Menu(mainmenu,tearoff=0)
    mainmenu.add_cascade(label = 'Menu', menu = menu)
    menu.add_command(label='A propos', command = about)
    menu.add_command(label='Quitter', command = MaFenetre.destroy)
    
    MaFenetre.config(menu = mainmenu)
    MaFenetre.mainloop()
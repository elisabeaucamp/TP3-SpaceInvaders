#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 15:48:34 2021

@author: lemarie
"""

from tkinter import Tk, Canvas, Button, PhotoImage, Frame, Menu, Label
from a_propos import about
from alien import alien
from vaisseau import cVaisseau
from ilots import cIlot


def accueil(MaFenetre,width,height):
    
    """MENU PRINCIPAL"""
    Frame_accueil = Frame(MaFenetre,relief='groove',bg='grey')
    titre = Label(Frame_accueil,bg='grey',font="Verdana 10",text='Bienvenue sur Space invader')
    titre.pack(padx=100,pady=20)
    #Création d'un bouton Quitter
    BoutonQuitter = Button(Frame_accueil,width=10,text='Quitter',command=MaFenetre.destroy)
    BoutonQuitter.pack(pady=20)
    #Création d'un bouton Start
    BoutonStart = Button(Frame_accueil,width=10,text ='Lancer le jeux',command=lambda:game(MaFenetre,Frame_accueil,width,height))
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


def game(MaFenetre,Frame_accueil,width,height):
    Frame_accueil.destroy()
    """LANCEMENT DU JEUX"""
    # creation d'un widget Frame dans la fenetre principale
    Frame1 = Frame(MaFenetre,relief='groove', bg = 'grey')
    Frame1.pack(side='left',padx=10,pady=10)
    
    # creation d'un widget Frame dans la fenetre principale
    Frame2 = Frame(MaFenetre,relief='groove', bg ='pink')
    Frame2.pack(side='left',padx=10,pady=10)
    
    BoutonQuitter = Button(Frame2,width=10,text='Quitter',command=lambda:quitter(MaFenetre,Frame1,Frame2,width,height))
    BoutonQuitter.pack()
    
    #Image de fond du jeux
    photo = PhotoImage(file='Images/Terre.gif')
    #Création d'un widget canvas
    Canevas=Canvas(Frame1,height=height,width=width)
    Canevas.photo = photo #on conserve la photo de l'image
    Canevas.create_image(-130,620,anchor='sw',image=photo)
    Canevas.focus_set()
    unVaisseau=cVaisseau(Canevas=Canevas,width=width)
    
    #Génération des aliens
    """
    On génère une grille d'alien de alien_ligne x alien_colonne
    Puis on enregistre ces coordonnées dans un tableau que l'on passer à l'objet ennemie
    """
    alien_ligne=4
    alien_colonne=8
    alien_array=[]
    #génération du tableau
    for i in range(alien_ligne):
        for j in range(alien_colonne):
            y=int(300/alien_ligne)*i+20
            x=int(500/alien_colonne)*j+100
            alien_array.append([x,y])
    
    #génération des objets alien sur le canvas
    ennemies=alien(alien_array,canvas=Canevas,window=MaFenetre)
    ennemies.move(20,10)
    #génération des ilots et du vaisseau
    unIlot = cIlot(Canevas = Canevas)
    unVaisseau.init2(alien_array,unIlot)
    
    #bind des touches pour le vaisseau
    Canevas.bind('<Left>',unVaisseau.deplacer)
    Canevas.bind('<Right>',unVaisseau.deplacer)
    Canevas.bind('<space>',unVaisseau.tir)
    Canevas.pack()
    
def quitter(MaFenetre,Frame1,Frame2,width,height):
    Frame1.destroy()
    Frame2.destroy()
    accueil(MaFenetre,width,height)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 16:27:42 2021

@author: lemarie
"""

from tkinter import Tk, Canvas, Button, PhotoImage, Frame, Menu

class alien:
    def __init__(self,alien_array,canvas,window):
        self.alien_array = alien_array
        self.canvas=canvas
        self.window=window
        
        dim=20
        for i in range(len(self.alien_array)):
            self.canvas.create_rectangle(self.alien_array[i][0],self.alien_array[i][1],self.alien_array[i][0]+dim,self.alien_array[i][1]+dim, fill = 'red')
            
    def move():
        


width = 800
height = 500
dim = 20

MaFenetre = Tk()
MaFenetre.title("Space Invaders")

#génération du tableau de coordonnée des alien :

alien_ligne=4
alien_colonne=8
alien_array=[]

for i in range(alien_ligne):
    for j in range(alien_colonne):
        y=int(300/alien_ligne)*i+20
        x=int(500/alien_colonne)*j+100
        alien_array.append([x,y])

print(alien_array)

Frame1 = Frame(MaFenetre,relief='groove', bg = 'grey')
Frame1.pack(side='left',padx=10,pady=10)

# creation d'un widget Frame dans la fenetre principale
Frame2 = Frame(MaFenetre,relief='groove', bg ='pink')
Frame2.pack(side='left',padx=10,pady=10)

#Création d'un widget canvas
Canevas = Canvas(Frame1, height = height, width = width)
Canevas.focus_set()
Canevas.pack()

ennemies = alien(alien_array=alien_array,canvas=Canevas,window=MaFenetre)
enemies.move()

#Création d'un bouton Quitter
BoutonQuitter = Button(Frame2, text = 'Quitter', command = MaFenetre.destroy)
BoutonQuitter.pack(anchor = 'nw', padx = 10, pady = 10)

#Création d'un bouton Start
BoutonStart = Button(Frame2, text = 'Start')
BoutonStart.pack(anchor = 'sw', padx = 10, pady = 10)

#Création d'un menu
mainmenu = Menu(Frame1)
menu = Menu(mainmenu,tearoff = 0)
mainmenu.add_cascade(label = 'Menu', menu = menu)
menu.add_command(label='A propos', command = about)
menu.add_command(label='Quitter', command = menu.destroy)


MaFenetre.config(menu = mainmenu)
MaFenetre.mainloop()
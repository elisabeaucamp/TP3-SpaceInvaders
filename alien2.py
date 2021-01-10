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
        self.dim=20
        self.tour=0

        for i in range(len(self.alien_array)):
            rect=self.canvas.create_rectangle(self.alien_array[i][0],self.alien_array[i][1],self.alien_array[i][0]+self.dim,self.alien_array[i][1]+self.dim, fill = 'red')
            self.alien_array[i].append(rect)
        
    def move(self,dX,dY):
        
        if self.alien_array[len(alien_array)-1][0]+self.dim > int(self.canvas.cget('width'))-10:
            dX=-dX
            self.tour+=1
        
        if self.alien_array[0][0] < 10:
            dX=-dX
            self.tour+=1
        
        for i in range(len(self.alien_array)):
            self.alien_array[i][0]+=dX
            if self.tour==2:
                self.alien_array[i][1]+=dY
            
            self.canvas.coords(self.alien_array[i][2],self.alien_array[i][0],self.alien_array[i][1],self.alien_array[i][0]+self.dim,self.alien_array[i][1]+self.dim)

        if self.tour==2:
            self.tour=0

        self.window.after(50,lambda:self.move(dX,dY))

width = 800
height = 500

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
ennemies.move(10,20)

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
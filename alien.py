#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Auteur : Mathurin LEMARIE
#Date : 14/12/2020
#Reste à faire : déplacement verticale de l'alien,redéfinir "fen" et "can"

"""
Objet alien : 
Atribut : 
    - fen_pos_x : la position en abscisse de l'alien
    - fen_pos_y : la position en ordonnée de l'alien
Les arguments entrées pour créer l'alien sont la ligne et la colonne
On part du principe que dans le jeux, les alien peuvent se positionner dans une grille
de 4 ligne par 8 colonne
la fonction move permet de déplacer l'objet sur le canvas
"""

#from tkinter import Tk,Canvas
from data import data


width,height,dim,dX = data()

class alien:
    def __init__(self,line,column,canvas,window):
        global height,width,dim
        #calcule des coordonnées en fonction de la hauteur et de la largeur du canvas
        self.fen_pos_x=(width*column/8)-dim
        self.fen_pos_y=((height/2*line)/4)-dim
        self.canvas=canvas
        self.window=window
        
        #création du rectangle que l'on enregistre dans l'attribu rect_alien
        self.rect_alien=self.canvas.create_rectangle(self.fen_pos_x,self.fen_pos_y,self.fen_pos_x+dim,self.fen_pos_y+dim,fill='red')
    
    def move(self,dX):
        global height,width,dim
        
        if self.fen_pos_x+dim>width:
            dX=-dX
        
        if self.fen_pos_x<dim:
            dX=-dX
        
        self.fen_pos_x=self.fen_pos_x+dX
        self.canvas.coords(self.rect_alien,self.fen_pos_x,self.fen_pos_y,self.fen_pos_x+dim,self.fen_pos_y+dim)
        self.window.after(40,lambda:self.move(dX))


"""
#Programme de test de l'objet
fen = Tk()

width=700
height=500
dim=20
dX=5

can = Canvas(fen, width=width, height=height, bg='white')

alien_1=alien(line=2,column=1)
alien_1.move(dX)

can.pack()
fen.mainloop()
"""
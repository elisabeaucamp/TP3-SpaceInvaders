#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Auteur : Mathurin LEMARIE
#Date : 04/01/2021
#Reste à faire : détection du projectile

"""
Objet alien : 
Atribut : 
    - column : numéro de la colonne
    - fen_pos_x : la position en abscisse de l'alien
    - fen_pos_y : la position en ordonnée de l'alien
    - canvas : canevas dans lequel se trouve l'objet l'objet
    - window : fenetre dans lequel se trouve l'objet
    - width : largeur du canvas
    - height : hauteur du canvas
    - dim : dimension des alien
Les arguments entrées pour créer l'alien sont la ligne et la colonne
Les arguments canvas,window,width,height et dim permettent de connaitre la dimension de la grille ainsi
que l'adresse de la grille et de la fenetre
On part du principe que dans le jeux, les alien peuvent se positionner dans une grille
de 4 ligne par 8 colonne
la fonction move permet de déplacer l'objet sur le canvas
"""

#from tkinter import Tk,Canvas


class alien:
    def __init__(self,line,column,canvas,window,width,height,dim):
        #calcule des coordonnées en fonction de la hauteur et de la largeur du canvas
        self.line=line
        self.fen_pos_x=(width*column/8)-dim
        self.fen_pos_y=((height/2*line)/4)-dim
        self.canvas=canvas
        self.window=window
        self.width=width
        self.height=height
        self.dim=dim
        
        #création du rectangle que l'on enregistre dans l'attribu rect_alien
        self.rect_alien=self.canvas.create_rectangle(self.fen_pos_x,self.fen_pos_y,self.fen_pos_x+dim,self.fen_pos_y+dim,fill='red')
    
    def move_down(self,dX,dY):
        
        #déscente du vaisseau jusqu'à la ligne suivante
        if self.fen_pos_y < ((self.height/2*self.line)/4)-self.dim:
            self.fen_pos_y+=dY
        else: #rappelle de la fonction de mouvement droite/gauche après la fin de la descente
            self.move(dX,dY,0)
            return #arrête l'execution de la fonction
        
        self.canvas.coords(self.rect_alien,self.fen_pos_x,self.fen_pos_y,self.fen_pos_x+self.dim,self.fen_pos_y+self.dim)
        self.window.after(40,lambda:self.move_down(dX,dY))
    
    def move(self,dX,dY,tour):
        
        if self.fen_pos_x+self.dim>self.width:
            dX=-dX
            tour+=1
        
        if self.fen_pos_x+dX<0:
            dX=-dX
            tour+=1
        
        #vérification qu'un allé-retour à déjà été fait ou non
        if tour==2:
            self.line+=1
            self.move_down(dX,dY)
            tour=0
            return #arrête l'exécution de la fonction
        
        self.fen_pos_x+=dX
        self.canvas.coords(self.rect_alien,self.fen_pos_x,self.fen_pos_y,self.fen_pos_x+self.dim,self.fen_pos_y+self.dim)
        self.window.after(40,lambda:self.move(dX,dY,tour))


"""
#Programme de test de l'objet
fen = Tk()

width=700
height=500
dim=20
dX=5

can = Canvas(fen, width=width, height=height, bg='white')

alien_1=alien(line=2,column=1,canvas=can,window=fen)
alien_1.move(dX)

can.pack()
fen.mainloop()
"""
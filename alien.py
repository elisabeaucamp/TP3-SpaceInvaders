#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Auteur : Mathurin LEMARIE
#Date : 04/01/2021
#Reste à faire : détection du projectile

"""
Objet alien : 
Atributs :
    - column : numéro de la colonne
    - fen_pos_x : la position en abscisse de l'alien
    - fen_pos_y : la position en ordonnée de l'alien
    - canvas : canevas dans lequel se trouve l'objet l'objet
    - window : fenetre dans lequel se trouve l'objet
    - width : largeur du canvas
    - height : hauteur du canvas
    - dim : dimension des alien
    - vaisseau : vaisseau du joueur
Les arguments entrées pour créer l'alien sont la ligne et la colonne
Les arguments canvas,window,width,height et dim permettent de connaitre la dimension de la grille ainsi
que l'adresse de la grille et de la fenetre
On part du principe que dans le jeux, les alien peuvent se positionner dans une grille
de 4 ligne par 8 colonne
la fonction move permet de déplacer l'objet sur le canvas
"""

#from tkinter import Tk,Canvas
#from endgame import end_game

class alien:
    def __init__(self,line,column,canvas,window,width,height,dim,vaisseau):
        #calcule des coordonnées en fonction de la hauteur et de la largeur du canvas
        self.line=line
        self.fen_pos_x=(width*column/8)-dim
        self.fen_pos_y=(((3*height)/5*line)/4)-dim
        self.canvas=canvas
        self.window=window
        self.width=width
        self.height=height
        self.dim=dim
        self.vaisseau=vaisseau
        
        #création du rectangle que l'on enregistre dans l'attribue rect_alien
        self.rect_alien=self.canvas.create_rectangle(self.fen_pos_x,self.fen_pos_y,self.fen_pos_x+dim,self.fen_pos_y+dim,fill='red')
    
    def move_down(self,dX,dY,new_pos_y):
        
        #déscente du vaisseau jusqu'à la ligne suivante
        if self.fen_pos_y < new_pos_y:
            self.fen_pos_y+=dY
        else: #rappelle de la fonction de mouvement droite/gauche après la fin de la descente
            self.move(dX,dY,0)
            return #arrête l'execution de la fonction
        
        self.canvas.coords(self.rect_alien,self.fen_pos_x,self.fen_pos_y,self.fen_pos_x+self.dim,self.fen_pos_y+self.dim)
        self.window.after(40,lambda:self.move_down(dX,dY,new_pos_y))
    
    def move(self,dX,dY,tour):
        if self.fen_pos_x+self.dim>self.width:
            dX=-dX
            tour+=1
        
        if self.fen_pos_x+dX<0:
            dX=-dX
            tour+=1
        
        #print(self.vaisseau.canvas.coords(self.vaisseau.rect_vaisseau))
        
        #vérification qu'un allé-retour à déjà été fait ou non
        if tour==2:
            new_pos_y = self.fen_pos_y+self.dim*2
            self.move_down(dX,dY,new_pos_y)
            tour=0
            return #arrête l'exécution de la fonction
        
        if self.fen_pos_x+self.dim > self.vaisseau.canvas.coords(self.vaisseau.rect_vaisseau)[0] and self.fen_pos_x < self.vaisseau.canvas.coords(self.vaisseau.rect_vaisseau)[2] and self.fen_pos_y+self.dim > self.vaisseau.canvas.coords(self.vaisseau.rect_vaisseau)[1] and self.fen_pos_y < self.vaisseau.canvas.coords(self.vaisseau.rect_vaisseau)[3]:
            end_game(self.window,self.canvas)
            return #arrête l'exécution de la fonction
        
        self.fen_pos_x+=dX
        self.canvas.coords(self.rect_alien,self.fen_pos_x,self.fen_pos_y,self.fen_pos_x+self.dim,self.fen_pos_y+self.dim)
        self.window.after(40,lambda:self.move(dX,dY,tour))
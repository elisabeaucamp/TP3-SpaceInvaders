'''auteur : Elisa
Date : 4 janvier
To do : faire communiquer les fichiers'''

from tkinter import Tk, Canvas, Button, PhotoImage, Frame, Menu

class cVaisseau :
    def __init__(self):
        self.MaFenetre_pos_x = 400
        self.MaFenetre_pos_y = 490
        self.rect_vaisseau = Canevas.create_rectangle(self.MaFenetre_pos_x - 45, self.MaFenetre_pos_y - 10, self.MaFenetre_pos_x + 45, self.MaFenetre_pos_y + 10, fill = 'red')

    def deplacer (self, event):
        touche = event.keysym
        print(touche)
        #Allez à droite...
        if touche == "Right":
            #...si on n'est pas deja trop à droite
            if self.MaFenetre_pos_x < width - 55 :
                self.MaFenetre_pos_x += 10
            #...si on l'est trop
            else :
                self.MaFenetre_pos_x += 0
        #Allez à gauche...
        if touche == "Left":
            #...si on n'est pas déjà trop à gauche
            if self.MaFenetre_pos_x > 55 :
                self.MaFenetre_pos_x -= 10
            #...si on l'est trop
            else : 
                self.MaFenetre_pos_x -= 0
        Canevas.coords(self.rect_vaisseau, self.MaFenetre_pos_x - 45, self.MaFenetre_pos_y - 10, self.MaFenetre_pos_x + 40, self.MaFenetre_pos_y + 10)

    def getPosX(self) :
        return int(self.MaFenetre_pos_x)

    def getPosY(self) :
        return int(self.MaFenetre_pos_y)

    def tir(self,event) :
        touche = event.keysym
        if touche == "space" :
            print('hyper vitesse')
            projectile = cProjectile()
            projectile.move(event)
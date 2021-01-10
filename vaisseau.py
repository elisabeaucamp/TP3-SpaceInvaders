'''auteur : Elisa
Date : 4 janvier
To do : faire communiquer les fichiers tuer les aliens'''

from tkinter import Tk, Canvas, Button, PhotoImage, Frame, Menu
#from alien import alien
from ilots import cIlot

class cVaisseau :
    def __init__(self,Canevas,width):
        self.MaFenetre_pos_x = 400
        self.MaFenetre_pos_y = 490
        self.canvas = Canevas
        self.width = width

        #création du vaisseau
        self.rect_vaisseau = self.canvas.create_rectangle(self.MaFenetre_pos_x - 45, self.MaFenetre_pos_y - 10, self.MaFenetre_pos_x + 45, self.MaFenetre_pos_y + 10, fill = 'red')

    def deplacer (self, event):
        touche = event.keysym
        #Allez à droite...
        if touche == "Right":
            #...si on n'est pas deja trop à droite
            if self.MaFenetre_pos_x < self.width - 55 :
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
        self.canvas.coords(self.rect_vaisseau, self.MaFenetre_pos_x - 45, self.MaFenetre_pos_y - 10, self.MaFenetre_pos_x + 40, self.MaFenetre_pos_y + 10)

    def getPosX(self) :
        return int(self.MaFenetre_pos_x)

    def getPosY(self) :
        return int(self.MaFenetre_pos_y)

    def __str__(self) :
        return "[" + str(self.MaFenetre_pos_x)+"]"

    def tir(self,event) :
        touche = event.keysym
        if touche == "space" :
            projectile = cProjectile(posx = self.MaFenetre_pos_x , posy = self.MaFenetre_pos_y,Canevas = self.canvas)
            projectile.move(event,self.alien,self.ilot)
            #projectile.move(event,self.alien2)
    
    def death(self):
        self.canvas.delete(self.rect_vaisseau)

    def init2(self,alien,ilot):
        self.alien = alien
        self.ilot = ilot

class cProjectile :
    def __init__(self,posx,posy,Canevas) :
        self.MaFenetre_posx = posx
        self.MaFenetre_posy = posy
        self.canvas = Canevas

        #Création projectile
        self.rect_projectile = self.canvas.create_rectangle(self.MaFenetre_posx - 5, self.MaFenetre_posy - 5, self.MaFenetre_posx + 5, self.MaFenetre_posy + 5, fill = 'yellow')

    
    def move (self,event,alien,ilot) :
        self.MaFenetre_posy -= 10
        if self.MaFenetre_posy < 0 :
            self.canvas.delete(self.rect_projectile)
            return

            #self.canvas.delete(self.rect_projectile)
            #self.canvas.delete(ennemi1.rect_alien)
        for i in range(len(alien)):
            if alien[i][0] < self.MaFenetre_posx < alien[i][0]+20 and alien[i][1] < self.MaFenetre_posy < alien[i][1]+20 and alien[i][3]==1:
                self.canvas.delete(alien[i][2])
                alien[i][3]=0
                self.canvas.delete(self.rect_projectile)
                return

        if self.MaFenetre_posy == ilot.posy1 + 30 and ilot.abscisse11 < self.MaFenetre_posx < ilot.abscisse12 :
            print("ilot central touché")
            self.canvas.delete(self.rect_projectile) 
            ilot.change_color1(1)
        
        if self.MaFenetre_posy == ilot.posy2 + 30 and ilot.abscisse21 < self.MaFenetre_posx < ilot.abscisse22 :
            print("ilot gauche touché")
            self.canvas.delete(self.rect_projectile) 
            ilot.change_color1(2)

        if self.MaFenetre_posy == ilot.posy3 + 30 and ilot.abscisse31 < self.MaFenetre_posx < ilot.abscisse32 :
            print("ilot droit touché")
            self.canvas.delete(self.rect_projectile) 
            ilot.change_color1(3)

        self.canvas.coords(self.rect_projectile, self.MaFenetre_posx - 5, self.MaFenetre_posy - 5, self.MaFenetre_posx + 5, self.MaFenetre_posy + 5)
        self.canvas.after(15,lambda:self.move(event,alien,ilot))
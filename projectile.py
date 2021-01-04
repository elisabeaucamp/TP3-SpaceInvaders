'''auteur : Elisa
Date : 4 janvier
To do : infliger des dégats'''

from tkinter import Tk, Canvas, Button, PhotoImage, Frame, Menu

class cProjectile :
    def __init__(self) :
        self.MaFenetre_posx = unVaisseau.MaFenetre_pos_x
        self.MaFenetre_posy = unVaisseau.MaFenetre_pos_y
        self.rect_projectile = Canevas.create_rectangle(self.MaFenetre_posx - 5, self.MaFenetre_posy - 5, self.MaFenetre_posx + 5, self.MaFenetre_posy + 5, fill = 'yellow')
    
    def move (self,event) :
        self.MaFenetre_posy -= 10
        if self.MaFenetre_posy < 0 :
            Canevas.delete(self.rect_projectile)
        Canevas.coords(self.rect_projectile, self.MaFenetre_posx - 5, self.MaFenetre_posy - 5, self.MaFenetre_posx + 5, self.MaFenetre_posy + 5)
        Canevas.after(40,lambda:self.move(event))
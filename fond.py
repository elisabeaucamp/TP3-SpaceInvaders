'''auteur : Elisa
Date : 14 décembre
To do : création du projectile au bon endroit tant qu'on n'a pas appuyé sur espace'''

from tkinter import Tk, Canvas, Button, PhotoImage, Frame, Menu
from a_propos import about

class cVaisseau :
    def __init__(self):
        self.MaFenetre_pos_x = 400
        self.MaFenetre_pos_y = 490
        self.rect_vaisseau = Canevas.create_rectangle(self.MaFenetre_pos_x - 45, self.MaFenetre_pos_y - 10, self.MaFenetre_pos_x + 45, self.MaFenetre_pos_y + 10, fill = 'red')

    def deplacer (self, event):
        touche = event.keysym
        print(touche)
        #Allez à droite...
        if touche == 'd' or touche == "Right":
            #...si on n'est pas deja trop à droite
            if self.MaFenetre_pos_x < width - 55 :
                self.MaFenetre_pos_x += 10
            #...si on l'est trop
            else :
                self.MaFenetre_pos_x += 0
        #Allez à gauche...
        if touche == 'q' or touche == "Left":
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

class cProjectile :
    def __init__(self) :
        self.MaFenetre_posx = 400
        self.MaFenetre_posy = 480
        self.rect_projectile = Canevas.create_rectangle(self.MaFenetre_posx - 5, self.MaFenetre_posy - 5, self.MaFenetre_posx + 5, self.MaFenetre_posy + 5, fill = 'yellow')
    
    def tir (self,event) :
        touche = event.keysym
        if touche == "space" :
            
            self.MaFenetre_posy -= 10
            if self.MaFenetre_posy < 0 :
                Canevas.delete(self.rect_projectile)
        Canevas.coords(self.rect_projectile, self.MaFenetre_posx - 5, self.MaFenetre_posy - 5, self.MaFenetre_posx + 5, self.MaFenetre_posy + 5)
        Canevas.after(40,lambda:self.tir(event))


#Création de la fenêtre principale
MaFenetre = Tk()
MaFenetre.title("Space Invaders")
width = 800
height = 500

#Image de fond
photo = PhotoImage(file = 'Images/Terre.gif')

# creation d'un widget Frame dans la fenetre principale
Frame1 = Frame(MaFenetre,relief='groove', bg = 'yellow')
Frame1.pack(side='left',padx=10,pady=10)

# creation d'un widget Frame dans la fenetre principale
Frame2 = Frame(MaFenetre,relief='groove', bg ='pink')
Frame2.pack(side='left',padx=10,pady=10)

#Création d'un widget canvas
Canevas = Canvas(Frame1, height = height, width = width)
item = Canevas.create_image(0,0, anchor = 'sw', image = photo)
print('Image de fond(item', item,")")
Canevas.focus_set()
unVaisseau = cVaisseau()
Canevas.bind('<Key>', unVaisseau.deplacer)
unProjectile = cProjectile()
Canevas.bind('<Key>', unProjectile.tir)
Canevas.pack()

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
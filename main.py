'''auteur : Elisa
Date : 14 décembre
To do : création du projectile au bon endroit tant qu'on n'a pas appuyé sur espace'''

from tkinter import Tk, Canvas, Button, PhotoImage, Frame, Menu
from a_propos import about
from alien import alien
from vaisseau import cVaisseau
from ilots import cIlot

#Création de la fenêtre principale
MaFenetre = Tk()
MaFenetre.title("Space Invaders")
width = 800
height = 500

#Image de fond
photo = PhotoImage(file = 'Images/Terre.gif')

# creation d'un widget Frame dans la fenetre principale
Frame1 = Frame(MaFenetre,relief='groove', bg = 'grey')
Frame1.pack(side='left',padx=10,pady=10)

# creation d'un widget Frame dans la fenetre principale
Frame2 = Frame(MaFenetre,relief='groove', bg ='pink')
Frame2.pack(side='left',padx=10,pady=10)

#Création d'un widget canvas
Canevas = Canvas(Frame1, height = height, width = width)
item = Canevas.create_image(0,0, anchor = 'sw', image = photo)
print('Image de fond(item', item,")")
Canevas.focus_set()
unVaisseau = cVaisseau(Canevas=Canevas,width=width)

#Génération des aliens
"""
On génère une grille d'alien de alien_ligne x alien_colonne
Puis on enregistre ces coordonnées dans un tableau que l'on passer à l'objet ennemie
"""
alien_ligne=4
alien_colonne=8
alien_array=[]

for i in range(alien_ligne):
    for j in range(alien_colonne):
        y=int(300/alien_ligne)*i+20
        x=int(500/alien_colonne)*j+100
        alien_array.append([x,y])

ennemies=alien(alien_array,canvas=Canevas,window=MaFenetre)
ennemies.move(20,10)

unIlot = cIlot(Canevas = Canevas)

unVaisseau.init2(alien_array,unIlot)

Canevas.bind('<Left>',unVaisseau.deplacer)
Canevas.bind('<Right>',unVaisseau.deplacer)
Canevas.bind('<space>',unVaisseau.tir)
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
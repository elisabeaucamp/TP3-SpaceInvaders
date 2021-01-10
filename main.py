'''auteur : Elisa
Date : 14 décembre
To do : création du projectile au bon endroit tant qu'on n'a pas appuyé sur espace'''

from tkinter import Tk, Canvas, Button, PhotoImage, Frame, Menu
from a_propos import about
from alien import alien
from vaisseau import cVaisseau

#Création de la fenêtre principale
MaFenetre = Tk()
MaFenetre.title("Space Invaders")
width = 800
height = 500
dim = 20
dX = 10
dY = 10

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

alien_1=alien(line=6,column=4,canvas=Canevas,window=MaFenetre,width=width,height=height,dim=dim,vaisseau=unVaisseau)
alien_1.move(dX,dY,0)
unVaisseau.init2(alien_1)

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
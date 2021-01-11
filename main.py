"""
Auteur : Elisa
Date : 11 Janvier 2021

=========================
Programme principale, permet le lancement de la fenêtre du jeux

=========================
To do : 
    - Ajout d'un game over
    - Ajout d'un start
    - Affichage d'un score
"""

from tkinter import Tk, Canvas, Button, PhotoImage, Frame, Menu
from a_propos import about
from alien import alien
from vaisseau import cVaisseau
from ilots import cIlot
from accueil import accueil

#Création de la fenêtre principale
MaFenetre = Tk()
MaFenetre.title("Space Invaders")
width = 800
height = 500

accueil(MaFenetre)


"""LANCEMENT DU JEUX"""
# creation d'un widget Frame dans la fenetre principale
Frame1 = Frame(MaFenetre,relief='groove', bg = 'grey')
Frame1.pack(side='left',padx=10,pady=10)

# creation d'un widget Frame dans la fenetre principale
Frame2 = Frame(MaFenetre,relief='groove', bg ='pink')
Frame2.pack(side='left',padx=10,pady=10)

#Image de fond
photo = PhotoImage(file = 'Images/Terre.gif')
#Création d'un widget canvas
Canevas = Canvas(Frame1, height = height, width = width)
Canevas.create_image(-140,600, anchor = 'sw', image=photo)
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
#génération du tableau
for i in range(alien_ligne):
    for j in range(alien_colonne):
        y=int(300/alien_ligne)*i+20
        x=int(500/alien_colonne)*j+100
        alien_array.append([x,y])

#génération des objets alien sur le canvas
ennemies=alien(alien_array,canvas=Canevas,window=MaFenetre)
ennemies.move(20,10)
#génération des ilots et du vaisseau
unIlot = cIlot(Canevas = Canevas)
unVaisseau.init2(alien_array,unIlot)

#bind des touches pour le vaisseau
Canevas.bind('<Left>',unVaisseau.deplacer)
Canevas.bind('<Right>',unVaisseau.deplacer)
Canevas.bind('<space>',unVaisseau.tir)
Canevas.pack()
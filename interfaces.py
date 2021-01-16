"""
Auteur : Mathurin LEMARIE
Date : 11/01/2021

=========================
Description : ensemble des fonction permettant de changer l'interface de la fenêtre
Fonctions : 
    - acceuil : affiche la fenêtre d'accueil dans laquelle se trouve : 
        - Un bouton de lancement du jeux (dans Frame_accueil)
        - Un bouton pour quitter le programme (dans Frame_accueil)
        - Un menu dans lequel il y a un bouton pour quitter et 
          un bouton 'a propos' affichant une fenêtre
        - Entrée : MaFenetre : adresse de la fenêtre dans laquelle se trouve l'interface
        - Cette fonction ne retourne aucunes sorties.
    
    - game : fenêtre du jeux dans laquelle se trouve :
        - L'interface du jeux (Frame1)
        - Un bouton quitter le jeux et retourner à l'accueil (Frame2)
        - Un bouton de lancement du jeux (Frame2)
        - Un menu avec 'quitter' et 'à propos'
        - Entrées :
            - MaFenetre : adresse de la fenêtre de l'interface
            - Frame_accueil : adresse de la frame dans lauqelle se trouvait l'interface d'accueil
              permet de la supprimer au début de cette fonction
            - height,width : respectivement hauteur et largeur du canvas du jeux
        - Cette fonction ne retourne aucunes sorties.
    
    - quitter : fonction permettant de retourner à la page d'accueil
        - Entrées : 
            - MaFenetre : adresse de la fenêtre de l'interface
            - Frame1,Frame2 : respectivement la frame de l'interface du jeux et la frame dans lauqelle
              se trouve le bouton quitter pendant le jeux
            - height,width : respectivement hauteur et largeur du canvas du jeux
            - Canevas : adresse du canvas du jeux
        - Cette fonction ne retourne aucunes sorties.

    - start : fonction permettant de générer les ennemies, le vaisseau et les ilots, ce qui lance la partie : 
        - Entrée :
            - Canevas : adresse du canvas dans lequel on à l'interface du jeux
            - MaFenetre : adresse de la fenêtre du jeux, utile pour certains objets
            - width : largeur du canvas du jeux, utile pour l'objet vaisseau

=========================
To do : faire la fonction game_over()
"""

from tkinter import Canvas, Button, PhotoImage, Frame, Menu, Label, StringVar
from a_propos import about
from generation import generation
from vaisseau import cVaisseau
from alien import alien


def accueil(MaFenetre):
    
    #Largeur et hauteur de la fenêtre de jeux    
    width = 800
    height = 500
    
    """MENU PRINCIPAL"""
    Frame_accueil = Frame(MaFenetre,relief='groove',bg='grey')
    titre = Label(Frame_accueil,bg='grey',font="Verdana 10",text='Bienvenue sur Space invader')
    titre.pack(padx=100,pady=20)
    #Création d'un bouton Quitter
    BoutonQuitter = Button(Frame_accueil,width=10,text='Quitter',command=MaFenetre.destroy)
    BoutonQuitter.pack(pady=20)
    #Création d'un bouton Start
    BoutonStart = Button(Frame_accueil,width=10,text ='Nouvelle partie',command=lambda:game(MaFenetre,Frame_accueil,width,height))
    BoutonStart.pack(pady=20)
    #ajout de la frame sur la fenêtre
    Frame_accueil.pack()
    
    #Création d'un menu
    mainmenu = Menu(Frame_accueil)
    menu = Menu(mainmenu,tearoff=0)
    mainmenu.add_cascade(label = 'Menu', menu = menu)
    menu.add_command(label='A propos', command = about)
    menu.add_command(label='Quitter', command = MaFenetre.destroy)
    
    MaFenetre.config(menu = mainmenu)
    MaFenetre.mainloop()


def game(MaFenetre,Frame_accueil,width,height):


    # creation d'un widget Frame dans la fenetre principale
    Frame1 = Frame(MaFenetre,relief='groove', bg = 'grey')
    Frame1.pack(side='left',padx=10,pady=10)
    #Image de fond du jeux
    photo = PhotoImage(file='Images/Terre.gif')
    #Création d'un widget canvas
    Canevas=Canvas(Frame1,height=height,width=width)
    Canevas.photo = photo #on conserve la photo de l'image
    Canevas.create_image(-130,620,anchor='sw',image=photo)
    Canevas.focus_set()
    Canevas.pack()
    

    #Suppression de la frame de la page d'accueil
    Frame_accueil.pack_forget()
    """LANCEMENT DU JEUX"""
    
    
    # creation d'un widget Frame dans la fenetre principale
    Frame2 = Frame(MaFenetre,relief='groove', bg ='pink')
    Frame2.pack(side='left',padx=20,pady=10)
    
    ennemies,unVaisseau,unIlot = generation(Canevas,MaFenetre,width,Frame2)

    BoutonQuitter = Button(Frame2,width=10,text='Quitter',command=lambda:quitter(MaFenetre,Frame1,Frame2,width,height,Canevas,ennemies))
    BoutonQuitter.pack()
    BoutonQuitter = Button(Frame2,width=10,text='Lancer le jeux',command=lambda:start(Canevas,ennemies,unVaisseau,unIlot))
    BoutonQuitter.pack()

def quitter(MaFenetre,Frame1,Frame2,width,height,Canevas,ennemies):
    ennemies.stop()
    Frame1.destroy()
    Frame2.destroy()
    accueil(MaFenetre)

def game_over(canvas):
    canvas.delete("all")
    photo = PhotoImage(file='Images/game_over.gif')
    canvas.photo = photo #on conserve la photo de l'image
    canvas.create_image(-30,10,anchor='nw',image=photo)
    
def start(Canevas,ennemies,unVaisseau,unIlot):
    #Lancement du mouvement des ennemies
    ennemies.move(20,10)
    
    #fonction permettant le lien entre vaisseau <-> alien <-> ilots
    unVaisseau.init2(ennemies.alien_array,unIlot,unVaisseau)
    
    #bind des touches pour le vaisseau
    Canevas.bind('<Left>',unVaisseau.deplacer)
    Canevas.bind('<Right>',unVaisseau.deplacer)
    Canevas.bind('<space>',unVaisseau.tir)
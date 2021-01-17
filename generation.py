"""
Auteur : Mathurin LEMARIE
Date : 11/01/2021

=========================
Fonction de génération des entités du jeux : alien,vaisseau et ilot
Cette fonction prend comme entrées :
    - canvas : l'adresse du canvas dans lequel le jeux se déroule
    - window : l'adresse de la fenêtre du jeux
    - width : largeur de la fenêtre du jeux
Cette fonction retourne en sortie :
    - ennemies : l'adresse de la l'objet alien généré
    - unVaisseau : l'adresse de l'objet vaiseau généré
    - unIlot : l'adresse de l'objet ilot généré
"""

from alien import alien
from vaisseau import cVaisseau
from ilots import cIlot
from game import game

def generation(canvas,window,width,Frame2,lst_vie,Quitter,Start):
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
    
    

    #génération des ilots et du vaisseau
    unVaisseau=cVaisseau(Canevas=canvas,width=width,Frame2 = Frame2,lst_vie = lst_vie)
    unIlot = cIlot(Canevas=canvas)
    #génération de la grille d'alien
    ennemies=alien(alien_array=alien_array,canvas=canvas,window=window,ilot = unIlot)
    
    #génération de la class game
    jeux=game(ennemies=ennemies,btnQuitter=Quitter,btnStart=Start)
    
    return ennemies,unVaisseau,unIlot,jeux
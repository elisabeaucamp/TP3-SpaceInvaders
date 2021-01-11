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

from tkinter import Tk
from accueil import accueil

#Création de la fenêtre principale
MaFenetre = Tk()
MaFenetre.title("Space Invaders")
width = 800
height = 500

accueil(MaFenetre,width,height)
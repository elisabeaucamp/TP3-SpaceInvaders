"""
Auteur : Elisa
Date : 11 Janvier 2021

=========================
Programme principale, permet le lancement du jeux
On génère simplement la fenêtre de jeux, puis on appelle la fonction accueil permettant
d'afficher la fenêtre d'accueil du jeux

=========================
To do : 
    - Ajout d'un game over
    - Ajout d'un start
    - Affichage d'un score
"""

from tkinter import Tk
from interfaces import accueil

#Création de la fenêtre
MaFenetre = Tk()
MaFenetre.title("Space Invaders")

accueil(MaFenetre)
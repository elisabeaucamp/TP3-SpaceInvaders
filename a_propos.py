"""
Auteur : Mathurin LEMARIE
Date : 11/01/2021

=========================
Cette fonction permet d'afficher le contenu la fenêtre 'à propos' lorsque l'on clique sur celle-ci
dans : menu --> à propos

=========================
To do : modification potentiel du texte
"""

from tkinter import Tk, Label

def about():
    about_window=Tk()
    about_window.title("A propos de notre jeux")
    txt_lbl=Label(about_window, text="SPACE INVADER\n\nAuteurs :\n\nElisa BEAUCAMP & Mathurin LEMARIE\n\n2021")
    txt_lbl.pack(padx=100,pady=100)
    about_window.mainloop()
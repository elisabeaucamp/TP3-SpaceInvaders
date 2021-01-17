"""
Auteur : Mathurin LEMARIE

=========================
Class game : classe gérant l'interface au début et à la fin de la partie
Attribues :
    - ennemies : adresse vers la class ennemies.
    - btnQuitter : adresse vers le bouton Quitter de la fenêtre.
    - btnStart : adresse vers le bouton Start de la fenêtre.

Fonction :
    - end : permet de mettre fin à la partie proprement.
      cette fonction permet de stopper les ennmies pour qu'ils ne lancent plus de projectiles
      à la fin de la partie.
      On change aussi le nom du bouton start
    - start : permet de supprimer le bouton "lancer la partie" lorsque la partie se lance.
      On change aussi le nom du bouton quitter

=========================
To do :
"""

class game:
    def __init__(self,ennemies,btnQuitter,btnStart):
        self.ennemies=ennemies
        self.btnQuitter=btnQuitter
        self.btnStart=btnStart
    
    def end(self):
        self.ennemies.stop()
        self.btnStart.config(text="Nouvelle partie")
        self.btnStart.pack()
    
    def start(self):
        self.btnQuitter.config(text="Quitter la partie")
        self.btnStart.pack_forget()
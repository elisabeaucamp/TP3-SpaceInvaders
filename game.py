"""
Auteur : Mathurin LEMARIE

=========================
Class game : classe gérant l'interface au début et à la fin de la partie
Attribues :
    - ennemies : adresse vers la class ennemies.
    - btnQuitter : adresse vers le bouton Quitter de la fenêtre.
    - btnStart : adresse vers le bouton Start de la fenêtre.
    - Frame1 : adresse la frame principal dans lequel on retrouve le canvas
    - Frame2 : adresse de la frame d'information dans lauqelle on retrouve le score, les vies etc...

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
    def __init__(self,ennemies,window,btnQuitter,btnStart,Frame1,Frame2):
        self.ennemies=ennemies
        self.window=window
        self.btnQuitter=btnQuitter
        self.btnStart=btnStart
        self.Frame1=Frame1
        self.Frame2=Frame2
    
    def end(self):
        from interfaces import restart
        self.ennemies.stop()
        self.btnQuitter.configure(text="revenir à l'accueil",command=lambda:restart(self.window,self.Frame1,self.Frame2))
        self.btnQuitter
    
    def start(self):
        self.btnQuitter.config(text="Quitter la partie")
        self.btnStart.pack_forget()
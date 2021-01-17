"""
Auteur : Mathurin LEMARIE

=========================
Class game :
    

=========================
To do :
"""

class game:
    def __init__(self,ennemies,vaisseau,canvas,window,btnQuitter,btnStart):
        self.ennemies=ennemies
        self.vaisseau=vaisseau
        self.canvas=canvas
        self.window=window
        self.btnQuitter=btnQuitter
        self.btnStart=btnStart
    
    def end(self):
        self.ennemies.stop()
        self.btnStart.pack()
    
    def start(self):
        self.btnStart.pack_forget()
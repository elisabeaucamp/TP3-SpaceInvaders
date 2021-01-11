"""
Auteur : Mathurin LEMARIE
Date : 11/01/2021

=========================
Objet alien :
Permet de créer la grille d'alien ennemie
Attribues : 
    - alien_array : tableau contenant la liste des alien et leurs attribues propres.
      pour chaque slot :
        - indice 0 et 1 : coordonnées respectivement x et y des aliens
        - indice 2 : adresse de l'objet rectangle dans le canvas
        - indice 3 : indique l'état de l'alien dans le jeux : 1 si en vie, 0 si mort
    - canvas : canvas dans lequel on génère les aliens
    - window : fenêtre dans laquelle on génère le canvas    
Fonction : 
    - move : fait bouger toute les 3 secondes les alien de dX sur le côté et de dY vers le bas

=========================
To do : détection d'un game over
"""

#from tkinter import Tk, Canvas, Button, PhotoImage, Frame, Menu

class alien:
    def __init__(self,alien_array,canvas,window):
        self.alien_array = alien_array
        self.canvas=canvas
        self.window=window
        self.dim=20
        self.tour=0
        
        #Boucle permettant d'enregistrer l'adresse de l'objet rectangle et l'état de l'alien (mort ou vivant)
        for i in range(len(self.alien_array)):
            rect=self.canvas.create_rectangle(self.alien_array[i][0],self.alien_array[i][1],self.alien_array[i][0]+self.dim,self.alien_array[i][1]+self.dim, fill = 'red')
            #on ajoute un tag 'ennemie' à tous les alie : utile pour les colisions
            self.canvas.addtag_closest('ennemie',self.alien_array[i][0],self.alien_array[i][1])
            self.alien_array[i].append(rect)
            self.alien_array[i].append(1)

    def move(self,dX,dY):
        #Fonction permettant de faire bouger l'alien
        
        #détection de la bordure droite du canvas
        if self.alien_array[len(self.alien_array)-1][0]+self.dim > int(self.canvas.cget('width'))-10:
            dX=-dX
            self.tour+=1
        
        #détection de la bordure gauche du canvas
        if self.alien_array[0][0] < 10:
            dX=-dX
            self.tour+=1
        
        #mise à jour des coordonées x et y de chaque alien
        for i in range(len(self.alien_array)):
            self.alien_array[i][0]+=dX
            if self.tour==2:
                #"si un allé retour à été fait..."
                self.alien_array[i][1]+=dY
            
            self.canvas.coords(self.alien_array[i][2],self.alien_array[i][0],self.alien_array[i][1],self.alien_array[i][0]+self.dim,self.alien_array[i][1]+self.dim)

        #remise à 9 du compteur d'allé retour
        if self.tour==2:
            self.tour=0

        #rebouclage de la fonction toutes les 3 secondes
        self.window.after(3000,lambda:self.move(dX,dY))
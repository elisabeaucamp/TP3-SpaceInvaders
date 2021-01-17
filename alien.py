"""
Auteur : Mathurin LEMARIE
Date : 11/01/2021

=========================
Class alien :
Permet de créer la grille d'alien ennemie et les projectiles qu'ils lancent.

Attribues : 
    - alien_array : tableau contenant la liste des alien et leurs attribues propres.
      pour chaque slot :
        - indice 0 et 1 : coordonnées respectivement x et y des aliens.
        - indice 2 : adresse de l'objet rectangle dans le canvas.
        - indice 3 : indique l'état de l'alien dans le jeux : 1 si en vie, 0 si mort.
    - canvas : canvas dans lequel on génère les aliens.
    - window : fenêtre dans laquelle on génère le canvas.
    - dim : dimension du rectangle de l'alien.
    - tour : variable s'incrémentant de 1 des que les alien on touché le bord.
      Si tour=2, alors cela veut dire que la grille d'alien a fait un allé retour.
      On fait alors descendre cette grille de quelque pixel vers le bas.
    - after_id_alien : id de la méthode after dans la fonction move() de la class alien. Cela permet d'arrêter ce after dans la fonction stop().
    - ilot : adresse de l'objet ilot permettant de gérer la colision avec les projectiles des alien
    - jeux : adresse de la class jeux permettant de faire les modifications nécessaires à la fin d'une partie

Fonctions : 
    - move : fait bouger toute les 3 secondes les alien de dX sur le côté et de dY vers le bas.
    - stop : cette fonction permet d'arrêter la fonction move() pour arrêter le déplacement des alien.
    - init2 : permet de définir l'attribue 'jeux' : adresse de l'objet jeux permettant de mettre fin au jeux

Class projectile_alien :
    - Attribues : 
        - alien_array,canvas,window : même attribues que la class alien.
        - dim_proj : dimension du rectangle projectile.
        - dim_alien : on récupère la dimension des rectangles des aliens.
        - coord_x,coord_y : coordonnées x et y du projectile.
        - after_id_proj : id de la méthode after dans la fonction move() de la class projectile. Cela permet de stoper le after dans la fonction stop().

Fonctions :
    - move : permet de faire bouger le projectile vers le bas, et détecte une colision avec un ilot ou le vaisseau.
    - stop : même chose que pour la fonction stop de la class alien.

=========================
To do : ajout images alien
"""

import random
from tkinter import PhotoImage
from ilots import cIlot
from vaisseau import cVaisseau

class alien:
    def __init__(self,alien_array,canvas,window,ilot):
        self.alien_array = alien_array
        self.canvas=canvas
        self.window=window
        self.dim=20
        self.tour=0
        self.ilot = ilot
        self.after_id_alien=-1
        
        #Boucle permettant d'enregistrer l'adresse de l'objet rectangle et l'état de l'alien (mort ou vivant)
        for i in range(len(self.alien_array)):
            rect=self.canvas.create_rectangle(self.alien_array[i][0],self.alien_array[i][1],self.alien_array[i][0]+self.dim,self.alien_array[i][1]+self.dim, fill = 'red')
            #img_alien=PhotoImage(file='Images/alien.png')
            #rect=self.canvas.create_image(self.alien_array[i][0],self.alien_array[i][1],image=img_alien)
            #on ajoute un tag 'ennemie' à tous les alie : utile pour les colisions
            self.canvas.addtag_closest('ennemie',self.alien_array[i][0],self.alien_array[i][1])
            self.alien_array[i].append(rect)
            self.alien_array[i].append(1)

    def move(self,dX,dY,ilot,vaisseau):
        #Fonction permettant de faire bouger l'alien
        
        #Rebouclage de la fonction toutes les 2.5 secondes. Le after est appliqué au début pour pouvoir récupérer son ID actuel.
        self.after_id_alien = self.window.after(2500,lambda:self.move(dX,dY,ilot,vaisseau))
        
        #détection des bords pour appliquer un changement de direction
        for i in range(len(self.alien_array)):
            #détection de la bordure droite
            if self.alien_array[i][0]+self.dim > int(self.canvas.cget('width'))-10 and self.alien_array[i][3] == 1:
                dX=-dX
                self.tour+=1
                break
            
            #détection de la bordure gauche
            if self.alien_array[i][0] < 10 and self.alien_array[i][3] == 1:
                dX=-dX
                self.tour+=1
                break
        
        victoire=0
        #mise à jour des coordonées x et y de chaque alien
        for i in range(len(self.alien_array)):
            victoire += self.alien_array[i][3] #permet la détection de la victoire
            self.alien_array[i][0]+=dX
            if self.tour==2:
                #"si un allé retour à été fait..."
                self.alien_array[i][1]+=dY
                
            if self.alien_array[i][1]+self.dim > 370:
                from interfaces import game_over
                game_over(self.canvas,self.jeux)
                return #on arrêtre l'exécution de la fonction
            
            self.canvas.coords(self.alien_array[i][2],self.alien_array[i][0],self.alien_array[i][1],self.alien_array[i][0]+self.dim,self.alien_array[i][1]+self.dim)
        
        
        #détection d'une victoires
        if victoire==0: #si la somme == 0 : alors il n'y a plus d'alien en vie
            from interfaces import win
            win(self.canvas,self.jeux)
            print(victoire)

        #remise à 0 du compteur d'allé retour
        if self.tour==2:
            self.tour=0
        
        #Les alien on 1 chance sur 2 de tirer.
        shot = random.uniform(1,2)
        if shot > 1:
            #génération d'un projectile dans le cas ou on à tirer un chiffre au dessus de 1
            projectile_alien(alien_array=self.alien_array,canvas=self.canvas,window=self.window,alien_dim=self.dim,ilot=ilot,vaisseau = vaisseau,jeux=self.jeux)
        
    def stop(self):
        self.window.after_cancel(self.after_id_alien)
    
    def init2(self,jeux):
        #ajout de l'attribue jeux à la class alien
        self.jeux=jeux

class projectile_alien:
    def __init__(self,alien_array,canvas,window,alien_dim,ilot,vaisseau,jeux):
        self.alien_array=alien_array
        self.canvas=canvas
        self.window=window
        self.alien_dim=alien_dim
        self.ilot = ilot
        self.vaisseau = vaisseau
        self.proj_dim=10 #dimension du projectile
        self.jeux=jeux
        
        alien_live=[]
        #on récupère la liste de tous les alien en vie
        for i in range(len(self.alien_array)):
            if self.alien_array[i][3]==1:
                alien_live.append([self.alien_array[i][0],self.alien_array[i][1]])
        
        #on prend un alien aléatoire parmis tous les alien en vie
        alien_ind = random.randint(0,len(alien_live)-1)
        self.coord_x=alien_live[alien_ind][0] #on récupère la coordonnée X de l'alien pris au hasard
        self.coord_y=alien_live[alien_ind][1] #on récupère la coordonnée Y de l'alien pris au hasard
        
        #Génération du projectile sur le canvas
        self.proj_rect = self.canvas.create_rectangle(self.coord_x+self.alien_dim/2,self.coord_y+self.alien_dim/2,self.coord_x+self.proj_dim,self.coord_y+self.proj_dim,fill='blue')
        self.move(10,ilot,vaisseau) 
        
    def move(self,dY,ilot,vaisseau):
        self.coord_y += dY
        
        #détection du projectile lorsqu'il sort de la fenêtre du canvas
        if self.coord_x > self.canvas.winfo_height():
            self.canvas.delete(self.proj_rect)
            return
        
        #vérification d'une colision avec un item sur le canvas
        colision = list(self.canvas.find_overlapping(self.coord_x+self.alien_dim/2,self.coord_y+self.alien_dim/2,self.coord_x+self.proj_dim,self.coord_y+self.proj_dim))
        #récupération des items avec un tag 'ilot'
        ilotag = self.canvas.find_withtag('ilot')
        #récupération de l'item vaisseau
        vaisseautag = self.canvas.find_withtag('vaisseau')

        if colision :
            for i in range(len(colision)):
                #colision avec un ilot
                if colision[i] in list(ilotag) :
                    self.canvas.delete(self.proj_rect)
                    if ilot.returncolor(colision[i]) == 'blue' : #si l'ilot est bleu il change de couleur
                        ilot.change_color1(colision[i])
                    elif ilot.returncolor(colision[i]) == 'purple' : #deuxième changement de couleur
                        ilot.change_color2(colision[i])
                    elif ilot.returncolor(colision[i]) == 'black' :#au 3e coup l'ilot se détruit
                        self.canvas.delete(colision[i])
                    return
                #colision avec le vaisseau
                if colision[i] in list(vaisseautag):
                    self.canvas.delete(self.proj_rect)
                    self.vaisseau.liste_vie.append(1)
                    vaisseau.set_vie(self.vaisseau.liste_vie)
                    print(len(self.vaisseau.liste_vie))
                    if len(self.vaisseau.liste_vie) == 3 :
                        from interfaces import game_over
                        game_over(self.canvas,self.jeux)
                        return
                    return


        self.canvas.coords(self.proj_rect,self.coord_x,self.coord_y,self.coord_x+self.proj_dim,self.coord_y+self.proj_dim)
        self.after_id_proj = self.window.after(20,lambda:self.move(dY,ilot,vaisseau)) #on récupère l'id de la méthode after pour pouvoir l'utiliser dans le stop
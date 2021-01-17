"""
Auteur : Elisa
Date : 11 janvier 2021

=========================
cVaisseau : 
objet du vaisseau permettant le déplacement et le tire du vaisseau
Attribus :
    - Mafenetre_pos_x : position x du vaisseau
    - Mafenetre_pos_y : position y du vaisseau
    - canvas : canvas dans lequel se trouve le vaisseau
    - width : largeur de la fenêtre
    - rect_vaisseau : objet rectangle du vaisseau
Fonctions :
    - deplacer : permet de déplacer à gauche ou à droite le vaisseau en fonction respectivement
      des flèches de gauche ou de droite
    - getPosX : permet de récupérer la coordonnée x du vaisseau
    - getPosY : permet de récupérer la coordonnée y du vaisseau
    - tir : permet de générer un projectile lors de la pression de la bar espace
    - death : supprime le vaisseau et lance le 'game over'
    - init2 : permet de récupérer les coordonnées des aliens et des ilots

=========================
cProjectile :
objet projectile se déplaceant vers le haut de la fenêtre.
Attribus :
    - MaFenetre_pos_x : position x du projectile
    - MaFenetre_pos_y : position y du projectile
    - canvas : canvas dans lequel se trouve le projectile
    - rect_projectile : objet rectangle du projectile
Fonction :
    - move : permet de bouger le projectile vers le haut
      la fonction détecte aussi une colision avec un alien ou un ilot

=========================
To do : détecter une victoire potentielle
"""

from ilots import cIlot
from tkinter import StringVar, Label, PhotoImage

class cVaisseau :
    def __init__(self,Canevas,width,Frame2,lst_vie):
        self.MaFenetre_pos_x = 400
        self.MaFenetre_pos_y = 490
        self.canvas = Canevas
        self.width = width
        self.score = StringVar()
        self.score.set('score : 0')
        self.label_score = Label(Frame2,pady=10,bg='pink',font="Verdana 10",textvariable= self.score)
        self.label_score.pack()
        self.vie = StringVar()
        self.vie.set('Vies : 3')
        self.label_vie = Label(Frame2,pady=10,bg='pink',font="Verdana 10",textvariable= self.vie)
        self.label_vie.pack()
        self.liste_vie = lst_vie

        #création du vaisseau
        self.img_vaisseau = PhotoImage(file='Images/vaisseau_dimensionne.png')
        self.rect_vaisseau = self.canvas.create_image(self.MaFenetre_pos_x,self.MaFenetre_pos_y, image = self.img_vaisseau)
        #l'image ne devrait pas avoir de fond car l'image téléchargée est un png transparent mais le fond blanc apparaît automatiquement

        #création tag
        self.canvas.addtag_closest('vaisseau',self.MaFenetre_pos_x,self.MaFenetre_pos_y)

    def deplacer (self, event):
        touche = event.keysym
        #Allez à droite...
        if touche == "Right":
            #...si on n'est pas deja trop à droite
            if self.MaFenetre_pos_x < self.width - 55 :
                self.MaFenetre_pos_x += 10
            #...si on l'est trop
            else :
                self.MaFenetre_pos_x += 0
        #Allez à gauche...
        if touche == "Left":
            #...si on n'est pas déjà trop à gauche
            if self.MaFenetre_pos_x > 55 :
                self.MaFenetre_pos_x -= 10
            #...si on l'est trop
            else : 
                self.MaFenetre_pos_x -= 0
        self.canvas.coords(self.rect_vaisseau, self.MaFenetre_pos_x, self.MaFenetre_pos_y)

    def tir(self,event) : #tir du vaisseau
        touche = event.keysym
        if touche == "space" : #appui barre espace
            #on crée un objet de la classe projectile
            projectile = cProjectile(posx = self.MaFenetre_pos_x , posy = self.MaFenetre_pos_y,Canevas = self.canvas,rect_vaisseau=self.rect_vaisseau)
            #on le fait bouger
            projectile.move(event,self.alien,self.ilot,self.vaisseau)

    #récuperer le vaisseau l'alien et l'ilot meme s'ils sont créé après l'objet vaisseau dans le PP
    def init2(self,alien,ilot,vaisseau): 
        self.alien = alien
        self.ilot = ilot
        self.vaisseau = vaisseau

    #calcul du score
    def set_score(self,liste_alien):
        score = 0
        for k,l in enumerate (liste_alien) : #on parcoure la liste des aliens
            length = len(l)
            nbr_alien = liste_alien[k][length-1] #c'est une liste de liste
            if nbr_alien == 0 : #pour chaque sous-liste, si le dernier chiffre est 0 c'est que l'alien est mort
                score += 10 #à chaque 0, c'est un alien mort, donc on prend 10 points
        self.score.set('Score : ' + str(score))

    def set_vie(self,lst_vie) :
        vie_depart = 3 #nb vie au lancement du jeu
        vie_actuelle = vie_depart - len(lst_vie) #lst_vie se remplit à chaque coup reçu
        print(vie_actuelle)
        self.vie.set('Vies : ' + str(vie_actuelle)) #mise à jour label




class cProjectile :
    def __init__(self,posx,posy,Canevas,rect_vaisseau) :
        self.MaFenetre_posx = posx
        self.MaFenetre_posy = posy
        self.canvas = Canevas
        self.rect_vaisseau = rect_vaisseau
        self.width = 800

        #Création projectile
        self.rect_projectile = self.canvas.create_rectangle(self.MaFenetre_posx - 5, self.MaFenetre_posy - 5, self.MaFenetre_posx + 5, self.MaFenetre_posy + 5, fill = 'yellow')

    def move (self,event,alien,ilot,vaisseau) :
        self.MaFenetre_posy -= 10
        
        #détection de la bordure supérieur du canvas
        if self.MaFenetre_posy < 0 :
            self.canvas.delete(self.rect_projectile)
            return #on arrête l'exécution de la fonction car le projectile n'existe plus

        #vérification d'une colision avec un item sur le canvas
        colision = list(self.canvas.find_overlapping(self.MaFenetre_posx-5,self.MaFenetre_posy-5,self.MaFenetre_posx+5,self.MaFenetre_posy+5))
        #récupération des item avec un tag 'ennemie'
        ennemie = self.canvas.find_withtag('ennemie')
        #récupération des items avec un tag 'ilot'
        ilotag = self.canvas.find_withtag('ilot')

        if colision: #on vérifie que la liste n'est pas vide
            for i in range(len(colision)):
                if colision[i] in list(ennemie): #on vérifie que l'item en colision a bien le tag 'ennemie'
                    for j in range(len(alien)):
                        if colision[i] == alien[j][2] and alien[j][3]==1: #permet de trouver quelle ligne du tableau correspond à l'ennemie touché
                            #supression de l'ennemie sur le canvas et passage à l'état mort dans le tableau d'ennemies
                            self.canvas.delete(colision[i])
                            alien[j][3]=0
                            #suppression du projectile
                            self.canvas.delete(self.rect_projectile)
                            vaisseau.set_score(alien)
                            return #on arrête l'exécution de la fonction move
                
                if colision[i] in list(ilotag) : #on vérifie que le projectile est en colision avec un ilot
                    self.canvas.delete(self.rect_projectile)
                    if ilot.returncolor(colision[i]) == 'blue' : #si l'ilot est bleu il change de couleur
                        ilot.change_color1(colision[i])
                    elif ilot.returncolor(colision[i]) == 'purple' : #deuxième changement de couleur
                        ilot.change_color2(colision[i])
                    elif ilot.returncolor(colision[i]) == 'black' :#au 3e coup l'ilot se détruit
                        self.canvas.delete(colision[i])
                    return
                

        self.canvas.coords(self.rect_projectile, self.MaFenetre_posx - 5, self.MaFenetre_posy - 5, self.MaFenetre_posx + 5, self.MaFenetre_posy + 5)
        self.canvas.after(15,lambda:self.move(event,alien,ilot,vaisseau))
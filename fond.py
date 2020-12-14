'''auteur : Elisa
Date : 14 décembre
To do : fond du jeu'''

from tkinter import Tk, Canvas, Button, PhotoImage, Frame, Menu
from a_propos import about

class vaisseau :
    def __init__(self,line, column):
        global height
        self.MaFenetre_pos_x = width - (width - 10)
        self.MaFenetre_pos_y = height - 10
        self.rect_vaisseau = Canevas.create_rectangle(self.MaFenetre_pos_x, self.MaFenetre_pos_y, self.MaFenetre_pos_x + 90, self.MaFenetre_pos_y - 20, fill = 'red')

    def deplacer (self, event):
        touche = event.keysym
        dX =  + 20
        dY = 10 + 20
        print(touche)
        if touche == 'z':
            self.MaFenetre_pos_y -= dY
        if touche == 's':
            self.MaFenetre_pos_y += dY
        if touche == 'd':
            self.MaFenetre_pos_x += dX
        if touche == 'q':
            self.MaFenetre_pos_x -= dX

        Canevas.coords(self.rect_vaisseau, self.MaFenetre_pos_x - (dX/2), self.MaFenetre_pos_y - (dX/2),  self.MaFenetre_pos_x + (dX/2), self.MaFenetre_pos_y + (dX/2))

    '''def projectile (self, event) :
        touche = event.keysym
        print(touche)
        if touche == 'space' :
            '''
            


#Création de la fenêtre principale
MaFenetre = Tk()
MaFenetre.title("Space Invaders")
width = 800
height = 500
dim = 20


#Image de fond
#photo = PhotoImage(file = 'Images/Terre.gif')

# creation d'un widget Frame dans la fenetre principale
Frame1 = Frame(MaFenetre,relief='groove', bg = 'yellow')
Frame1.pack(side='left',padx=10,pady=10)

# creation d'un widget Frame dans la fenetre principale
Frame2 = Frame(MaFenetre,relief='groove', bg ='pink')
Frame2.pack(side='left',padx=10,pady=10)

#Création d'un widget canvas
Canevas = Canvas(Frame1, height = height, width = width, bg = 'black')
#tem = Canevas.create_image(0,0, anchor = 'sw', image = photo)
#print('Image de fond(item', item,")")
Canevas.focus_set()
vaisseau = vaisseau(line = height, column = 1)
Canevas.bind('<Key>', vaisseau.deplacer)
Canevas.pack()

#Création d'un bouton Quitter
BoutonQuitter = Button(Frame2, text = 'Quitter', command = MaFenetre.destroy)
BoutonQuitter.pack(anchor = 'nw', padx = 10, pady = 10)

#Création d'un bouton Start
BoutonStart = Button(Frame2, text = 'Start')
BoutonStart.pack(anchor = 'sw', padx = 10, pady = 10)

#Création d'un menu
mainmenu = Menu(Frame1)
menu = Menu(mainmenu,tearoff = 0)
mainmenu.add_cascade(label = 'Menu', menu = menu)
menu.add_command(label='A propos', command = about)
menu.add_command(label='Quitter', command = menu.destroy)


MaFenetre.config(menu = mainmenu)
MaFenetre.mainloop()
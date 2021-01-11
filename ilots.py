'''auteur : Elisa
Date : 10 janvier
To do : création des ilots'''

from tkinter import Tk, Canvas, Button, PhotoImage, Frame, Menu

class cIlot :
    def __init__(self,Canevas) :
        self.posx1 = 400
        self.posy1 = 400
        self.posx2 = 200
        self.posy2 = 400
        self.posx3 = 600
        self.posy3 = 400
        self.canvas = Canevas

        #creation ilots
        self.rect_ilot1 = self.canvas.create_rectangle(self.posx1 - 30, self.posy1 - 30, self.posx1 + 30, self.posy1 + 30, fill = 'blue')
        self.rect_ilot2 = self.canvas.create_rectangle(self.posx2 - 30, self.posy2 - 30, self.posx2 + 30, self.posy2 + 30, fill = 'blue')
        self.rect_ilot3 = self.canvas.create_rectangle(self.posx3 - 30, self.posy3 - 30, self.posx3 + 30, self.posy3 + 30, fill = 'blue')

        #creation abscisses
        self.abscisse11 = self.posx1 - 30
        self.abscisse12 = self.posx1 + 30
        self.abscisse21 = self.posx2 - 30
        self.abscisse22 = self.posx2 + 30
        self.abscisse31 = self.posx3 - 30
        self.abscisse32 = self.posx3 + 30

    #change la couleur de l'ilot de blue à purple
    def change_color1(self,numilot) :
        if numilot == 1 :
            self.canvas.itemconfig(self.rect_ilot1, fill = 'purple')
        if numilot == 2 :
            self.canvas.itemconfig(self.rect_ilot2, fill = 'purple')
        if numilot == 3 :
            self.canvas.itemconfig(self.rect_ilot3, fill = 'purple')

    #change la couleur de l'ilot de purple à black
    def change_color2(self,numilot) :
        if numilot == 1 :
            self.canvas.itemconfig(self.rect_ilot1, fill = 'black')
        if numilot == 2 :
            self.canvas.itemconfig(self.rect_ilot2, fill = 'black')
        if numilot == 3 :
            self.canvas.itemconfig(self.rect_ilot3, fill = 'black')

    #retourne la couleur actuelle de l'ilot
    def returncolor(self,numilot) :
        if numilot == 1 :
            color = self.canvas.itemcget(self.rect_ilot1, "fill")
        if numilot == 2 :
            color = self.canvas.itemcget(self.rect_ilot2, "fill")
        if numilot == 3 :
            color = self.canvas.itemcget(self.rect_ilot3, "fill")
        return color
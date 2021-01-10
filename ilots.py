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
        self.rect_ilot1 = self.canvas.create_rectangle(self.posx1 - 30, self.posy1 - 30, self.posx1 + 30, self.posy1 + 30, fill = 'grey')
        self.rect_ilot2 = self.canvas.create_rectangle(self.posx2 - 30, self.posy2 - 30, self.posx2 + 30, self.posy2 + 30, fill = 'grey')
        self.rect_ilot3 = self.canvas.create_rectangle(self.posx3 - 30, self.posy3 - 30, self.posx3 + 30, self.posy3 + 30, fill = 'grey')

        #creation abscisses
        self.abscisse11 = self.posx1 - 30
        self.abscisse12 = self.posx1 + 30
        self.abscisse21 = self.posx2 - 30
        self.abscisse22 = self.posx2 + 30
        self.abscisse31 = self.posx3 - 30
        self.abscisse32 = self.posx3 + 30

    
    def change_color1(self,numilot) :
        if numilot == 1 :
            self.rect_ilot1 = self.canvas.create_rectangle(self.posx1 - 30, self.posy1 - 30, self.posx1 + 30, self.posy1 + 30, fill = 'orange')
        if numilot == 2 :
            self.rect_ilot2 = self.canvas.create_rectangle(self.posx2 - 30, self.posy2 - 30, self.posx2 + 30, self.posy2 + 30, fill = 'orange')
        if numilot == 3 :
            self.rect_ilot1 = self.canvas.create_rectangle(self.posx3 - 30, self.posy3 - 30, self.posx3 + 30, self.posy3 + 30, fill = 'orange')

    #def getcolor(self,numilot) :
        #color = self.rect_ilot1.['fill']
#ROLLET Matéo
#mateo.rollet@etu.univ-lyon1.fr
#class joueur
#V0.1

import core
import random

class Joueur:
    def __init__(self):
        self.couleur = [255,255,255]
        self.r = 30
        self.x = random.randint(self.r, core.WINDOW_SIZE[0]-self.r)
        self.y = random.randint(self.r, core.WINDOW_SIZE[1]-self.r)

    def show(self):
        core.Draw.circle(self.couleur,[self.x,self.y],self.r)

    def moov(self):
        if core.getKeyPressList("z"):
            self.y = self.y - 5
        if core.getKeyPressList("s"):
            self.y = self.y + 5
        if core.getKeyPressList("q"):
            self.x = self.x - 5
        if core.getKeyPressList("d"):
            self.x = self.x + 5
        self.edge()
    def edge(self):
        if (self.y+self.r)> core.WINDOW_SIZE[0]:
            self.y=core.WINDOW_SIZE[0]-self.r
        if (self.x+self.r)> core.WINDOW_SIZE[0]:
            self.x=core.WINDOW_SIZE[0]-self.r
        if (self.y-self.r)< 0:
            self.y=self.y+1
        if (self.x-self.r)< 0:
            self.x=self.x+1


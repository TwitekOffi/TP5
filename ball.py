#ROLLET Matéo
#mateo.rollet@etu.univ-lyon1.fr
#class ball
#V0.1
from pygame.math import Vector2

import core
import random


class Ball:
    def __init__(self):
        self.couleur = [random.randint(0,255),random.randint(0,255),random.randint(0,100)]
        self.r = 10
        self.x = random.randint(self.r, core.WINDOW_SIZE[0]-self.r)
        self.y = random.randint(self.r, core.WINDOW_SIZE[1]-self.r)

        self.acceleration = Vector2(0,0)
        self.vel= Vector2(0,0)
        self.maxVel=1

    def show(self):
        core.Draw.circle(self.couleur,[self.x,self.y],self.r)

    def randomMove(self):
        self.acc=[random.uniform(-5,5),random.uniform(-5,5)]
        self.vel= self.vel+self.acc

        if self.vel.length() > self.maxVel:
            self.vel.scale_to_length(self.maxVel)

        self.x=self.x+self.vel.x
        self.y=self.y+self.vel.y
        self.edge()


    def moov(self):
        if core.getKeyPressList("z"):
            self.y = self.y - 1
        if core.getKeyPressList("s"):
            self.y = self.y + 1
        if core.getKeyPressList("q"):
            self.x = self.x - 1
        if core.getKeyPressList("d"):
            self.x = self.x + 1
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

    def collision(self, joueur):
        dist = Vector2(self.x,self.y).distance_to(Vector2(joueur.x,joueur.y))
        sommeRayon = self.r+joueur.r
        if sommeRayon >= dist:
            return True
        else:
            return False


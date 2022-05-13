#ROLLET Matéo
#mateo.rollet@etu.univ-lyon1.fr
#TP5
#V0.1

import core
from ball import Ball
from joueur import Joueur


def setup():
    print("setup")
    core.WINDOW_SIZE=[800,800]
    core.fps = 144
    nbBalles=100

    j = Joueur()
    core.memory("joueur",j)
    core.memory("gameOver",False)
    core.memory("score",0)

    core.memory("TabBalle",[])

    for i in range (0, nbBalles):
        b = Ball()
        core.memory("TabBalle").append(b)






def run():
    print("run")

    if not core.memory("gameOver"):
        core.memory("score", core.memory("score")+1/core.fps)
        core.cleanScreen()
        for i in core.memory("TabBalle"):
            i.show()
            i.randomMove()
            gameOver = i.collision(core.memory("joueur"))
            if gameOver:
                core.memory("gameOver", True)

        core.memory("joueur").show()
        core.memory("joueur").moov()
    else:
        core.Draw.text((255,0,0),"GameOver :"+str(core.memory("score")),[10,10])







if __name__ == '__main__':
    core.main(setup, run)
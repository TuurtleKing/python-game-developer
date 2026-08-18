

import os 
os.environ["SDL_VIDEO_WINDOW_POS"] = "50,50"
import pgzrun
import random
WIDTH=1000
HEIGHT=800
TITLE="Hashira training"
directionY=random.choice([-1,1])
directionX=random.choice([-1,1])

tokito=Actor("tokito")
zenitsu=Actor("zenitsu")
zenitsu.x=random.randint(100,WIDTH-100)
zenitsu.y=random.randint(100,WIDTH-100)
def draw():
    screen.fill("black")  #if you want afterimages remove this
    zenitsu.draw()
    tokito.draw()


def on_key_down(key):
     if key==keys.E:
         tokito.x=tokito.x+100
     if key==keys.  Q:
             tokito.x=tokito.x-100
     if key==keys.X:
             tokito.y=tokito.y+100
     if key==keys.Z:
                 tokito.y=tokito.y-100
    







def update():
    global directionX, directionY
    if keyboard.D:
        tokito.x=tokito.x+3
    elif keyboard.a:
            tokito.x=tokito.x-3
    if keyboard.S:
            tokito.y=tokito.y+3
    elif keyboard.W:
            tokito.y=tokito.y-3
    
    zenitsu.x=zenitsu.x+random.randint(3,5)*directionX
    zenitsu.y=zenitsu.y+random.randint(3,5)*directionY
    if zenitsu.right>WIDTH or zenitsu.left<0:
        directionX=directionX*-1
    if zenitsu.bottom>HEIGHT or zenitsu.top<0:
        directionY=directionY*-1
           



pgzrun.go()
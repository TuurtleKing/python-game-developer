

import os 
os.environ["SDL_VIDEO_WINDOW_POS"] = "50,50"
import pgzrun
import random
WIDTH=600
HEIGHT=500
TITLE="bumblebee and flower"
bumblebee=Actor("bumblebee")
flower=Actor("flower")
flower.x=random.randint(50,WIDTH-50)
flower.y=random.randint(50,WIDTH-50)
def draw():
    screen.blit("backround",(0,0))
    flower.draw()
    bumblebee.draw()

#this only works 1 time when the key is pressed we cannot hold it
# def on_key_down(key):
#     if key==keys.D:
#         bumblebee.x=bumblebee.x+1





def update():
    if keyboard.D:
        bumblebee.x=bumblebee.x+1
    elif keyboard.a:
            bumblebee.x=bumblebee.x-1
    if keyboard.S:
            bumblebee.y=bumblebee.y+1
    elif keyboard.w:
            bumblebee.y=bumblebee.y-1





pgzrun.go()


import os 
os.environ["SDL_VIDEO_WINDOW_POS"] = "50,50"
import pgzrun
import random
WIDTH=600
HEIGHT=500
TITLE="bumblebee and flower"
score=0
gameover=False
bumblebee=Actor("bumblebee")
flower=Actor("flower")
flower.x=random.randint(50,WIDTH-50)
flower.y=random.randint(50,HEIGHT-50)
def draw():
    if not gameover:
        screen.blit("backround",(0,0))
        flower.draw()
        bumblebee.draw()
        screen.draw.text(f"score:{score}",topleft=(20,20),fontsize=20,color="green")
    else:
        screen.fill("black")
        screen.draw.text(f"game over your final score is:{score}",center=(WIDTH/2,HEIGHT/2),fontsize=20,color="green")

#this only works 1 time when the key is pressed we cannot hold it
# def on_key_down(key):
#     if key==keys.D:
#         bumblebee.x=bumblebee.xdd+1

def timer():
     global gameover
     gameover=True



def update():
    global score
    if keyboard.D:
        bumblebee.x=bumblebee.x+1
    elif keyboard.a:
            bumblebee.x=bumblebee.x-1
    if keyboard.S:
            bumblebee.y=bumblebee.y+1
    elif keyboard.W:
            bumblebee.y=bumblebee.y-1

    if bumblebee.colliderect(flower):
        flower.x=random.randint(50,WIDTH-50)
        flower.y=random.randint(50,HEIGHT-50)
        score=score+1




clock.schedule(timer,10)
pgzrun.go()
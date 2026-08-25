
import os 
os.environ["SDL_VIDEO_WINDOW_POS"] = "50,50"
import pgzrun
import random
HEIGHT=600
WIDTH=600
TITLE="satellites game"
timer=0
numberofsat=10
satellites=[]
for i in range(numberofsat):
    sats=Actor("satellite")
    sats.x=random.randint(50,WIDTH-50)
    sats.y=random.randint(50,HEIGHT-50)
    satellites.append(sats)
#print(satellites)

def draw():
    screen.blit("background",(0,0))
    screen.draw.text(str(timer),(10,10))
    number=1
    for sat in satellites:
        sat.draw()
        screen.draw.text (str(number),(sat.x,sat.y+12))
        number=number+1














pgzrun.go()
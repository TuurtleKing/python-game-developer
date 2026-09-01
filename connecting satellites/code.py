
import os 
os.environ["SDL_VIDEO_WINDOW_POS"] = "50,50"
import time
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

lines=[]
currentsat=0
starttime=time.time()


def draw():
    screen.blit("background",(0,0))
    screen.draw.text(str(timer),(10,10))
    number=1
    for sat in satellites:
        sat.draw()
        screen.draw.text (str(number),(sat.x,sat.y+12))
        number=number+1
    for line in lines:
        screen.draw.line(line[0],line[1],"green")
    


def on_mouse_down(pos):
    global currentsat,lines
    if currentsat<numberofsat:
        if satellites[currentsat].collidepoint(pos):
            if currentsat!=0:
                start=satellites[currentsat].pos
                end=satellites[currentsat-1].pos
                lines.append([start,end])
            currentsat=currentsat+1
        else:
            currentsat=0
            lines=[]




def update():
    global timer
    if currentsat<numberofsat:
        currenttime=time.time()
        timer=currenttime-starttime



pgzrun.go()
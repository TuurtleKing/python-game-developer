import os 
os.environ["SDL_VIDEO_WINDOW_POS"] = "50,50"
import time
import pgzrun
import random

HEIGHT=600
WIDTH=600
TITLE="Alphabet Path Game"

timer=0
total_letters=10
letters=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
circler=[]

#Create cirlce actors and place them randomly so it is easyer to use collidpoint
for i in range(total_letters):
    cirlce = Actor("satellite")
    cirlce.x = random.randint(50, WIDTH - 50)
    circle.y = random.randint(50, HEIGHT - 50)
    circler.append(circle)

lines=[]
currentabc=0
starttime=time.time()


def draw():
    screen.blit("background", (0, 0))
    screen.draw.text(str(round(timer, 1)), (10, 10), fontsize=30)
    
    #draw circles and put the abc letters over them
    for i in range(len(circler)):
        circler[i].draw()
        screen.draw.text(letters[i], (circler[i].x - 5, circler[i].y - 10), fontsize=30, color="white")
    
    #draw green lines between connected circles/abc
    for line in lines:
        screen.draw.line(line[0], line[1], "green")


def on_mouse_down(pos):
    global currentabc, lines
    if currentabc < total_letters:
        #check if you clicked the correct circle/abc in order
        if circler[currentabc].collidepoint(pos):
            if currentabc != 0:
                start=circler[currentabc].pos
                end=circler[currentabc - 1].pos
                lines.append([start, end])
            currentsat = currentsat + 1
        else:
            #reset if click the wrong place
            currentabc=0
            lines=[]


def update():
    global timer
    if currentsat<total_letters:
        timer = time.time() - starttime


pgzrun.go()





#this game does not work since i cant find downloadable black whire circles
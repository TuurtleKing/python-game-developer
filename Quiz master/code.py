
import os 
os.environ["SDL_VIDEO_WINDOW_POS"] = "50,50"
import pgzrun
import random 
HEIGHT=600 
WIDTH=600
TITLE="Quiz" 
marqueebox=Rect(0,0,600,50)
questionbox=Rect(15,65,400,150)
timerbox=Rect(430,65,155,150)
allfile=[]
def draw():
    screen.fill("black")
    screen.draw.filled_rect(marqueebox, "grey")
    screen.draw.filled_rect(questionbox, "grey")
    screen.draw.filled_rect(timerbox, "grey")

def readfile():
    file=open("Quiz master/questions.txt","r")
    allfile=file.read().split("\n")
   
    print(allfile)



readfile()












pgzrun.go()
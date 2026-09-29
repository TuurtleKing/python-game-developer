
import os 
os.environ["SDL_VIDEO_WINDOW_POS"] = "50,50"
import pgzrun
import random 

HEIGHT=460
WIDTH=600
TITLE="Quiz"

timeleft=10
current=0
total=0


marqueebox=Rect(0,0,600,50)
questionbox=Rect(15,65,400,150)
timerbox=Rect(430,65,155,150)
optbox1=Rect(15,230,192,100)
optbox2=Rect(222,230,192,100)
optbox3=Rect(15,345,192,100)
optbox4=Rect(222,345,192,100)
optboxs=[optbox1, optbox2, optbox3, optbox4]
skipbox=Rect(430,230,155,215)

allfile=[]

def draw():
    screen.fill("black")
    screen.draw.filled_rect(marqueebox, "grey")
    screen.draw.filled_rect(questionbox, "grey")
    screen.draw.filled_rect(timerbox, "grey")
    screen.draw.filled_rect(skipbox, "grey")
    for box in optboxs:
        screen.draw.filled_rect(box, "grey")

    screen.draw.textbox (str(timeleft),timerbox,color="green",shadow=(0.5,0.5),scolor="black")
    screen.draw.textbox (f"Welcome to Quiz Master. You are at Round {current} out of {total}",timerbox,color="green",shadow=(0.5,0.5),scolor="black")

def readfile():
    global total
    file=open("Quiz master/questions.txt","r")
    allfile=file.read().split("\n")
    file.close()
    total=len(allfile)
    
    print(allfile)



readfile()












pgzrun.go()
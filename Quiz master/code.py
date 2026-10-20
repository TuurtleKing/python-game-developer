
import os 
os.environ["SDL_VIDEO_WINDOW_POS"] = "50,50"
import pgzrun
import random 
#460
HEIGHT=510
WIDTH=600
TITLE="Quiz"

timeleft=10
current=0
total=0
gameover=False
score=0
result=""

marqueebox=Rect(0,0,600,50)
questionbox=Rect(15,65,400,150)
timerbox=Rect(430,65,155,150)
optbox1=Rect(15,230,192,100)
optbox2=Rect(222,230,192,100)
optbox3=Rect(15,345,192,100)
optbox4=Rect(222,345,192,100)
optboxs=[optbox1, optbox2, optbox3, optbox4]
skipbox=Rect(430,230,155,215)
correctbox=Rect(0,465,600,50)

allfile=[]
onequestion=""

def draw():
    screen.fill("black")
    if not gameover:
        screen.draw.filled_rect(marqueebox, "grey")
        screen.draw.filled_rect(questionbox, "grey")
        screen.draw.filled_rect(timerbox, "grey")
        screen.draw.filled_rect(skipbox, "grey")
        screen.draw.filled_rect(correctbox, "grey")
        for box in optboxs:
            screen.draw.filled_rect(box, "grey")

        screen.draw.textbox (str(timeleft),timerbox,color="green",shadow=(0.5,0.5),scolor="black")
        screen.draw.textbox (f"Welcome to Quiz Master. You are at Round {current} out of {total}",marqueebox,color="green",shadow=(0.5,0.5),scolor="black")

        screen.draw.textbox (onequestion[0].strip(),questionbox)
        screen.draw.textbox (onequestion[1].strip(),optbox1)
        screen.draw.textbox (onequestion[2].strip(),optbox2)
        screen.draw.textbox (onequestion[3].strip(),optbox3)
        screen.draw.textbox (onequestion[4].strip(),optbox4)

        screen.draw.textbox ("SKIP",skipbox,angle=90)

        screen.draw.textbox (result, correctbox)
    else:
        
        screen.draw.text (f"Gameover you scored {score} out of {total}",center=(WIDTH/2,HEIGHT/2))

def readfile():
    global total, allfile
    file=open("Quiz master/questions.txt","r")
    allfile=file.read().split("\n")
    file.close()
    total=len(allfile)
    
    print(allfile)

def readnext():
    global onequestion, current, gameover, timeleft
    if len(allfile)>0:
        onequestion=allfile.pop(0).split("|")
        current=current+1
        timeleft=10
    else:
        gameover=True

def on_mouse_down(pos):
    global score, result
    if skipbox.collidepoint(pos):
        readnext()

    for optbox in optboxs:
        if optbox.collidepoint(pos):
            if optboxs.index(optbox)==int(onequestion[5])-1:
                score=score+1
                result="correct"
            else:
                result="incorrect"
            readnext()
            
def timer():
    global timeleft
    if timeleft >0:
        timeleft=timeleft-1
    else:
        readnext()


readfile()
readnext()

def update():
    marqueebox.x=marqueebox.x-4
    if marqueebox.right<0:
        marqueebox.left=WIDTH







clock.schedule_interval(timer,1)

pgzrun.go()
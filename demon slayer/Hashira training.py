

import os 
os.environ["SDL_VIDEO_WINDOW_POS"] = "50,50"
import pgzrun
import random
WIDTH=800
HEIGHT=600
TITLE="Hashira training"
score=0
gameover=False
directionY=random.choice([-1,1])
directionX=random.choice([-1,1])

tokito=Actor("tokito")
zenitsu=Actor("zenitsu")
zenitsu.x=random.randint(100,WIDTH-100)
zenitsu.y=random.randint(100,HEIGHT-100)
def draw():
    if not gameover:
        screen.fill("black")  #if you want afterimages remove this
        zenitsu.draw()
        tokito.draw()
        screen.draw.text(f"score:{score}",topleft=(20,20),fontsize=20,color="green")
    else:
        screen.fill("black")
        screen.draw.text(f"game over your final score is:{score}",center=(WIDTH/2,HEIGHT/2),fontsize=20,color="green")

    

def timer():
    global gameover,screen2
    gameover=True  
    screen2=True
    #def draw():
          #screen.blit("muichiro",(0,0))


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
    global directionX, directionY, score
    if not gameover:
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
            
        if tokito.colliderect(zenitsu):
                zenitsu.x=random.randint(50,WIDTH-50)
                zenitsu.y=random.randint(50,HEIGHT-50)
                score=score+1

clock.schedule(timer,60)
pgzrun.go()
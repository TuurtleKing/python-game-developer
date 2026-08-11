import pgzrun 
import random
HEIGHT= 600
WIDTH= 700
TITLE = "Triangle"
#new idea using varibles since 
#i figured out the cooditets but couldnt figure out
#the other way
top = (350, 200)      
bottomleft = (200, 500)  
bottomright = (500, 500) 
def draw():
    screen.fill("black")
    R=random.randint(0,255)
    G=random.randint(0,255)
    B=random.randint(0,255)
    #screen.draw.line((200,500),(500,500),"green")
    #screen.draw.line((500,),(500,350),"green")
#line 1
    screen.draw.line(bottomleft, bottomright, (R,G,B))
#line 2
    screen.draw.line(bottomright, top, (R,G,B))
#line 3
    screen.draw.line(top, bottomleft, (R,G,B))

def update():
    pass





pgzrun.go()
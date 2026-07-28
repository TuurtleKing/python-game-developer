import pgzrun
import random
WIDTH = 500
HEIGHT = 500
TITLE = "shapes"
def draw():
    screen.fill("black")
    size=10
    for i in range(100):
        R=random.randint(0,255)
        G=random.randint(0,255)
        B=random.randint(0,255)
        rec=Rect(0,0,size,size)
        rec.center=WIDTH/2,HEIGHT/2
        screen.draw.rect(rec,(R,G,B))
        size=size+5

def update():
    pass
















pgzrun.go()
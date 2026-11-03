import os 
os.environ["SDL_VIDEO_WINDOW_POS"] = "50,50"
import pgzrun

HEIGHT=700
WIDTH=700

r=4
bullets=[]
bees=[]
for i in range(4):
    beerow1=[]
    xrow=30
    yrow=30
    for i in range(r):
        bee=Actor("bee")
        bee.y=yrow
        bee.x=xrow+80*i
        beerow1.append(bee)
    bees.append(beerow1)
    r=r-1
    xrow=xrow+80
    yrow=yrow+80
#print(bees)
ship=Actor("ship")
ship.pos=WIDTH/2,HEIGHT-50


def draw():
    screen.fill("black")

    ship.draw()

    for bullet in bullets:
        bullet.draw()

    for row in bees:
        for bee in row:
            bee.draw()

def on_key_down(key):
    #for machine gun put in update anf change if key to if keyboard.space:a
    if key==keys.SPACE:
            bullet=Actor("bullet")
            bullet.pos=ship.midtop
            bullets.append(bullet)


def update():
    if keyboard.A:
        ship.x=ship.x-4
    if keyboard.D:
        ship.x=ship.x+4

    if ship.x<0:
        ship.x=WIDTH
    if ship.x>WIDTH:
        ship.x=0

    for bullet in bullets:
        bullet.y=bullet.y-8
pgzrun.go()

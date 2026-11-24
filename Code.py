import os 
os.environ["SDL_VIDEO_WINDOW_POS"] = "50,50"
import pgzrun

HEIGHT=700
WIDTH=700

message=""
gameover=False
score=0
direction=1
r=4
bullets=[]
bees=[]
yrow=30
xrow=30
for i in range(4):
    beerow1=[]
    for i in range(r):
        bee=Actor("bee")
        bee.y=yrow
        bee.x=xrow+80*i
        beerow1.append(bee)
    bees.append(beerow1)
    r=r-1
    xrow=xrow+40
    yrow=yrow+70
#print(bees)
ship=Actor("ship")
ship.pos=WIDTH/2,HEIGHT-50


def draw():
    screen.fill("black")
    if not gameover:
        ship.draw()

        for bullet in bullets:
            bullet.draw()

        for row in bees:
            for bee in row:
                bee.draw()
        screen.draw.text(str(score),(WIDTH/2,30))
    else:
        screen.draw.text(message,(WIDTH/2,40))
        screen.draw.text(f"your score is {score}",(WIDTH/2,30))

def on_key_down(key):
    #for machine gun put in update anf change if key to if keyboard.space:
    if key==keys.SPACE:
            bullet=Actor("bullet")
            bullet.pos=ship.midtop
            bullets.append(bullet)


def update():
    global direction, score, gameover, message
    movedown=False
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
    if any(bees):
        for row in bees:
            for bee in row:
                if (direction==1 and bee.x>=WIDTH) or (direction==-1 and bee.x<=0):
                    movedown=True
                    break
        if movedown:
            direction=direction*-1
        for row in bees:
            for bee in row:
                bee.x=bee.x+2*direction
                if movedown:
                    bee.y=bee.y+40

        for row in range(len(bees)):
            for bee in bees[row]:
                for bullet in bullets:
                    if bullet.colliderect(bee):
                        sounds.eep.play()
                        bullets.remove(bullet)
                        bees[row].remove(bee)
                        score=score+1

        for row in bees:
            for bee in row:
                if bee.colliderect(ship):
                    gameover=True 
                    message="you have lost"
        
    else:
        gameover=True 
        message="you have won"
pgzrun.go()

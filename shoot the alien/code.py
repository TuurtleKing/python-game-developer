import pgzrun
import random
WIDTH=700
HEIGHT=600
TITLE="Shoot The Alien"
alien=Actor("alien")
alien.x=random.randint(50,WIDTH-50)
alien.y=random.randint(50,HEIGHT-50)
def draw():
    screen.fill("black")
    screen.draw.text(TITLE,center=(350,30),fontsize=30,color="green")
    alien.draw()



def on_mouse_down(pos):
    if alien.collidepoint(pos):
        alien.x=random.randint(50,WIDTH-50)
        alien.y=random.randint(50,HEIGHT-50)        









pgzrun.go()

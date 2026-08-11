import pgzrun
import random
WIDTH=700
HEIGHT=600
TITLE="Shoot The Alien"
alien=Actor("alien")
alien.x=random.randint(50,WIDTH-50)
alien.y=random.randint(50,HEIGHT-50)
message=""
def draw():
    screen.fill("black")
    screen.draw.text(TITLE,center=(350,30),fontsize=30,color="green")
    alien.draw()
    screen.draw.text(message,center=(350,60),fontsize=25,color="light green")



def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        alien.x=random.randint(50,WIDTH-50)
        alien.y=random.randint(50,HEIGHT-50)     
        message="correct! you hit the alien"
    else:
        message="incorrect! you hit air"









pgzrun.go()

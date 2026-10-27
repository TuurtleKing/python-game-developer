import os 
os.environ["SDL_VIDEO_WINDOW_POS"] = "50,50"
import pgzrun

HEIGHT=700
WIDTH=700

ship=Actor("ship")
ship.pos=WIDTH/2,HEIGHT-50


def draw():
    screen.fill("black")

    ship.draw()





def update():
    if keyboard.A:
        ship.x=ship.x-4
    if keyboard.D:
        ship.x=ship.x+4

    if ship.x<=0:
        ship.x=WIDTH
    if ship.x>=WIDTH:
        ship.x=0
pgzrun.go()

import os 
os.environ["SDL_VIDEO_WINDOW_POS"] = "50,50"
import time
import pgzrun
import random

HEIGHT = 600
WIDTH = 1000
TITLE = "Alphabet Path Game"

timer = 0
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S","T","U", "V", "W", "X", "Y", "Z"]
circles = []  # Renamed for clarity
total_letters = len(letters)

# Create circle actors and place them randomly
for i in range(total_letters):
    circle = Actor("circlee")  # Fixed variable name
    circle.x = random.randint(50, WIDTH - 50)
    circle.y = random.randint(50, HEIGHT - 50)
    circles.append(circle)

lines = []
currentabc = 0
starttime = time.time()


def draw():
   # screen.blit("background", (0, 0))
    screen.fill("black")
    screen.draw.text(str(round(timer, 1)), (10, 10), fontsize=30)
    
    # Draw circles and overlay the letter on each
    for i in range(len(circles)):
        circles[i].draw()
        screen.draw.text(letters[i], (circles[i].x - 5, circles[i].y - 10), fontsize=30, color="white")
    
    # Draw green lines between connected circles
    for line in lines:
        screen.draw.line(line[0], line[1], "green")


def on_mouse_down(pos):
    global currentabc, lines
    if currentabc < total_letters:
        # Check if you clicked the correct letter/circle in sequence
        if circles[currentabc].collidepoint(pos):
            if currentabc != 0:
                start = circles[currentabc].pos
                end = circles[currentabc - 1].pos
                lines.append([start, end])
            currentabc = currentabc + 1  # Fixed variable name
        else:
            # Reset path on wrong click
            currentabc = 0
            lines = []


def update():
    global timer
    if currentabc < total_letters:  # Fixed variable name
        timer = time.time() - starttime


pgzrun.go()

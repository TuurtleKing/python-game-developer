import os
os.environ["SDL_VIDEO_WINDOW_POS"] = "50,50"
import pgzrun
import random

WIDTH = 600
HEIGHT = 600
TITLE = "Pac-Math Quiz"

#game Variables
score = 0
gameover = False
current_q = 0

#player setup (Pac-Man)
player = Actor("pacman")  # Make sure you have a pacman image in your images folder
player.x = WIDTH / 2
player.y = HEIGHT / 2

#quiz questions and answers
#format: [Question Text, Correct Answer, Wrong 1, Wrong 2, Wrong 3]
questions = [
    ["10 - 7", 3, 7, 4, 8],
    ["5 + 6", 11, 10, 12, 9],
    ["4 * 3", 12, 16, 7, 14],
    ["15 / 3", 5, 3, 6, 4],
    ["9 - 4", 5, 6, 13, 3]
]

total_questions = len(questions)

# Answer circles setup
answer_actors = []
answer_values = []

def setup_question():
    global answer_actors, answer_values
    answer_actors = []
    answer_values = []

    if current_q < total_questions:
        #get options for the current question
        opts = [
            questions[current_q][1],
            questions[current_q][2],
            questions[current_q][3],
            questions[current_q][4]
        ]
        #shuffle so the correct answer isn't always in the same place
        random.shuffle(opts)

        #create 4 targets around the screen
        positions = [(100, 150), (500, 150), (100, 450), (500, 450)]
        for i in range(4):
            circle = Actor("circlee")  #reusing your circle actor
            circle.x = positions[i][0]
            circle.y = positions[i][1]
            answer_actors.append(circle)
            answer_values.append(opts[i])




def draw():
    screen.fill("grey")

    if not gameover:
        #draw question banner at the top
        screen.draw.text(f"Question: {questions[current_q][0]}", (20, 20), fontsize=30, color="yellow")
        screen.draw.text(f"Score: {score}", (450, 20), fontsize=30, color="green")

        #draw player
        player.draw()

        #draw answer choices on screen
        for i in range(len(answer_actors)):
            answer_actors[i].draw()
            screen.draw.text(
                str(answer_values[i]),
                center=(answer_actors[i].x, answer_actors[i].y),
                fontsize=28,
                color="white")
           
    else:
        screen.draw.text(
        f"Game Over! Final Score: {score}/{total_questions}",
        center=(WIDTH / 2, HEIGHT / 2),
        fontsize=35,
        color="green")
        


def update():
    global score, current_q, gameover

    if not gameover:
        #player movement using WASD
        if keyboard.d and player.right < WIDTH:
            player.x = player.x + 4
        elif keyboard.a and player.left > 0:
            player.x = player.x - 4

        if keyboard.s and player.bottom < HEIGHT:
            player.y = player.y + 4
        elif keyboard.w and player.top > 0:
            player.y = player.y - 4

        #check collision with answer targets
        for i in range(len(answer_actors)):
            if player.colliderect(answer_actors[i]):
                #check if the collected answer matches the correct answer
                if answer_values[i] == questions[current_q][1]:
                    score = score + 1

                current_q = current_q + 1

                if current_q < total_questions:
                    #reset player to center for next round
                    player.x = WIDTH / 2
                    player.y = HEIGHT / 2
                    setup_question()
                else:
                    gameover = True
                break
setup_question()

pgzrun.go()






#here is a description i prepared so i can explain it easy 
#If the game is running, draw() renders the player, the question text at the top,
#and draws each circle with its answer number written right in the center using
#screen.draw.text()."
#I used continuous keyboard input (keyboard.a, keyboard.d, etc.)
#so Pac-Man moves smoothly when key buttons are held down
#
#


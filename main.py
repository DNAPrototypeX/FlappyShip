# Paul Moore

import pygame
from ship import Ship
from buildings import Buildings
import sys
# Define some colors, you may want to add more
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Flappy ship")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
buildings_list = []
clock = pygame.time.Clock()
player = Ship(screen, buildings_list)
building = Buildings(screen, player)
score = 0
timer = 0
font = pygame.font.SysFont('Calibri', 25, True, False)
f = open("highscore.txt", "r")
high_score = f.read()
high_score_text = font.render("HighScore: " + str(high_score), True, RED)
f.close()



# -------- Main Program Loop -----------
while not done:
    # --- Main event loop

    # --- All events are detected here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.going_down = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                player.going_down = True

    # --- Game logic should go here
    timer += 1
    # --- Screen-clearing code goes here
    #  Here, we clear the screen to white.
    screen.fill(WHITE)

    # --- Drawing code should go here
    if timer == 120:
        buildings_list.append(Buildings(screen, player))
        timer = 0

    for item in buildings_list:
        if not item.update():
            buildings_list.remove(item)
        if item.bottom.x + 50 < 300 and item.inplay:
            score += 1
            if score > int(high_score):
                w = open("highscore.txt", "w")
                w.write(str(score))
                w.close()
            item.inplay = False

    if not player.update():
        for item in buildings_list:
            item.speed = 0
        player.die()
    # replace with if statement to check for collision
    score_text = font.render(str(score), True, RED)
    screen.blit(score_text, [10, 10])
    screen.blit(high_score_text, [450, 10])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.


pygame.quit()

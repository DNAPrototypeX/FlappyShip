# Paul Moore

import pygame
from ship import Ship
from buildings import Buildings
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
building = Buildings(screen)

timer = 0
score = 0
font = pygame.font.SysFont('Calibri', 25, True, False)

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

    score_text = font.render(str(score), True, BLACK)
    screen.blit(score_text, [10, 10])

    # --- Screen-clearing code goes here
    #  Here, we clear the screen to white.
    screen.fill(WHITE)

    # --- Drawing code should go here
    if timer == 120:
        buildings_list.append(Buildings(screen))
        timer = 0

    for item in buildings_list:
        if not item.update():
            buildings_list.remove(item)

    player.buildings = buildings_list

    player.update()
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()

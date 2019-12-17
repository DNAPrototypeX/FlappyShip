# Paul Moore
def Main():
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
    YELLOW = (255, 255, 0)
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
    score = 0
    font = pygame.font.SysFont('Calibri', 25, True, False)
    title_font = pygame.font.SysFont('Calibri', 72, True, False)
    f = open("highscore.txt", "r")
    high_score = f.read()
    high_score_text = font.render("HighScore: " + str(high_score), True, RED)
    f.close()
    background = pygame.image.load('background.jpg').convert()
    background_x = 0
    pygame.mixer.music.load('music.wav')
    pygame.mixer.music.play(-1, 0.0)
    screen.fill(BLACK)
    difficulties = [pygame.Rect(250, 250, 20, 20), pygame.Rect(350, 250, 20, 20), pygame.Rect(450, 250, 20, 20)]
    difficulties_colours = [GREEN, YELLOW, RED]
    difficulties_text = ['Easy', 'Normal', 'Hard']

    def drawText(text, font, surface, x, y, clr):
        textobj = font.render(text, 1, clr)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    def TitleScreen():
        menu_message = 'Select a difficulty!'
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # pressing escape quits
                        sys.exit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for item in difficulties:
                        if item.collidepoint(m_pos[0], m_pos[1]):
                            if item == difficulties[0]:
                                speed = -1.5
                            elif item == difficulties[1]:
                                speed = -2
                            elif item == difficulties[2]:
                                speed = -3
                            return speed
            screen.fill(BLACK)
            m_pos = pygame.mouse.get_pos()
            for item in difficulties:
                if item.collidepoint(m_pos[0], m_pos[1]):
                    item.width = 40
                    item.height = 40
                else:
                    item.width = 20
                    item.height = 20

            menu_message = "Select a difficulty!"
            for i in range(len(difficulties)):
                if difficulties[i].width == 40:
                    pygame.draw.rect(screen, difficulties_colours[i], difficulties[i].move(-10, -10))
                    menu_message = difficulties_text[i]
                    drawText(menu_message, font, screen, 250, 350, YELLOW)
                elif difficulties[i].width == 20:
                    pygame.draw.rect(screen, difficulties_colours[i], difficulties[i])

            drawText(menu_message, font, screen, 250, 350, YELLOW)
            drawText("Flappy Ship!", title_font, screen, 175, 100, YELLOW)
            pygame.display.flip()

    def start():
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # pressing escape quits
                        sys.exit()
                    return

    def respawn():
        screen.fill(BLACK)
        drawText('You Died :(', title_font, screen, 175, 100, RED)
        drawText('Respawn? Y/N', font, screen, 250, 350, YELLOW)
        pygame.display.flip()
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # pressing escape quits
                        sys.exit()
                    if event.key == pygame.K_y:
                        Main()
                    if event.key == pygame.K_n:
                        sys.exit()
                    return

    speed = TitleScreen()
    menu_message = 'Press any key to start!'
    screen.fill(BLACK)
    drawText(menu_message, title_font, screen, 25, 200, YELLOW)
    pygame.display.update()
    start()
    buildings_list.append(Buildings(screen, speed))

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

        # --- Screen-clearing code goes here
        #  Here, we clear the screen to white.
        screen.fill(WHITE)

        # --- Drawing code should go here
        background_x += speed
        if background_x < -1400:
            background_x = 0
        screen.blit(background, [background_x, 0])

        if buildings_list[len(buildings_list) - 1].bottom.x < 550:
            buildings_list.append(Buildings(screen, speed))

        for item in buildings_list:
            if not item.update():
                buildings_list.remove(item)
            elif item.bottom.x + 50 < 300 and item.inplay:
                score += 1
                if score > int(high_score):
                    w = open("highscore.txt", "w")
                    w.write(str(score))
                    w.close()
                item.inplay = False
        print(buildings_list[0].speed)
        if not player.update():
            respawn()
        # replace with if statement to check for collision
        score_text = font.render(str(score), True, RED)
        screen.blit(score_text, [10, 10])
        if score > int(high_score):
            high_score_text = font.render("HighScore: " + str(score), True, RED)
        screen.blit(high_score_text, [450, 10])

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.

    pygame.quit()


Main()

import pygame
import random


class Buildings:
    def __init__(self, screen):
        self.screen = screen
        self.bottom = pygame.Rect(800, random.randrange(125, 425), 50, 500)
        self.top = pygame.Rect(self.bottom.x, self.bottom.y - 500, 50, 375)

    def update(self):
        self.top.x -= 2
        self.bottom.x -= 2
        pygame.draw.rect(self.screen, (0, 0, 0), self.top)
        pygame.draw.rect(self.screen, (0, 0, 0), self.bottom)
        if self.bottom.x < -50:
            return False
        else:
            return True

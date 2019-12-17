import pygame
import random


class Buildings:
    def __init__(self, screen, speed):
        self.screen = screen
        self.bottom = pygame.Rect(800, random.randrange(127, 495), 50, 500)
        self.top = pygame.Rect(self.bottom.x, self.bottom.y - 500, 50, 375)
        self.top_image = pygame.image.load('top_building.png').convert()
        self.bottom_image = pygame.image.load('bottom_building.png').convert()
        self.inplay = True
        self.speed = speed
        self.background_x = 0

    def update(self):
        self.top.x += self.speed
        self.bottom.x += self.speed
        self.screen.blit(self.top_image, self.top)
        self.screen.blit(self.bottom_image, self.bottom)
        if self.bottom.x < -50:
            return False
        return True

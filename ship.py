import pygame
WHITE = (255, 255, 255)
MAGENTA = (255, 0, 255)


class Ship(pygame.sprite.Sprite):
    def __init__(self, screen, buildings):
        super().__init__()
        self.image_moving = pygame.image.load("ship_moving.png").convert()
        self.image_static = pygame.image.load("ship_static.png").convert()
        self.image_moving.set_colorkey(MAGENTA)
        self.image_static.set_colorkey(MAGENTA)
        self.rect = self.image_moving.get_rect()
        self.rect.height -= 20
        self.y_speed = 3
        self.going_down = True
        self.screen = screen
        self.buildings = buildings

    def die(self):
        print("dead")

    def update(self):
        if self.going_down and self.y_speed < 7.6:
            self.y_speed += 0.2
        elif self.y_speed > -7.6:
            self.y_speed -= 0.2
        self.rect.y += self.y_speed

        if self.rect.y > 460:
            self.y_speed = 0
            self.rect.y = 460
        elif self.rect.y < -1:
            self.rect.y = -1

        if not self.going_down:
            self.screen.blit(self.image_moving, [300, self.rect.y])
        else:
            self.screen.blit(self.image_static, [300, self.rect.y])

        for item in self.buildings:
            if self.rect.colliderect(item.bottom) or self.rect.colliderect(item.top):
                return False
        return True


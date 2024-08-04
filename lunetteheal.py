import pygame

class HealthPack(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.game = game
        self.image = pygame.image.load('asset/lunette.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.fall_speed = 0
        self.gravity = 0.5
    
    def update(self):
        self.fall_speed += self.gravity
        self.rect.y += self.fall_speed


        if self.rect.y >= 770 - self.rect.height:
            self.rect.y = 770 - self.rect.height
            self.fall_speed = 0

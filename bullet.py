import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.velocity = 3
        self.player = player
        self.image = pygame.image.load('asset/bullet.png')
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 320
        self.rect.y = player.rect.y + 120
        self.origin_image = self.image
        self.angle = 0
    
    def rotate(self):
        self.angle += 12
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_bullet.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()
        for enemy in self.player.game.check_collision(self, self.player.game.all_enemy):
            self.remove()
            enemy.remove()
        if  self.rect.x > 1200:
            self.player.all_bullet.remove(self)

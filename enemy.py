import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.8
        self.velocity = random.randint(2, 5)
        self.all_bullet = pygame.sprite.Group()
        self.image = pygame.image.load('asset/enemy1.png')
        self.image = pygame.transform.scale(self.image,(300,300))
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 500 + random.randint(0, 300)
        self.hit_time = None

    def remove(self):
        self.game.score += 20
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 500 + random.randint(0, 300)
        self.velocity = random.randint(2, 5)
        self.hit_time = None

    def forward(self):
        if self.rect.x < -300:
            self.game.score -= 20
            self.remove()
        if not self.game.check_collision(self, self.game.all_player):
            self.rect.x -= self.velocity
        else:
            if self.hit_time is None:
                self.hit_time = pygame.time.get_ticks()
            elif pygame.time.get_ticks() - self.hit_time > 500:
                self.remove()
            self.game.player.damage(self.attack)

class Enemy1(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.8
        self.velocity = random.randint(2, 5)
        self.all_bullet = pygame.sprite.Group()
        self.image = pygame.image.load('asset/enemy2.png')
        self.image = pygame.transform.scale(self.image,(300,300))
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 500 + random.randint(0, 300)
        self.hit_time = None

    def remove(self):
        self.game.score += 20
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 500 + random.randint(0, 300)
        self.velocity = random.randint(2, 5)
        self.hit_time = None

    def forward(self):
        if self.rect.x < -300:
            self.game.score -= 20
            self.remove()
        if not self.game.check_collision(self, self.game.all_player):
            self.rect.x -= self.velocity
        else:
            if self.hit_time is None:
                self.hit_time = pygame.time.get_ticks()
            elif pygame.time.get_ticks() - self.hit_time > 500:
                self.remove()
            self.game.player.damage(self.attack)


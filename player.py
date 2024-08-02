import pygame
from bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 2
        self.all_bullet = pygame.sprite.Group()
        self.image = pygame.image.load('asset/player1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 500
        self.last_shot_time = 0

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            self.game.game_over()

    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 150, self.rect.y + 75, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 150, self.rect.y + 75, self.health, 5])

    def launch_bullet(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= 500:  # Vérifier si 0,5 secondes se sont écoulées
            self.all_bullet.add(Bullet(self))
            self.game.sound_mana.play('tir')
            self.last_shot_time = current_time  # Mettre à jour le temps du dernier tir
    
    def move_right(self):
        if not self.game.check_collision(self, self.game.all_enemy):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity

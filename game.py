from sounds import SoundMana
import pygame
from player import Player
from enemy import Enemy, Enemy1
from bullet import Bullet

class Game:
    def __init__(self):
        self.is_playing = False
        self.all_player = pygame.sprite.Group() 
        self.player = Player(self)
        self.all_player.add(self.player)
        self.all_enemy = pygame.sprite.Group()
        self.sound_mana = SoundMana()
        self.score = 0
        self.pressed = {}
    
    def start(self):
        self.is_playing = True
        self.sound_mana.play('music')
        self.spawn_enemy()
        self.spawn_enemy()

    def game_over(self):
        self.all_enemy = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False
        self.score = 0
        self.sound_mana.stop('music')
        self.sound_mana.play('game_over')

    def update(self, screen):
        font = pygame.font.SysFont("Verdana", 60)
        score_text = font.render(f"Score : {self.score}", 1, (255,0,0))
        screen.blit(score_text, (20,20))

        screen.blit(self.player.image, self.player.rect)

        self.player.update_health_bar(screen)
        for bullet in self.player.all_bullet:
            bullet.move()

        for enemy in self.all_enemy:
            enemy.forward()
        self.player.all_bullet.draw(screen)

        self.all_enemy.draw(screen)

        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 890:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
        elif self.pressed.get(pygame.K_UP):
            self.player.jump()

    def spawn_enemy(self):
        enemy = Enemy(self)
        enemy1 = Enemy1(self)
        self.all_enemy.add(enemy)
        self.all_enemy.add(enemy1)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
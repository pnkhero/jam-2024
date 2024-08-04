import pygame
import random
from sounds import SoundMana
from player import Player
from enemy import Enemy, Enemy1
from bullet import Bullet
from lunetteheal import HealthPack
import time

class Game:
    def __init__(self):
        self.is_playing = False
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)
        self.all_enemy = pygame.sprite.Group()
        self.all_healthpacks = pygame.sprite.Group()
        self.sound_mana = SoundMana()
        self.score = 0
        self.pressed = {}
        self.last_spawn_time = time.time()

        # Initialize dragon image and rect
        self.dragon_image = pygame.image.load('asset/dragon.png').convert_alpha()
        self.dragon_rect = self.dragon_image.get_rect(topleft=(0, 550))  # Set initial position of the dragon

    def start(self):
        self.is_playing = True
        self.sound_mana.play('music')
        self.spawn_enemy()
        self.spawn_enemy()
        self.spawn_healthpack(400, 0)

    def reset_game(self):
        self.is_playing = False
        self.all_enemy.empty()
        self.all_healthpacks.empty()
        self.player.health = self.player.max_health
        self.player.rect.x = 250
        self.player.rect.y = 690
        self.score = 0
        self.last_spawn_time = time.time()

    def game_over(self):
        self.sound_mana.stop('music')
        self.sound_mana.play('game_over')
        self.reset_game()

    def update(self, screen):
        current_time = time.time()
        if current_time - self.last_spawn_time >= 10:
            self.spawn_healthpack(random.randint(200, screen.get_width() - 30), 0)
            self.last_spawn_time = current_time

        font = pygame.font.SysFont("Verdana", 60)
        score_text = font.render(f"Score : {self.score}", 1, (255, 0, 0))
        screen.blit(score_text, (20, 20))

        screen.blit(self.player.image, self.player.rect)
        self.player.update_health_bar(screen)

        for bullet in self.player.all_bullet:
            bullet.move()

        for enemy in self.all_enemy:
            enemy.forward()

        for healthpack in self.all_healthpacks:
            healthpack.update()

        self.player.all_bullet.draw(screen)
        self.all_enemy.draw(screen)
        self.all_healthpacks.draw(screen)

        # Check for collisions with health packs
        healthpacks_collided = pygame.sprite.spritecollide(self.player, self.all_healthpacks, True, pygame.sprite.collide_mask)
        if healthpacks_collided:
            self.player.health = min(self.player.health + 20, self.player.max_health)

        # Check for collision with dragon
        if self.player.rect.colliderect(self.dragon_rect):
            self.player.health = 0
            self.game_over()

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

    def spawn_healthpack(self, x, y):
        healthpack = HealthPack(self, x, y)
        self.all_healthpacks.add(healthpack)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

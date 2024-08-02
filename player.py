import pygame
from bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 3
        self.jump_velocity = 15
        self.gravity = 0.8
        self.is_jumping = False
        self.jump_speed = 0
        self.all_bullet = pygame.sprite.Group()
        
        self.sprite_sheet = pygame.image.load('asset/play.png').convert_alpha()
        self.frames_right = self.load_frames(self.sprite_sheet, 8, offset_x=0) 
        self.frames_left = [pygame.transform.flip(frame, True, False) for frame in self.frames_right]
        self.frames = self.frames_right
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 690
        self.last_shot_time = 0
        self.last_update_time = 0
        self.frame_rate = 100

    def load_frames(self, sprite_sheet, num_frames, scale=None, offset_x=0):
        frames = []
        frame_width = sprite_sheet.get_width() // num_frames
        frame_height = sprite_sheet.get_height()

        for i in range(num_frames):
            frame = sprite_sheet.subsurface(pygame.Rect(i * frame_width + offset_x, 0, frame_width, frame_height))
            if scale:
                frame = pygame.transform.scale(frame, scale)
            frames.append(frame)
        frames.append(frames[0])

        return frames

    def update_animation(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update_time > self.frame_rate:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            self.last_update_time = current_time

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            self.game.game_over()

    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + -15, self.rect.y + -10, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + -15, self.rect.y + -10, self.health, 5])

    def launch_bullet(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= 500:
            self.all_bullet.add(Bullet(self))
            self.game.sound_mana.play('tir')
            self.last_shot_time = current_time

    def move_right(self):
        if not self.game.check_collision(self, self.game.all_enemy):
            self.rect.x += self.velocity
            self.frames = self.frames_right
            self.update_animation()

    def move_left(self):
        if not self.game.check_collision(self, self.game.all_enemy):
            self.rect.x -= self.velocity
            self.update_animation()

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.jump_speed = self.jump_velocity

    def apply_gravity(self):
        if self.is_jumping or self.rect.y < 690:
            self.rect.y -= self.jump_speed
            self.jump_speed -= self.gravity
            if self.rect.y >= 690:
                self.rect.y = 690
                self.is_jumping = False
                self.jump_speed = 0

    def update(self):
        self.update_animation()
        self.apply_gravity()
        self.all_bullet.update()

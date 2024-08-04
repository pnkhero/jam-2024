import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.8
        self.velocity = random.randint(3, 5)
        self.all_bullet = pygame.sprite.Group()
        
        self.sprite_sheet = pygame.image.load('asset/eny.png').convert_alpha()
        self.frames_right = self.load_frames(self.sprite_sheet, 12)
        self.frames_left = [pygame.transform.flip(frame, True, False) for frame in self.frames_right]
        self.frames = self.frames_right
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        
        self.rect = self.image.get_rect()
        self.rect.x = 1200
        self.rect.y =  715
        self.hit_time = None
        self.last_update_time = 0
        self.frame_rate = 300

    def load_frames(self, sprite_sheet, num_frames, scale=None):
        frames = []
        frame_width = sprite_sheet.get_width() // num_frames
        frame_height = sprite_sheet.get_height()

        for i in range(num_frames):
            frame = sprite_sheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
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

    def remove(self):
        self.game.score += 20
        self.rect.x = 1200
        self.rect.y = 715
        self.velocity = random.randint(3, 5)
        self.hit_time = None

    def forward(self):
        if self.rect.x < -300:
            self.game.score -= 20
            self.remove()
        if not self.game.check_collision(self, self.game.all_player):
            self.rect.x -= self.velocity
            self.update_animation()
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
        self.velocity = random.randint(3, 5)
        self.all_bullet = pygame.sprite.Group()
        self.image = pygame.image.load('asset/enemy2.png')
        self.image = pygame.transform.scale(self.image,(300,300))
        self.rect = self.image.get_rect()
        self.rect.x = 1200
        self.rect.y = 500 + random.randint(0, 200)
        self.hit_time = None

    def remove(self):
        self.game.score += 20
        self.rect.x = 1200
        self.rect.y = 500 + random.randint(0, 200)
        self.velocity = random.randint(3, 5)
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


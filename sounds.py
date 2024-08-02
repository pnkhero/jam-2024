import pygame

class SoundMana:
    def __init__(self):
        self.sounds = {
            'click': pygame.mixer.Sound("asset/sounds/click.ogg"),
            'game_over': pygame.mixer.Sound("asset/sounds/game_over.ogg"),
            'tir': pygame.mixer.Sound("asset/sounds/tir.ogg"),
            'music': pygame.mixer.Sound("asset/sounds/Blue.ogg")
        }
    
    def play(self, name):
        self.sounds[name].play()
    def stop(self, name):
        self.sounds[name].stop()
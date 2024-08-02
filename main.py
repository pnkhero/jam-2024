#! /usr/bin/python3

import pygame
import math
from game import Game

pygame.init()

clock = pygame.time.Clock()
FPS = 40  # Augmentation des FPS pour une animation plus fluide

# Fenêtre de jeu
pygame.display.set_caption("waterland")
screen = pygame.display.set_mode((1200, 900))

# Charger et convertir les images d'arrière-plan et autres assets
background = pygame.image.load('asset/bg.jpg').convert()
nuage = pygame.image.load('asset/nuage.png').convert_alpha()
nuage1 = pygame.image.load('asset/nuage.png').convert_alpha()
zozo = pygame.image.load('asset/zozo.png').convert_alpha()
zozo = pygame.transform.scale(zozo, (700, 300))
soleil = pygame.image.load('asset/soleil.png').convert_alpha()
soleil = pygame.transform.scale(soleil, (300, 300))
banner = pygame.image.load('asset/banner.png').convert_alpha()
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# Bouton play
play_button = pygame.image.load('asset/button.png').convert_alpha()
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)
zozo_rect = zozo.get_rect()
zozo_rect.x = math.ceil(screen.get_width() / 2)
zozo_rect.y = math.ceil(screen.get_height() / 2.50)
soleil_rect = zozo.get_rect()
soleil_rect.x = math.ceil(screen.get_width() / 2)
soleil_rect.y = math.ceil(screen.get_height() / 2.50)

# Initialiser les positions des arrière-plans
background_x = 0
nuage_x = 0
nuage1_x = screen.get_width() // 2

game = Game()

running = True

# Mettre à jour l'écran
pygame.display.flip()

# Boucle de jeu
while running:
    # Appliquer l'arrière-plan
    screen.blit(background, (background_x, 0))
    screen.blit(background, (background_x + background.get_width(), 0))

    # Effet de parallaxe pour les nuages
    nuage_x -= 1
    nuage1_x -= 1

    if nuage_x <= -nuage.get_width():
        nuage_x = screen.get_width()

    if nuage1_x <= -nuage1.get_width():
        nuage1_x = screen.get_width()

    screen.blit(nuage, (nuage_x, 50))
    screen.blit(nuage1, (nuage1_x, 100))

    if game.is_playing:
        screen.blit(soleil, (920, 0))
        game.update(screen)
    else:
        screen.blit(banner, banner_rect)
        screen.blit(play_button, play_button_rect)
        screen.blit(zozo, zozo_rect)

    pygame.display.flip()

    # Fermer la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit(0)
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.launch_bullet()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()
                game.sound_mana.play('click')

    clock.tick(FPS)

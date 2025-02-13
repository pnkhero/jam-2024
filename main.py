#! /usr/bin/python3

import pygame
import math
from game import Game

pygame.init()

clock = pygame.time.Clock()
FPS = 40

pygame.display.set_caption("waterland")
screen = pygame.display.set_mode((1200, 900))

background = pygame.image.load('asset/sky.png').convert()
mountain = pygame.image.load('asset/mountain.png').convert_alpha()
sol = pygame.image.load('asset/sol.png').convert_alpha()
soleil = pygame.image.load('asset/soleil.png').convert_alpha()
soleil = pygame.transform.scale(soleil, (300, 300))
banner = pygame.image.load('asset/banner.png').convert_alpha()
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

play_button = pygame.image.load('asset/button.png').convert_alpha()
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)
restart_button = pygame.image.load('asset/button.png').convert_alpha()
restart_button = pygame.transform.scale(restart_button, (400, 150))
restart_button_rect = restart_button.get_rect()
restart_button_rect.x = math.ceil(screen.get_width() / 3.33)
restart_button_rect.y = math.ceil(screen.get_height() / 2)

background_x = 0
mountain_x = 0
mountain_y = screen.get_height() - mountain.get_height() - 50
sol_x = 0
sol_y = screen.get_height() - sol.get_height()

game = Game()

running = True

pygame.display.flip()

while running:

    background_x -= 0.4
    mountain_x -= 1
    sol_x -= 2

    if background_x <= -background.get_width():
        background_x = 0
    if mountain_x <= -mountain.get_width():
        mountain_x = 0
    if sol_x <= -sol.get_width():
        sol_x = 0

    screen.blit(background, (background_x, 0))
    screen.blit(background, (background_x + background.get_width(), 0))
    screen.blit(mountain, (mountain_x, mountain_y))
    screen.blit(mountain, (mountain_x + mountain.get_width(), mountain_y))
    screen.blit(sol, (sol_x, sol_y))
    screen.blit(sol, (sol_x + sol.get_width(), sol_y))

    if game.is_playing:
        screen.blit(soleil, (920, 0))
        screen.blit(game.dragon_image, game.dragon_rect.topleft)
        game.update(screen)
    else:
        screen.blit(banner, banner_rect)
        if game.player.health == 0:
            screen.blit(restart_button, restart_button_rect)
        else:
            screen.blit(play_button, play_button_rect)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit(0)
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.launch_bullet()
            elif event.key == pygame.K_UP:
                game.player.jump()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos) and not game.is_playing:
                game.start()
                game.sound_mana.play('click')
            elif restart_button_rect.collidepoint(event.pos) and not game.is_playing:
                game.start()
                game.sound_mana.play('click')

    clock.tick(FPS)

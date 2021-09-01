import pygame


def inputs(sprite_handler, player):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_r:
                player.input_event("r")
                

    return True
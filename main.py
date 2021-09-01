import pygame, time, sprite_handler_class, enemy_controller_class, ally_controller_class, ship_class, bullet_class, input_handler, player_class


def main():
    pygame.init()
    pygame.display.init()
    screen = pygame.display.set_mode([1280, 720], pygame.RESIZABLE)
    gameSurface = pygame.Surface(pygame.display.get_window_size())

    t = time.time()  #time for fps

    sprite_handler = sprite_handler_class.Sprite_Handler()
    enemy_controller = enemy_controller_class.Enemy_Controller(sprite_handler)
    ally_controller = ally_controller_class.Ally_Controller(sprite_handler)
    player = player_class.Player(sprite_handler)
    sprite_handler.create_wall()

    running = True
    while running:

        running = input_handler.inputs(sprite_handler, player)


        enemy_controller.update()
        ally_controller.update() 
        sprite_handler.update()
        player.update()

        gameSurface.fill((50, 50, 50))
        for w in sprite_handler.walls:
            gameSurface.blit(w.image, w.rect)
        for s in sprite_handler.ships:
            gameSurface.blit(s.image, s.rect)
        for g in sprite_handler.guns:
            gameSurface.blit(g.image, g.rect)
        for b in sprite_handler.bullets:
            gameSurface.blit(b.image, b.rect)
        for x in sprite_handler.explosions:
            gameSurface.blit(x.image, x.rect)

        zoomed_gameSurface = pygame.transform.scale(
            gameSurface, (pygame.display.get_window_size()))
        screen.blit(zoomed_gameSurface, (0, 0))
        #print(screen,pygame.display.get_window_size())
        pygame.display.flip()

        #makes 60 fps
        while (time.time() - t <= 0.016):
            pass
        print("ms/frame :",round((time.time() - t)*1000, 2), " |  fps:", round(1/(time.time() - t),1))
        t = time.time()
        print()


if __name__ == "__main__":
    main()
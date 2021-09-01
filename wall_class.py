import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, sprite_handler, x, y, length, width):
        super(Wall, self).__init__()
        self.image = pygame.Surface((length, width))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.image)

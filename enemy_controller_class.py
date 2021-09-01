import pygame, random, stats, pythagoras


class Enemy_Controller:
    def __init__(self, sprite_handler):
        self.sprite_handler = sprite_handler
        self.timer = 100

        self.sprite_handler.create_ship((900, 300), 90, "small_robot_ship", self)

    def update(self):
        self.timer -= 1
        if self.timer == 0:
            self.timer = 50
            r = random.randint(0,100)
            if r > 10:
                self.sprite_handler.create_ship(
                    (pygame.display.get_window_size()[0] +
                    stats.dictionary["small_robot_ship"]["width"] / 2, random.randint(100, 620)),
                    90, "small_robot_ship", self)
            else:
                self.sprite_handler.create_ship(
                    (pygame.display.get_window_size()[0] +
                    stats.dictionary["small_bio_ship"]["width"] / 2, random.randint(100, 620)),
                    90, "small_bio_ship", self)
        self.enemies_move()
        self.enemies_shoot()

    def enemies_move(self):
        for sprite in self.sprite_handler.ships:            
            if sprite.owner == self:
                sprite.move(pythagoras.get_target(sprite.pos, 90, 100))

    def enemies_shoot(self):
        for sprite in self.sprite_handler.ships:            
            if sprite.owner == self:
                sprite.shoot()

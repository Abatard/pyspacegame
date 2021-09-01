import pygame, random, stats, pythagoras


class Ally_Controller:
    def __init__(self, sprite_handler):
        self.sprite_handler = sprite_handler
        self.angle = 270
        self.timer = 100


        self.sprite_handler.create_ship((200, 300), self.angle, "small_robot_ship", self)

    def update(self):
        self.timer -= 1
        if self.timer == 0:
            self.timer = 50
            r = random.randint(0,100)
            if r > 10:
                self.sprite_handler.create_ship(
                    (0 - stats.dictionary["small_robot_ship"]["width"] / 2, random.randint(100, 620)),
                    self.angle, "small_robot_ship", self)
            else:
                self.sprite_handler.create_ship(
                    (0 - stats.dictionary["small_bio_ship"]["width"] / 2, random.randint(100, 620)),
                    self.angle, "small_bio_ship", self)
        self.allies_move()
        self.allies_shoot()

    def allies_move(self):
        for sprite in self.sprite_handler.ships:            
            if sprite.owner == self:
                sprite.move(pythagoras.get_target(sprite.pos, self.angle, 100))

    def allies_shoot(self):
        for sprite in self.sprite_handler.ships:            
            if sprite.owner == self:
                sprite.shoot()

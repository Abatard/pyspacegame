import pygame, random, stats, pythagoras


class Bullet(pygame.sprite.Sprite):
    def __init__(self, sprite_handler, pos, angle, typ, owner):
        super(Bullet, self).__init__()
        self.stats = stats.dictionary.get(typ).copy()
        self.pos = pygame.math.Vector2(pos)
        self.angle = angle
        self.typ = typ
        self.owner = owner
        self.sprite_handler = sprite_handler

        self.sprite_list = self.sprite_handler.sprite_dict[
            self.typ]["sprite_list"]

        self.sprite_handler.animator(self)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.sprite_handler.move_sprite(
            self, pythagoras.get_target(self.pos, self.angle, 100))
        self.check_collision()

    def check_collision(self):
        for sprite in self.sprite_handler.ships:
            if pygame.sprite.collide_mask(
                    self,
                    sprite) and sprite.stats["exploding"] == False and sprite.owner != self.owner:
                #print("ships collision")
                self.sprite_handler.explode(self)
                self.sprite_handler.damage_sprite(sprite, self.stats["damage"])
                self.kill()

        for sprite in self.sprite_handler.walls:
            if pygame.sprite.collide_mask(self, sprite) != None:
                #print("walls collision")
                self.sprite_handler.create_explosion(self.pos,
                                                     random.randint(0, 359),
                                                     "simple_explosion")
                self.kill()

        for sprite in self.sprite_handler.bullets:
            if pygame.sprite.collide_mask(self, sprite) and sprite != self and sprite.owner != self.owner:
                #print("bullets collision")
                self.sprite_handler.create_explosion(self.pos,
                                                     random.randint(0, 359),
                                                     "simple_explosion")
                sprite.kill()
                self.kill()

        for sprite in self.sprite_handler.guns:
            if pygame.sprite.collide_mask(
                    self, sprite) and sprite != self and sprite.stats[
                        "exploding"] == False and sprite.owner != self.owner:
                #print("guns collision")
                self.sprite_handler.create_explosion(self.pos,
                                                     random.randint(0, 359),
                                                     "simple_explosion")
                self.sprite_handler.damage_sprite(sprite, self.stats["damage"])
                self.kill()
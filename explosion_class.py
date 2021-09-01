import pygame, stats


class Explosion(pygame.sprite.Sprite):
    def __init__(self, sprite_handler, pos, angle, typ):
        super(Explosion, self).__init__()
        self.stats = stats.dictionary.get(typ).copy()
        self.pos = pygame.math.Vector2(pos)
        self.angle = angle
        self.typ = typ
        self.sprite_handler = sprite_handler

        self.sprite_list = self.sprite_handler.sprite_dict[self.typ]["sprite_list"]

        self.sprite_handler.animator(self)

    def get_stats(self, explosion_typ):
        if explosion_typ == "simple_explosion":
            return stats.simple_explosion

    def update(self):
    	self.stats["animation_lifetime_counter"] -= 1
    	if self.stats["animation_lifetime_counter"] <= 0:
    		self.kill()
    	self.sprite_handler.animator(self)


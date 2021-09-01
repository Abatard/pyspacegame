import pygame, gun_class, stats


class Ship(pygame.sprite.Sprite):
    def __init__(self, sprite_handler, pos, angle, typ, owner):
        super(Ship, self).__init__()
        self.stats = stats.dictionary[typ].copy()
        self.pos = pygame.math.Vector2(pos)
        self.angle = angle
        self.sprite_handler = sprite_handler
        self.owner = owner
        self.typ = typ
        self.guns = []

        self.sprite_list = self.sprite_handler.sprite_dict[
            self.typ]["sprite_list"]
        self.sprite_handler.animator(self)
        self.mask = pygame.mask.from_surface(self.image)

        self.get_gun()

    def get_gun(self):
        for for_counter in range(len(self.stats["guns"])):
            self.guns.append(
                gun_class.Gun(self.sprite_handler, self,
                              self.stats["guns"][for_counter]["x_offset"],
                              self.stats["guns"][for_counter]["y_offset"],
                              self.angle,
                              self.stats["guns"][for_counter]["typ"],
                              self.owner))

            self.guns[for_counter].stats["speed"] = self.stats["speed"]
            self.sprite_handler.guns.add(self.guns[for_counter])

    def update(self):
        if not self.stats["exploding"]:
            self.sprite_handler.animator(self)
        else:
            self.sprite_handler.explode(self)

    def move(self, target):
        if not self.stats["exploding"]:
            self.sprite_handler.move_sprite(self, target)
            for gun in self.guns:
                gun.update_position()

    def shoot(self):
        for gun in self.guns:
            gun.shoot()

    def turn(self):
        self.image = pygame.transform.rotate(self.imageBackup, self.angle)
        self.rect = self.image.get_rect(center=(self.posX, self.posY))

    def destroy(self):
        self.sprite_handler.explode(self)
        for gun in self.guns:
            gun.destroy()

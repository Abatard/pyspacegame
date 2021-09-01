import pygame, stats, random


class Gun(pygame.sprite.Sprite):
    def __init__(self, sprite_handler, mount, x_offset, y_offset, angle, typ,
                 owner):
        super(Gun, self).__init__()
        self.stats = stats.dictionary.get(typ).copy()
        self.pos = pygame.math.Vector2(0,0)
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.angle = angle
        self.mount = mount
        self.typ = typ
        self.owner = owner
        self.sprite_handler = sprite_handler

        self.sprite_list = self.sprite_handler.sprite_dict[
            self.typ]["sprite_list"]

        self.mount.sprite_handler.animator(self)
        self.mask = pygame.mask.from_surface(self.image)

        self.get_pos()

    def get_pos(self):
        if self.mount.stats["typ"] == "small_bio_ship":
            if self.mount.angle == 90:
                self.pos[0] = self.mount.pos[0]
                self.pos[1] = self.mount.pos[1] - self.mount.image.get_height(
                ) / 2 - self.image.get_height() / 2
            if self.mount.angle == 270:
                self.pos[0] = self.mount.pos[0] + self.image.get_width() / 3.5
                self.pos[1] = self.mount.pos[1] - self.mount.image.get_height(
                ) / 2 - self.image.get_height() / 2
        elif self.mount.stats["typ"] == "small_robot_ship":
            if self.mount.angle == 90:
                self.pos[0] = self.mount.pos[0] - self.stats[
                    "width"] * self.x_offset
                self.pos[1] = self.mount.pos[1] - self.stats[
                    "height"] * self.y_offset
            elif self.mount.angle == 270:
                self.pos[0] = self.mount.pos[0] - self.stats[
                    "width"] * self.x_offset
                self.pos[1] = self.mount.pos[1] - self.stats[
                    "height"] * self.y_offset

    def update(self):
        self.mount.sprite_handler.animator(self)
        if not self.stats["exploding"]:
            #self.mount.sprite_handler.animator(self)
            self.update_weapon()

        else:
            self.sprite_handler.explode(self)

    def update_weapon(self):
        if self.stats["ticks_per_shot_counter"] > 0:
            self.stats["ticks_per_shot_counter"] -= 1

    def update_position(self):
        self.get_pos()



    def shoot(self):

        if self.stats["ticks_per_shot_counter"] == 0:
            self.stats["ticks_per_shot_counter"] += self.stats[
                "ticks_per_shot"]

            if self.angle == 90:
                self.sprite_handler.create_bullet((
                    self.pos[0] - self.stats["width"] / 2 -
                    stats.stats_get(self.stats["bullet_typ"], "width") / 2,
                    self.pos[1]), random.randint(self.angle-10,self.angle+10), self.owner)

            if self.angle == 270:
                self.sprite_handler.create_bullet((
                    self.pos[0] + self.stats["width"] / 2 +
                    stats.stats_get(self.stats["bullet_typ"], "width") / 2,
                    self.pos[1]), random.randint(self.angle-10,self.angle+10), self.owner)

    def destroy(self):
        self.sprite_handler.explode(self)

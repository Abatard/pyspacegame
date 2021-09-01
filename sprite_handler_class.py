import pygame, math, random, ship_class, bullet_class, wall_class, explosion_class, gun_class


class Sprite_Handler:
    def __init__(self):

        self.ships = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.guns = pygame.sprite.Group()

        self.load_sprites()

    def update(self):
        self.ships.update()
        self.guns.update()
        self.bullets.update()
        self.explosions.update()

        self.out_of_screen_sprite_deleter()
        print(self.ships, self.bullets, self.explosions, self.guns)

    def create_wall(self):
        self.walls.add(wall_class.Wall(self, 0, 0, 1280, 10))
        self.walls.add(wall_class.Wall(self, 0, 710, 1280, 10))

    def create_ship(self, pos, angle, typ, owner):
        ship = ship_class.Ship(self, pos, angle, typ, owner)
        self.ships.add(ship)
        return ship

    def create_gun(self, ship, x_offset, y_offset, angle, gun_typ, owner):
        self.guns.add(
            gun_class.Gun(self, ship, x_offset, y_offset, angle, gun_typ,
                          owner))

    def create_bullet(self, pos, angle, owner):
        self.bullets.add(
            bullet_class.Bullet(self, pos, angle, "simple_bullet", owner))

    def create_explosion(self, pos, angle, typ):
        self.explosions.add(explosion_class.Explosion(self, pos, angle, typ))

    def move_sprite(self, sprite, target):
        direction = target - sprite.pos
        velocity = direction.normalize()

        if max(velocity[0], velocity[1]
               ) > 0:  #schaut welcher wert in velocity größer ist und
            velocity * (
                1 / max(velocity[0], velocity[1])
            )  #multipliziert zu 1 um denn mit speed zu multiplizieren
        else:
            velocity * (1 / min(velocity[0], velocity[1]))
        velocity *= sprite.stats["speed"]
        sprite.pos += velocity
        sprite.rect.center = (sprite.pos[0], sprite.pos[1])

    def animator(self, sprite):
        sprite.stats["animation_cycle_counter"] += 1
        if sprite.stats["animation_cycle_counter"] >= sprite.stats[
                "animation_cycle_max"]:
            sprite.stats["animation_cycle_counter"] = 0
            sprite.stats["animation_sprite_number_counter"] += 1
            if sprite.stats["animation_sprite_number_counter"] == len(
                    sprite.sprite_list):
                sprite.stats["animation_sprite_number_counter"] = 0

        sprite.image = pygame.transform.scale(
            sprite.sprite_list[
                sprite.stats["animation_sprite_number_counter"]],
            (sprite.stats["width"], sprite.stats["height"]))
        sprite.imageBackup = sprite.image
        sprite.image = pygame.transform.rotate(sprite.image, sprite.angle)
        sprite.rect = sprite.image.get_rect(center=(sprite.pos[0],
                                                    sprite.pos[1]))

    def damage_sprite(self, sprite, damage):
        sprite.stats["health"] -= damage
        if sprite.stats["health"] <= 0:
            sprite.destroy()

    def explode(self, sprite):
        if sprite.stats["exploding"] == False:
            sprite.stats["exploding"] = True

        sprite.stats["exploding_duration"] -= 1
        if sprite.stats["exploding_duration"] % sprite.stats[
                "exploding_modulus"] == 0:
            for _ in range(sprite.stats["explosion_amount"]):
                self.create_explosion(
                    (sprite.pos[0] +
                     random.randint(-int(sprite.stats["width"] / 3),
                                    int(sprite.stats["width"] / 3)),
                     sprite.pos[1] +
                     random.randint(-int(sprite.stats["height"] / 3),
                                    int(sprite.stats["height"] / 3))),
                    random.randint(0, 359), "simple_explosion")
        if sprite.stats["exploding_duration"] <= 0:
            sprite.kill()

    def out_of_screen_sprite_deleter(self):
        for sprite in self.guns:
            self.delete_sprite(sprite)
        for sprite in self.ships:
            self.delete_sprite(sprite)
        for sprite in self.bullets:
            self.delete_sprite(sprite)

    def delete_sprite(self, sprite):
        if sprite.pos[0] < -300 or sprite.pos[
                0] > pygame.display.get_window_size(
                )[0] + 300 or sprite.pos[1] < -300 or sprite.pos[
                    1] > pygame.display.get_window_size()[1] + 300:
            sprite.kill()

    def load_sprites(self):
        self.sprite_dict = {
            "simple_explosion": {
                "sprite_list": [
                    pygame.image.load("explosion_art/simple_explosion_1.png"
                                      ).convert_alpha(),
                    pygame.image.load("explosion_art/simple_explosion_2.png"
                                      ).convert_alpha(),
                    pygame.image.load("explosion_art/simple_explosion_3.png"
                                      ).convert_alpha(),
                    pygame.image.load("explosion_art/simple_explosion_4.png"
                                      ).convert_alpha(),
                    pygame.image.load("explosion_art/simple_explosion_5.png"
                                      ).convert_alpha(),
                    pygame.image.load("explosion_art/simple_explosion_6.png").
                    convert_alpha()
                ]
            },
            "small_bio_ship": {
                "sprite_list": [
                    pygame.image.load(
                        "ship_art/small_bio_ship_1.png").convert_alpha(),
                    pygame.image.load(
                        "ship_art/small_bio_ship_2.png").convert_alpha()
                ]
            },
            "small_robot_ship": {
                "sprite_list": [
                    pygame.image.load(
                        "ship_art/small_robot_ship_1.png").convert_alpha(),
                    pygame.image.load(
                        "ship_art/small_robot_ship_2.png").convert_alpha(),
                    pygame.image.load(
                        "ship_art/small_robot_ship_3.png").convert_alpha(),
                    pygame.image.load(
                        "ship_art/small_robot_ship_4.png").convert_alpha(),
                    pygame.image.load(
                        "ship_art/small_robot_ship_5.png").convert_alpha(),
                    pygame.image.load(
                        "ship_art/small_robot_ship_6.png").convert_alpha()
                ]
            },
            "simple_bullet": {
                "sprite_list": [pygame.image.load('bimg.png').convert_alpha()]
            },
            "simple_gun": {
                "sprite_list": [
                    pygame.image.load(
                        'gun_art/simple_gun_1.png').convert_alpha(),
                    pygame.image.load(
                        'gun_art/simple_gun_2.png').convert_alpha()
                ]
            }
        }

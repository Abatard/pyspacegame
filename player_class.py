import pygame, stats, ship_class, pythagoras

class Player:
    def __init__(self, sprite_handler):
        self.stats = stats.dictionary["player"]
        self.sprite_handler=sprite_handler
        self.ship = None
        #self.create_ship()

    def create_ship(self):
        self.ship = self.sprite_handler.create_ship((300,300),270,self.stats["ship"],self)
        self.ship.stats["health"]=self.stats["health"]


    def update(self):
        if self.ship:
            self.inputs()


    def input_event(self, key):
        if key == "r":
            self.create_ship()

    def move(self, move_angle):
        if self.ship.stats["exploding"] == False:
            self.ship.move(pythagoras.get_target(self.ship.pos, move_angle, 100))
        #if self.ship.stats["exploding"] == False:
        #    self.ship.posX += self.ship.stats["speed"] * x
        #    self.ship.posY += self.ship.stats["speed"] * y
        #for gun in self.ship.guns:
        #    if gun.stats["exploding"] == False:
        #        gun.posX += self.ship.stats["speed"] * x
        #        gun.posY += self.ship.stats["speed"] * y

    def inputs(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.move(0) # 1,0,-1 vorwärts, halt, rückwärts
        if keys[pygame.K_s]:
            self.move(180)
        if keys[pygame.K_a]:
            self.move(90)
        if keys[pygame.K_d]:
            self.move(270)
        if keys[pygame.K_SPACE]:
            self.ship.shoot()
import pygame
import os

class Bird:
    IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))),
             pygame.transform.scale2x(pygame.image.load(
                 os.path.join("imgs", "bird2.png"))),
             pygame.transform.scale2x(pygame.image.load(
                 os.path.join("imgs", "bird3.png")))
             ]
    MAX_ROTATION = 25
    ROT_VEL = 20  # Le nombre de degré qu'il perd à chaque "seconde"
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0  # la rotation par rapport à l'horizontale
        self.tick_count = 0  # compte le nombre de "seconde" depuis le derrnier saut
        self.vel = 0
        self.height = self.y
        # Permet de connaitre à quel séquence du vol on est (ailes vers le bas)
        self.img_count = 0
        self.img = self.IMGS[0]

    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1
        # fonction de déplacement en fonction du "temps"
        d = self.vel*self.tick_count + 1.5*self.tick_count**2

        if d >= 16:
            d = 16
        if d < 0:
            d -= 2
        self.y = self.y + d

        if d < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL

    def draw(self, win):
        self.img_count += 1

        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count < self.ANIMATION_TIME*2:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME*3:
            self.img = self.IMGS[2]
        elif self.img_count < self.ANIMATION_TIME*4:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME*4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0

        # S'il est en train de déscendre en vertical, pas besoin de le faire agiter ses ailes:
        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME*2

        # centre de rotation c'est le coin supérieur gauche donc il faut le corriger juste en dessous)
        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft = (self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)
        # Affichage: on fait la rotation et on le place à l'endroit de new_rect

    def get_mask(self):
        return pygame.mask.from_surface(self.img) #A mask is the "space" that an object can take
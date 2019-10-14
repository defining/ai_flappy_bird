import os
from classes.birds import Bird
from classes.pipes import Pipe
from classes.base import Base
import pygame
import neat
import random
import time

pygame.init()

WIN_WIDTH = 500
WIN_HEIGHT = 800
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))

def draw_window(win, bird, pipes, base):
    win.blit(BG_IMG, (0, 0))

    for pipe in pipes:
        pipe.draw(win)
    base.draw(win)
    bird.draw(win)
    pygame.display.update()
    


def main():
    bird = Bird(230, 350)
    base = Base(730)
    pipes = [Pipe(700)]
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    #clock = pygame.time.Clock()

    run = True
    while run:
        #time.sleep(0.2)
        #clock.tick(3000) #pour donner un tempo au jeu quelque soit l'OS mais ne marche pas
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        #bird.move()
        for pipe in pipes:
            pipe.move()
        base.move()
        draw_window(win, bird, pipes, base)
    pygame.quit()
    quit()


main()
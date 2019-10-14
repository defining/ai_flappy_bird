# coding: utf-8
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
STAT_FONT = pygame.font.SysFont("comicsans", 50)

def draw_window(win, bird, pipes, base, score):
    win.blit(BG_IMG, (0, 0))

    for pipe in pipes:
        pipe.draw(win)

    text = STAT_FONT.render("Score: " + str(score), 1, (255,255,255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))
    base.draw(win)
    bird.draw(win)
    pygame.display.update()
    


def main():
    bird = Bird(230, 350)
    base = Base(730)
    pipes = [Pipe(600)]
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    score = 0
    #clock = pygame.time.Clock()

    run = True
    while run:
        #time.sleep(0.2)
        #clock.tick(3000) #pour donner un tempo au jeu quelque soit l'OS mais ne marche pas
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        #bird.move()
        add_pipe = False
        rem = []
        for pipe in pipes:
            if pipe.collide(bird):
                pass
            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                rem.append(pipe)
            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                add_pipe = True
            pipe.move()
        if add_pipe:
            score += 1
            pipes.append(Pipe(600))
        
        for r in rem:
            pipes.remove(r)
        
        if bird.y + bird.img.get_height() >= 730:
            pass

        base.move()
        draw_window(win, bird, pipes, base, score)
    pygame.quit()
    quit()


main()
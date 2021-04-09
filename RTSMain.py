import pygame
import mapper
from config import *
import time
import os
import robot

screen = pygame.display.set_mode((SCREENX,SCREENY))
pygame.display.set_caption("Test")
screen.fill(WHITE) 

def display(list, screen):
    for row in list:
        for col in row:
            if col.has_changed:
                col.display(screen)

def main():

    frame = 0
    start = time.time()
    playMap = mapper.create_Map((SCREENX, SCREENY, TILE_SIZE))
    display(playMap, screen)
    bg_img = mapper.maptojpg(screen)
    screen.blit(bg_img, (0,0))
    clock = pygame.time.Clock()
    x = 0
    y = 0

    robo = robot.Robot(200, 300)
    robo.display(screen)

    running = True

    while running:

        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:       # pylint: disable=no-member
                running = False

        # for row in playMap:
        #     for col in row:
        #         if col.has_changed:
        #             col.display(screen)
        
        #screen.blit(bg_img, (0,0))
        screen.fill(WHITE)
        #pygame.draw.circle(screen, (0,0,0), (1000,750), 5)

        robo.find_destination(pygame.mouse.get_pos())
        robo.move()
        robo.display(screen)

        pygame.display.flip()

        frame += 1

        if time.time() - start >= 1:
            pygame.display.set_caption(f"{frame}")
            frame = 0
            start = time.time()

main()
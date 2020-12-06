import random
import tile
from config import *
import pygame

def maptojpg(screen):
    screen_data = pygame.image.tostring(screen, 'RGBA')
    bg_img = pygame.image.fromstring(screen_data, (SCREENX,SCREENY), 'RGBA')
    return bg_img

def create_Map(mapParam):
    maxX, maxY, tileSize = mapParam
    if maxX % tileSize != 0 or maxY % tileSize != 0:
        raise Exception("No")
    
    playmap = []
    ycoord = 0
    for i in range(0, int(maxY/tileSize)):
        placeholder = []
        xcoord = 0
        for i in range(0, int(maxX/tileSize)):
            placeholder.append(tile.Tile(xcoord, ycoord, GREEN_PRESETS[random.randint(0, len(GREEN_PRESETS)-1)]))
            xcoord += TILE_SIZE
        playmap.append(placeholder)
        del placeholder
        ycoord += tileSize
    
    print(maxY/tileSize, maxX/tileSize)
    return playmap

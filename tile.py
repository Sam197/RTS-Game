from config import *
from pygame import draw as pygame_draw

global id_num
idnum = ORGINAL_TILE_INDEX

class Tile:

    def __init__(self, x, y, colour):
        global idnum
        self.id = idnum
        idnum += 1
        self.x = x
        self.y = y
        self.colour = colour
        self.tileSize = TILE_SIZE
        self.has_changed = True
    
    def __repr__(self):
        return(f"Tile object, id {self.id}, coords ({self.x},{self.y}), size {self.tileSize}, colour {self.colour}")

    def display(self, screen):
        pygame_draw.rect(screen, self.colour, (self.x, self.y, self.tileSize, self.tileSize))
        #self.has_changed = False
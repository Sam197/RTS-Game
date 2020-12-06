from config import *
from entity import Entity
from pygame import image
from os import path

class Robot(Entity):
    
    def __init__(self, x, y):
        Entity.__init__(self, x, y)
        self.img = image.load(path.join('sprites', ENITY_SPRITES[0]))
        self.ref_img = self.img
from config import *
from entity import Entity
from pygame import image
from os import path

class Robot(Entity):
    
    def __init__(self, x, y):
        Entity.__init__(self, x, y)
        self.img = image.load(path.join('sprites', ENITY_SPRITES[0]))
        self.ref_img = self.img
        self.offsetWidth = int(0.5*(self.img.get_width()))
        self.offsetHeight = int(0.5*(self.img.get_height()))
        self.centreX = int(0.5*(self.img.get_width())) + x
        self.centreY = int(0.5*(self.img.get_height())) + y
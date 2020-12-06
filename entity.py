from config import *
from pygame import image, transform
from os import path
import math

class Entity:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = None
        self.ref_img = None
        self.rotateAngle = 0

    def find_quadrant(self, displacementX, displacementY):
        if displacementX > 0 and displacementY < 0:
            return 1
        elif displacementX > 0 and displacementY > 0:
            return 2
        elif displacementX < 0 and displacementY > 0:
            return 3
        elif displacementX < 0 and displacementY < 0:
            return 4
        
    def find_angle(self, quadrant):
        if quadrant == 1:
            return -(90 + self.rotateAngle)
        if quadrant == 2:
            return 270 - self.rotateAngle
        if quadrant == 3:
            return 90 - self.rotateAngle
        if quadrant == 4:
            return 90 - self.rotateAngle

    def find_destination(self, destination):
        destx, desty = destination
        displacementX = destx - self.x
        displacementY = desty - self.y
        self.rotateAngle = float(math.atan(displacementY/displacementX)*(180/math.pi))
        self.move_gradient = self.y/self.x
        quadrant = self.find_quadrant(displacementX, displacementY)
        self.rotateAngle = self.find_angle(quadrant)

    def move(self, destination):
        pass

    def display(self, screen):
        self.ref_img = transform.rotate(self.img, self.rotateAngle)
        screen.blit(self.ref_img, (self.x, self.y))
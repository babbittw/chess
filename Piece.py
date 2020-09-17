import pygame

class Piece:

    def __init__(self, screen, img):
        self.image = img
        self.x_tile = 0
        self.y_tile = 0
        self.x = 0
        self.y = 0
        self.screen = screen


    def move(self):
        pass

    def draw(self):
        self.screen.blit(self.image, (self.x,self.y))



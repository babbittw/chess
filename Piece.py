import pygame



class Piece:

    def __init__(self, screen, img):
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (100,100))
        self.x = 0
        self.y = 0
        self.rect = pygame.Rect(100, 100, 100, 100)
        self.screen = screen


    def move_direct(self):
        pass

    def move_drag(self):
        pass

    def get_cords(self):
        pass



    def draw(self):

        x_pixels = self.x * 100
        y_pixels = self.y * 100



        self.screen.blit(self.image, (x_pixels,y_pixels))



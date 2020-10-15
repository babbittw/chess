import pygame
from Piece import Piece

class King(Piece):

    def __init__(self, screen, img):
        super().__init__(screen, img)




    def get_valid_moves(self, old_x, old_y):
        x = old_x // 100
        y = old_y // 100

        output = []

        output.append((x + 1, y))
        output.append((x - 1, y))
        output.append((x + 1, y + 1))
        output.append((x + 1, y - 1))
        output.append((x - 1, y + 1))
        output.append((x - 1, y - 1))
        output.append((x, y + 1))
        output.append((x, y - 1))

        return output

    def is_valid_move(self, old_x, old_y, new_x, new_y):
        moves = self.get_valid_moves(old_x, old_y)

        if (new_x, new_y) in moves:
            return True
        return False


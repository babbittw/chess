import pygame
from Piece import Piece

class King(Piece):

    def __init__(self, screen, img,x ,y):
        super().__init__(screen, img)
        self.x = x
        self.y = y


    def get_valid_moves(self, x, y):

        output = []

        output.append((x + 1, y))
        output.append((x - 1, y))
        output.append((x + 1, y + 1))
        output.append((x + 1, y - 1))
        output.append((x - 1, y + 1))
        output.append((x - 1, y - 1))
        output.append((x, y + 1))
        output.append((x, y - 1))

        output = [move for move in output if not (move[0] > 8 or move[0] < 1 or move[1] > 8 or move[1] < 1)]

        return output



    def move(self):
        pass


    def draw_valid_moves(self):
        move_cords = self.get_valid_moves(self.x, self.y)
        moves = []

        m_img = pygame.image.load("poss_move.png")

        for m in move_cords:
            moves.append(pygame.Rect(m[0], m[1], 100, 100))

        for m in moves:
            self.screen.blit(m_img, (m.x * 100, m.y * 100))



    def is_valid_move(self, old_x, old_y, new_x, new_y):
        moves = self.get_valid_moves(old_x, old_y)

        if (new_x, new_y) in moves:
            return True
        return False


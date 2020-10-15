# This is a sample Python script.

import pygame
from Piece import Piece
from King import King
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

SCREEN_SIZE_PIXELS = 1000
TILE_SIZE_PIXELS = .1 * SCREEN_SIZE_PIXELS

def get_cords(rect):
    x = rect.x // 100
    y = rect.y // 100

    return (x, y)

def get_valid_moves(old_x, old_y):
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

def is_valid(old_x, old_y, new_x, new_y):
    moves = get_valid_moves(old_x, old_y)

    if (new_x, new_y) in moves:
        return True
    return False



def main():




    pygame.init()

    screen = pygame.display.set_mode((SCREEN_SIZE_PIXELS, SCREEN_SIZE_PIXELS))




    pieces_images = []



    # test = Piece(screen, 'pieces/B-Pawn.png')

    # king = pygame.image.load("pieces/B-King.png")
    # king = pygame.transform.scale(king, (100, 100))
    # rect = pygame.Rect(100, 100, 100 , 100)
    # rect_dragging = False

    king = King(screen, "pieces/B-King.png")






    pieces = []



    running = True
    while running:

        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False




            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 1:
            #         if rect.collidepoint(event.pos):
            #             old_x = rect.x
            #             old_y = rect.y
            #             rect_dragging = True
            #             mouse_x, mouse_y = event.pos
            #             offset_x = rect.x - mouse_x
            #             offset_y = rect.y - mouse_y
            # elif event.type == pygame.MOUSEBUTTONUP:
            #     if event.button == 1:
            #         rect.x = round(rect.x, -2)
            #         rect.y = round(rect.y, -2)
            #
            #         cords = get_cords(rect)
            #         if not is_valid(old_x, old_y, cords[0], cords[1]):
            #             rect.x = old_x
            #             rect.y = old_y
            #             rect.x = round(rect.x, -2)
            #             rect.y = round(rect.y, -2)
            #
            #         rect_dragging = False
            #
            # elif event.type == pygame.MOUSEMOTION:
            #     if rect_dragging:
            #         mouse_x, mouse_y = event.pos
            #         rect.x = mouse_x + offset_x
            #         rect.y = mouse_y + offset_y

        screen.fill((105, 105, 105))
        draw_board(screen)

        king.draw()





        pygame.display.update()

def draw_board(screen):

    color_1 = (90, 128, 85)
    color_2 = (227, 224, 200)

    current_color = color_1

    tiles = []
    for i in range(8):
        col = []
        for j in range(8):
            col.append(pygame.Rect(0,0,0,0))
        tiles.append(col)

    y = TILE_SIZE_PIXELS

    for i in range(8):
        x = TILE_SIZE_PIXELS
        for j in range(8):

            current_rect = pygame.Rect(x, y, TILE_SIZE_PIXELS, TILE_SIZE_PIXELS)

            tiles[i][j] = current_rect

            if current_color == color_1:
                current_color = color_2
            else:
                current_color = color_1

            pygame.draw.rect(screen, current_color, current_rect)



            x += TILE_SIZE_PIXELS

        if current_color == color_1:
            current_color = color_2
        else:
            current_color = color_1

        y += TILE_SIZE_PIXELS





    pass



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

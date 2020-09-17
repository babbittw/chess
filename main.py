# This is a sample Python script.

import pygame
import Piece
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

SCREEN_SIZE_PIXELS = 1000
TILE_SIZE_PIXELS = .1 * SCREEN_SIZE_PIXELS



def main():




    pygame.init()

    screen = pygame.display.set_mode((SCREEN_SIZE_PIXELS, SCREEN_SIZE_PIXELS))




    pieces_images = []



    #test = Piece(screen, pygame.image.load('pieces/B-Pawn.png'))

    pawn = pygame.image.load("pieces/B-Pawn.png")
    pawn = pygame.transform.scale(pawn, (100, 100))
    rect = pygame.Rect(100, 100, 100 , 100)
    rect_dragging = False

    running = True
    while running:

        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if rect.collidepoint(event.pos):
                        rect_dragging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = rect.x - mouse_x
                        offset_y = rect.y - mouse_y
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    rect.x = round(rect.x, -2)
                    rect.y = round(rect.y, -2)
                    rect_dragging = False

            elif event.type == pygame.MOUSEMOTION:
                if rect_dragging:
                    mouse_x, mouse_y = event.pos
                    rect.x = mouse_x + offset_x
                    rect.y = mouse_y + offset_y

        screen.fill((105, 105, 105))
        draw_board(screen)




        screen.blit(pawn, (rect.x, rect.y))



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

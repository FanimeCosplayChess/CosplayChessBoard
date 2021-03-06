import os
from argparse import ArgumentParser

import pygame
import numpy as np

from chess_pieces_defaults import pieces_dict, grid_dict
from get_csvs import get_images, get_moves

def main(args):
    dirname = os.path.dirname(__file__)

    pygame.init()

    pygame.font.init() # you have to call this at the start,
                       # if you want to use this module.

    FONT_SIZE = 30


    # Define Fonts

    myfont = pygame.font.SysFont('Comic Sans MS', 30)


    text_x = {}
    text_y = {}

    for i in range(8):
        text_x[i] = myfont.render(grid_dict['x'][i], False, (0, 0, 0))

    for j in range(8):
        text_y[j] = myfont.render(grid_dict['y'][j], False, (0, 0, 0))

    display_width = 800
    display_height = 600


    black = (50,50,50)
    white = (255,255,255)
    red = (255,0,0)

    car_width = 73


    if args.full:
        gameDisplay = pygame.display.set_mode((display_width,display_height),pygame.FULLSCREEN)
    else:
        gameDisplay = pygame.display.set_mode((display_width,display_height))

    pygame.display.set_caption('A bit Racey')
    clock = pygame.time.Clock()

    crashed = False


    def get_image(image_path, im_size = 50):
        img = pygame.image.load(image_path)

        img = pygame.transform.scale(img,(50,50))
        return img

    surf_dict =  {}
    image_dict = get_images()

    for k in pieces_dict.keys():

        filename = os.path.join(dirname, './images/'+image_dict[k].strip())
        surf_dict[k] = get_image(filename)

    piece_speed = 0


    p_x = 0
    p_y = 0

    # Get Moves as a list of x,y postions and a chess piece
    moves = get_moves()
    def game_loop():

        NUM_STEPS = 50
        game_state = "WAITING"
        x =  (display_width * 0.45)
        y = (display_height * 0.8)
        x_change = 0

        gameExit = False

        # Handle Input
        while not gameExit:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True

            #######################################################################
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if game_state != "MOVING":
                            cur_piece,(x_coord, y_coord) = moves.pop(0)
                            delta_x = pieces_dict[cur_piece].x_pos - x_coord
                            delta_y = pieces_dict[cur_piece].y_pos - y_coord
                            game_state = "MOVING"
            #######################################################################

            if game_state == "MOVING":

                pieces_dict[cur_piece].x_pos -= delta_x/NUM_STEPS
                pieces_dict[cur_piece].y_pos -= delta_y/NUM_STEPS
                if abs((pieces_dict[cur_piece].x_pos - x_coord)
                       +(pieces_dict[cur_piece].y_pos - y_coord)) < 2:


                    pieces_dict[cur_piece].x_pos = x_coord
                    pieces_dict[cur_piece].y_pos = y_coord

                    cur_piece = None
                    game_state = "AWAIT"

            #######################################################################

            # Draw Chessboard
            gameDisplay.fill(white)

            for i in range(8):
                for j in range(8):
                    if (i+j) % 2 ==0:
                        pygame.draw.rect(gameDisplay,black,(50+i*50,50+j*50,50,50))

            # Draw Grid
            for i in range(8):
                gameDisplay.blit(
                                text_x[i],
                                (50+i*50,20)
                                )

            for j in range(8):
                gameDisplay.blit(
                                 text_y[j],
                                 (20,50+j*50)
                                )

            # Draw Pieces
            for piece_key, piece_obj in pieces_dict.items():

                gameDisplay.blit(surf_dict[piece_key],(
                                                        piece_obj.x_pos,
                                                        piece_obj.y_pos))

            pygame.display.update()
            clock.tick(60)

    game_loop()
    pygame.quit()
    quit()

if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument('--full', '-f', action='store_true')
    args = parser.parse_args()
    main(args=args)

import csv
import os
import re


def get_images():
    image_dict = {}

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, './csvs/image_map.csv')
    with open(filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            image_dict[row[0]] = row[1]

    return image_dict




def parse_moves(chess_moves):
    # Input moves in chessboard format and output them in screenformat
    moves = []
    for piece, coord in chess_moves:
        #First check all moves are strings  and are in chess piece format
        if type(coord) != str  or not re.match("[A-H][1-8]",coord) :

            print ("INVALID DATA FORMAT. Make sure all moves are given as strings of chess coordinates")
            quit()

        x_pos = (ord(coord[0])- 65)*50+50
        y_pos = int(coord[1])*50
        moves.append((piece,(x_pos, y_pos)))

    # First check if all of the coordinates are in the correct format and quit
    # if they are not
    return moves

def get_moves():

    chess_moves = []

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, './csvs/moves.csv')
    with open(filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            chess_moves.append((row[0],row[1].strip()))

    moves = parse_moves(chess_moves=chess_moves)

    return moves

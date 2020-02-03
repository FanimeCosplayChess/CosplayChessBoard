import csv
import os

def get_images():
    image_dict = {}

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, './csvs/image_map.csv')
    with open(filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            image_dict[row[0]] = row[1]

    return image_dict

def get_moves():

    moves_list = []

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, './csvs/moves.csv')
    with open(filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            moves_list.append((row[0],(int(row[1].strip()),int(row[2].strip()))))

    return moves_list

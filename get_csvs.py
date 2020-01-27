import csv

def get_images():
    image_dict = {}

    with open('./csvs/image_map.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            image_dict[row[0]] = row[1]

    return image_dict

def get_moves():

    moves_list = []

    with open('./csvs/moves.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            moves_list.append((row[0],(int(row[1].strip()),int(row[2].strip()))))

    return moves_list




class ChessPiece(object):

    def __init__(
                 self,
                 init_x,
                 init_y,
                 team,
                 piece_type,
                ):

        self.x_pos = init_x
        self.y_pos = init_y
        self.team = team
        self.piece_type = piece_type



    def get_pos(self):
        return self.x_pos, self.y_pos



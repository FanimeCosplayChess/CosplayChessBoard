from chesspiece import ChessPiece

x_off = 50
y_off = 50

pieces_dict = {
                'w_rook_1':ChessPiece(
                                    init_x = 0+x_off,
                                    init_y = 0+y_off,
                                    team = 'white',
                                    piece_type = 'rook'
                                  ),

                'w_knight_1':ChessPiece(
                                    init_x = 0+x_off,
                                    init_y = 50+y_off,
                                    team = 'white',
                                    piece_type = 'rook'
                                  ),

                'w_bishop_1':ChessPiece(
                                    init_x = 0+x_off,
                                    init_y = 100+y_off,
                                    team = 'white',
                                    piece_type = 'rook'
                                  ),

                'w_queen':ChessPiece(
                                    init_x = 0+x_off,
                                    init_y = 150+y_off,
                                    team = 'white',
                                    piece_type = 'rook'
                                  ),

                'w_king':ChessPiece(
                                    init_x = 0+x_off,
                                    init_y = 200+y_off,
                                    team = 'white',
                                    piece_type = 'rook'
                                  ),

                'w_bishop_2':ChessPiece(
                                    init_x = 0+x_off,
                                    init_y = 250+y_off,
                                    team = 'white',
                                    piece_type = 'rook'
                                  ),

                'w_knight_2':ChessPiece(
                                    init_x = 0+x_off,
                                    init_y = 300+y_off,
                                    team = 'white',
                                    piece_type = 'rook'
                                  ),

                'w_rook_2':ChessPiece(
                                    init_x = 0+x_off,
                                    init_y = 350+y_off,
                                    team = 'white',
                                    piece_type = 'rook'
                                  ),

                'w_pawn_1':ChessPiece(
                                    init_x = 50+x_off,
                                    init_y = 0+y_off,
                                    team = 'white',
                                    piece_type = 'rook'
                                  ),

                'w_pawn_2':ChessPiece(
                                    init_x = 50+x_off,
                                    init_y = 50+y_off,
                                    team = 'white',
                                    piece_type = 'rook'
                                  ),

                'w_pawn_3':ChessPiece(
                                    init_x = 50+x_off,
                                    init_y = 100+y_off,
                                    team = 'white',
                                    piece_type = 'rook'
                                  ),

                'w_pawn_4':ChessPiece(
                                    init_x = 50+x_off,
                                    init_y = 150+y_off,
                                    team = 'white',
                                    piece_type = 'rook'
                                  ),

                'w_pawn_5':ChessPiece(
                                    init_x = 50+x_off,
                                    init_y = 200+y_off,
                                    team = 'white',
                                    piece_type = 'rook'
                                  ),

                'w_pawn_6':ChessPiece(
                                    init_x = 50+x_off,
                                    init_y = 250+y_off,
                                    team = 'white',
                                    piece_type = 'rook'
                                  ),

                'w_pawn_7':ChessPiece(
                                    init_x = 50+x_off,
                                    init_y = 300+y_off,
                                    team = 'white',
                                    piece_type = 'rook'
                                  ),

                'w_pawn_8':ChessPiece(
                                    init_x = 50+x_off,
                                    init_y = 350+y_off,
                                    team = 'white',
                                    piece_type = 'rook'
                                  ),

                'b_rook_1':ChessPiece(
                                    init_x = 350+x_off,
                                    init_y = 0+y_off,
                                    team = 'white',
                                    piece_type = 'rook'
                                  ),

                'b_knight_1':ChessPiece(
                                    init_x = 350+x_off,
                                    init_y = 50+y_off,
                                    team = 'white',
                                    piece_type = 'rook'
                                  ),

                'b_bishop_1':ChessPiece(
                                    init_x = 350+x_off,
                                    init_y = 100+y_off,
                                    team = 'white',
                                    piece_type = 'rook'
                                  ),

                'b_queen':ChessPiece(
                                    init_x = 350+x_off,
                                    init_y = 150+y_off,
                                    team = 'white',
                                    piece_type = 'rook'
                                  ),

                'b_king':ChessPiece(
                                    init_x = 350+x_off,
                                    init_y = 200+y_off,
                                    team = 'white',
                                    piece_type = 'rook'
                                  ),

                'b_bishop_2':ChessPiece(
                                    init_x = 350+x_off,
                                    init_y = 250+y_off,
                                    team = 'white',
                                    piece_type = 'rook'
                                  ),

                'b_knight_2':ChessPiece(
                                    init_x = 350+x_off,
                                    init_y = 300+y_off,
                                    team = 'white',
                                    piece_type = 'rook'
                                  ),

                'b_rook_2':ChessPiece(
                                    init_x = 350+x_off,
                                    init_y = 350+y_off,
                                    team = 'white',
                                    piece_type = 'rook'
                                  ),

                'b_pawn_1':ChessPiece(
                                    init_x = 300+x_off,
                                    init_y = 0+y_off,
                                    team = 'white',
                                    piece_type = 'rook'
                                  ),

                'b_pawn_2':ChessPiece(
                                    init_x = 300+x_off,
                                    init_y = 50+y_off,
                                    team = 'white',
                                    piece_type = 'rook'
                                  ),

                'b_pawn_3':ChessPiece(
                                    init_x = 300+x_off,
                                    init_y = 100+y_off,
                                    team = 'white',
                                    piece_type = 'rook'
                                  ),

                'b_pawn_4':ChessPiece(
                                    init_x = 300+x_off,
                                    init_y = 150+y_off,
                                    team = 'white',
                                    piece_type = 'rook'
                                  ),

                'b_pawn_5':ChessPiece(
                                    init_x = 300+x_off,
                                    init_y = 200+y_off,
                                    team = 'white',
                                    piece_type = 'rook'
                                  ),

                'b_pawn_6':ChessPiece(
                                    init_x = 300+x_off,
                                    init_y = 250+y_off,
                                    team = 'white',
                                    piece_type = 'rook'
                                  ),

                'b_pawn_7':ChessPiece(
                                    init_x = 300+x_off,
                                    init_y = 300+y_off,
                                    team = 'white',
                                    piece_type = 'rook'
                                  ),

                'b_pawn_8':ChessPiece(
                                    init_x = 300+x_off,
                                    init_y = 350+y_off,
                                    team = 'white',
                                    piece_type = 'rook'
                                  )
                }

grid_dict = {
            'x':{
                 0:'a',
                 1:'b',
                 2:'c',
                 3:'d',
                 4:'e',
                 5:'f',
                 6:'g',
                 7:'h',
            },
            'y':{
                 0:'1',
                 1:'2',
                 2:'3',
                 3:'4',
                 4:'5',
                 5:'6',
                 6:'7',
                 7:'8',
            }
    }

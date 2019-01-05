ROWS_NUMBER = 6
COLS_NUMBER = 7
class Board:

    def __init__(self):
        self.board = self.build_board()

    def build_board(self):
        board = []
        for i in range(ROWS_NUMBER):
            row = []
            for i in range(COLS_NUMBER):
                row.append("*")
            board.append(row)
        return board

    def insert_player(self, disc, col):
        # if col<0 or col>COLS_NUMBER:
        #     return False
        for row in range(ROWS_NUMBER, 0, -1):
            if self.board[row][col] != "*":
                self.board[row][col] = disc.get_number()
        #         return True
        # return False

    def get_board(self):
        return self.board

    def get_num_rows(self):
        return ROWS_NUMBER

    def get_num_cols(self):
        return COLS_NUMBER

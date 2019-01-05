
from board import Board
from disc import Disc
NAME_REQUEST = "enter tow player names seperated with space: "
class Game:#todo this class was gaven

    def __init__(self):#todo this function name was given
        self.board = Board()
        # name1 = input(NAME_REQUEST)#TODO unpack names
        self.disc1 = Disc(name, 1, "red")#TODO check if need a name or digit
        self.disc1 = Disc(name, 2, "blue")
        self.cur_player = 1
        pass

    def make_move(self, column):#todo check if cullapses
        try:
            self.board.insert_player(disc, col)
        except:
            raise ValueError("Illigal move")


    def get_winner(self):#todo this function name was given, #todo get done!
        found = set()
        board = self.board.get_board()
        for row in board:
            str_row = "".join(row)
            if "1111" in str_row:
                return 1
            if "0000" in str_row:
                return 0
        elif "0000" in found:
            return 0
        fliped = self.flip_board()
        for row in fliped:
            found.add("".join(row))
        if "1111" in found:
            return 1
        elif "0000" in found:
            return 0


    def flip_board(self):#todo get done!
        fliped = []
        board = self.board.get_board()
        for i in range(self.board.get_num_rows()):
            row = []
            for j in range(self.board.get_num_cols()):
                row.append(board[i][j])
            fliped.append(row)
        return fliped

    def get_player_at(self, row, col):#todo this function name was given
        try:
            contant = self.board.get_board()[row][col]
            if contant == 1:
                return 1
            elif contant == 0:
                return 0
            else:
                return None
        except:
            raise ValueError("Ilegal location")

    def get_current_player(self):#todo this function name was given
        return self.cur_player

if __name__ == '__main__':
    a = [1,2,3,4,5]
    print(m for m in a)

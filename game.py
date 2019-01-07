
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
    
    #---------------------------------------------------------------
    
def find_row_or_col_winner(matrix, row, col):
    if row == 1:
        check1 = len(matrix[0])
        check2 = len(matrix)
    else:
        check1 = len(matrix)
        check2 = len(matrix[0])
    addX = 0
    addY = 0
    print(check1)
    for i in range(check1):
        row_index = 0
        col_index = 0
        string_check = ""
        for j in range(check2):
            print("check row", row_index, "check col:", col_index)

            string_check += str(matrix[row_index + addY][col_index + addX])
            row_index += row
            col_index += col
        if col == 0:
            addX += 1
        else:
            addY += 1
        # todo to add to return tup or list that shows from what location the winning
        if "rrrr" in string_check:
            return "r", (i, string_check.find("r"))
        if "yyyy" in string_check:
            return "y", ((i, string_check.find("y")))
    return "n", (-1, -1)  # defualt value of index of not found what we were looking for as excepted in the world


a = [["x", "r", "x", "x", "x", "x", "x"], ["x", "r", "x", "x", "x", "x", "x"], ["x", "r", "x", "x", "x", "x", "x"],
     ["x", "r", "x", "x", "x", "x", "x"], ["x", "x", "x", "x", "x", "x", "x"], ["x", "x", "x", "x", "x", "x", "x"]]
for i in a:
    print(i)

print(find_row_or_col_winner(a, 1, 0))


def side_checks(matrix, orientaion):
    for i in range(3):
        if orientaion == 1:
            j = len(matrix[i]) - 1
            while (j > len(matrix) - 4):
                # todo to add to return tup or list that shows from what location the winning
                if (matrix[i][j] == matrix[i + 1][j - 1] == matrix[i + 2][j - 2] == matrix[i + 3][
                    j - 3] == "r"):
                    return "r" ,(i,j)#to check if returns the currect possition
                elif (matrix[i][j] == matrix[i + 1][j - 1] == matrix[i + 2][j - 2] == matrix[i + 3][
                    j - 3] == "yellow"):
                    return "y", (i,j)#to check if returns the currect possition
                j -= 1
        else:
            for j in range(3):
                if (matrix[i][j] == matrix[i + 1][j + 1] == matrix[i + 2][j + 2] == matrix[i + 3][
                    j + 3] == "r"):
                    return "r" , (i,j)#to check if returns the currect possition
                elif (matrix[i][j] == matrix[i + 1][j + 1] == matrix[i + 2][j + 2] == matrix[i + 3][
                    j + 3] == "yellow"):
                    return "y", (i, j)  # to check if returns the currect possition

    return "n",(-1,-1) #possition


#------------------------------------------------------------------------------------------------
    
    
    

if __name__ == '__main__':
    a = [1,2,3,4,5]
    print(m for m in a)

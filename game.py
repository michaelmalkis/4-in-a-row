from board import Board
from disc import Disc

NAME_REQUEST = "enter tow player names seperated with space: "


class Game:  # todo this class was gaven

    def __init__(self):  # todo this function name was given
        self.board = Board()
        self.play_board = self.board.get_board()
        # name1 = input(NAME_REQUEST)#TODO unpack names
        # self.disc1 = Disc(name, 1, "red")  # TODO check if need a name or digit
        # self.disc1 = "red"
        self.cur_player = 1
        self.players_info = {1: ["r", "defualt name"], 2: ["y", "defualt name"]}  # add name
        self.pos_change = (-1, -1)
        self.winner = []

    def make_move(self, column):  # todo check if callapses
        for i in range(self.board.get_num_cols()):
            if self.get_player_at(0, i) == None:
                break
        else:
            raise ValueError("Illegal location1111")
        if column < 0 or column > self.board.get_num_cols() - 1 or not self.make_move_check(column):
            raise ValueError("Illegal location")
        row = self.pos_change[0]  # make sure it works or it ruins something
        self.play_board[row][column] = self.cur_player  # todo changed cur player
        self.cur_player = 3 - self.cur_player  # watch and learn bitchess!!!

    def make_move_check(self, col):
        # if self.board[0][col] == "1" or self.p[0][col].fill == "yellow":
        row_to_add = 0
        if self.get_player_at(0, col) != None:  # wil call board at col row
            return False
        for row in range(self.board.get_num_rows()):
            if self.get_player_at(row, col) != None:
                self.pos_change = (row - 1, col)
                return True
            # elif row == self.board.get_num_rows() - 1:
        self.pos_change = (self.board.get_num_rows() - 1, col)
        return True

    def get_winner(self):  # todo this function name was given, #todo get done!
        check_cols = self.find_row_or_col_winner(1, 0)
        # todo check if it runs on rows
        print("check_cols:",check_cols)#todo remove
        if check_cols[0] != "n":
            self.winning_pos(check_cols[1], 0, 1)
            print("col found result:", self.find_row_or_col_winner(1, 0), "starting location", self.winner)
            return check_cols[0]
        # todo to check if it runs in col
        check_rows = self.find_row_or_col_winner(0, 1)
        print("check_row:",check_rows)
        if check_rows[0] != "n":
            self.winning_pos(check_rows[1], 1, 0)
            print("col found result:", self.find_row_or_col_winner(0, 1), "starting location", self.winner)
            return check_rows[0]

        # todo to check if it runs on sides the currect way
        # todo goes up and to the right
        check_orientaion1 = self.side_checks(1)
        print("check_orientaion1:",check_orientaion1)
        if check_orientaion1[0] != "n":
            self.winning_pos(check_orientaion1[1], -1, 1)
            print("sides up rigt-result:",self.side_checks(1),"starting location",self.winner)
            return check_orientaion1[0]

        # todo to check if it runs on sides the currect way
        # todo goes down and to the right
        check_orientaion = self.side_checks(0)
        print("check_orientaion:",check_orientaion)
        if check_orientaion[0] != "n":
            self.winning_pos(check_orientaion[1], 1, 1)
            print("sides up rigt-result:", self.side_checks(0), "starting location", self.winner)
            return check_orientaion[0]

    def winning_pos(self, winning_loc, x_move, y_move):
        y_loc, x_loc = winning_loc
        for i in range(4):
            self.winner.append((y_loc, x_loc))
            x_loc += x_move
            y_loc += y_move

    def get_pos_change(self):
        return self.pos_change

    def get_players(self):
        return self.players_info

    # def flip_board(self):  # todo get done!
    #     fliped = []
    #     board = self.board.get_board()
    #     for i in range(self.board.get_num_rows()):
    #         row = []
    #         for j in range(self.board.get_num_cols()):
    #             row.append(board[i][j])
    #         fliped.append(row)
    #     return fliped

    def get_player_at(self, row, col):  # todo this function name was given
        # print(row,",",col)
        try:
            possition = self.play_board[row][col]
            return possition if possition != 0 else None
            # contant = self.board.get_board()[row][col]
            # if contant == 1:
            #     return 1
            # elif contant == 0:
            #     return 0
            # else:
            #     return None
        except:
            raise ValueError("Ilegal location")

    def get_current_player(self):  # todo this function name was given
        return self.cur_player

    # ---------------------------------------------------------------

    def find_row_or_col_winner(self, run_on_x, run_on_y):
        matrix = self.play_board
        if run_on_x == 1:
            check1 = len(matrix[0])
            check2 = len(matrix)
        else:
            check1 = len(matrix)
            check2 = len(matrix[0])
        addX = 0
        addY = 0
        string_check = ""
        save_i = 0
        for i in range(check1):
            save_i = i
            row_index = 0
            col_index = 0
            string_check = ""
            for j in range(check2):
                string_check += str(matrix[row_index + addY][col_index + addX])
                row_index += run_on_x
                col_index += run_on_y

            addX += run_on_x
            addY += run_on_y

            # if run_on_y == 0:
            #     addX += 1
            # else:
            #     addY += 1
            if run_on_x == 1:
                if "1111" in string_check:  # todo to change to 1 or 2
                    return "1", (string_check.find("1111"), save_i)
                if "2222" in string_check:  # todo to change to 1 or 2
                    return "2", ((string_check.find("2222"), save_i))
            else:
                if "1111" in string_check:  # todo to change to 1 or 2
                    return "1", (save_i, string_check.find("1111"))
                if "2222" in string_check:  # todo to change to 1 or 2
                    return "2", (save_i, (string_check.find("2222")))
        return "n", (-1, -1)  # defualt value of index of not found what we were looking for as excepted in the world

    def side_checks(self, orientaion):
        matrix=self.play_board
        for i in range(3):
            if orientaion == 1:
                j = len(matrix[i]) - 1
                while (j > len(matrix) - 4):
                    if (matrix[i][j] == matrix[i + 1][j - 1] == matrix[i + 2][j - 2] == matrix[i + 3][
                        j - 3] == 1):
                        return "1", (i, j)  # to check if returns the currect possition
                    elif (matrix[i][j] == matrix[i + 1][j - 1] == matrix[i + 2][j - 2] == matrix[i + 3][
                        j - 3] == 2):
                        return "2", (i, j)  # to check if returns the currect possition
                    # print(i,"-",j ,"|", i + 1,"-",j - 1,"|" ,i + 2,"-",j - 2,"|" ,i + 3,"-", j - 3)
                    j -= 1
            else:
                for j in range(4):
                    if (matrix[i][j] == matrix[i + 1][j + 1] == matrix[i + 2][j + 2] == matrix[i + 3][
                        j + 3] == 1):
                        return "1", (i, j)  # to check if returns the currect possition
                    elif (matrix[i][j] == matrix[i + 1][j + 1] == matrix[i + 2][j + 2] == matrix[i + 3][
                        j + 3] == 2):
                        return "2", (i, j)  # to check if returns the currect possition
                    print(i, "-", j, "|", i + 1, "-", j + 1, "|", i + 2, "-", j + 2, "|", i + 3, "-", j + 3)
        return "n", (-1, -1)  # possition


def find_row_or_col_winner(matrix, run_on_x, run_on_y):
    # matrix = self.play_board
    if run_on_x == 1:
        check1 = len(matrix[0])
        check2 = len(matrix)
    else:
        check1 = len(matrix)
        check2 = len(matrix[0])
    addX = 0
    addY = 0
    print(check1)
    string_check = ""
    save_i = 0
    for i in range(check1):
        save_i = i
        row_index = 0
        col_index = 0
        string_check = ""
        for j in range(check2):

            string_check += str(matrix[row_index + addY][col_index + addX])
            row_index += run_on_x
            col_index += run_on_y

        addX += run_on_x
        addY += run_on_y

        # if run_on_y == 0:
        #     addX += 1
        # else:
        #     addY += 1

        if run_on_x == 1:
            if "1111" in string_check:  # todo to change to 1 or 2
                return "1", (string_check.find("1111"), save_i)
            if "2222" in string_check:  # todo to change to 1 or 2
                return "2", ((string_check.find("2222"), save_i))
        else:
            if "1111" in string_check:  # todo to change to 1 or 2
                return "1", (save_i, string_check.find("1111"))
            if "2222" in string_check:  # todo to change to 1 or 2
                return "2", (save_i, (string_check.find("2222")))
    return "n", (-1, -1)  # defualt value of index of not found what we were looking for as excepted in the world


# --------------------------------------------------------------

a = [["0", "1", "0", "0", "1", "1", "1"],
     ["0", "1", "0", "0", "0", "0", "0"],
     ["0", "1", "0", "0", "0", "0", "0"],
     ["0", "1", "0", "0", "0", "0", "0"],
     ["0", "0", "2", "2", "2", "2", "0"],
     ["0", "0", "0", "0", "0", "0", "0"]]

# print(a[0][3], 33333333333333)
# print(find_row_or_col_winner(a, 0, 1))
if __name__ == '__main__':
    pass
    # a = [1, 2, 3, 4, 5]
    # print(m for m in a)

# ------------------------------------------------------------------------------------------------

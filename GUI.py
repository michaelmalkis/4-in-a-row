from tkinter import *
from tkinter import font
from game import *


class Info(Frame):
    def __init__(self, master=None):
        Frame.__init__(self)
        self.configure(width=500, height=100)
        writing_profile = font.Font(self, size=25, family='Arial')
        self.t = Label(self, text="connect 4", font=writing_profile, bg="cyan", fg="purple2")
        self.t.grid(sticky=NSEW, pady=10)


class HolesInBoard(object):
    def __init__(self, x, y, can, fill="grey12", bg="red"):
        self.can = can
        self.x = x
        self.y = y
        self.fill = fill

        self.tour = 1

        self.r = 30
        self.HolesInBoard = self.can.create_oval(self.x + 10, self.y + 10, self.x + 61, self.y + 61, fill=fill,
                                                 outline="blue")

    def changeCollor(self, fill):
        self.can.itemconfigure(self.HolesInBoard, fill=fill)
        self.fill = fill

    def changeCollorWinner(self, fill):
        self.can.itemconfigure(self.HolesInBoard, fill=fill, outline="lime green", width=5)
        # Frame(root, highlightbackground="green", highlightcolor="green", highlightthickness=1, width=100, height=100, bd= 0)

        self.fill = fill


class Terrain(Canvas):

    def __init__(self, master=None):
        Canvas.__init__(self)
        self.configure(width=500, height=400, bg="blue")
        self.game = Game()
        self.player = 1
        self.fill = "yellow"
        self.p = []
        for i in range(0, 340, int(400 / 6)):
            list_range = []
            for j in range(0, 440, int(500 / 7)):
                list_range.append(HolesInBoard(j, i, self))

            self.p.append(list_range)
        self.bind("<Button-1>", self.detCol)

    def detCol(self, event):
        col = int(event.x / 71)
        old_pos = self.game.get_pos_change()
        old_player = self.game.get_current_player()
        # print(col)
        self.game.make_move(col)
        if self.game.get_pos_change() == old_pos:
            return
        # cur_player = self.game.get_current_player()
        info.t.config(text=self.game.get_players()[old_player][0])
        color = "red" if old_player == 2 else "yellow"
        row, col = self.game.get_pos_change()
        self.p[row][col].changeCollor(color)
        winner = self.game.get_winner()
        print(winner)
        if winner == "1":
            print("yellow won")
            self.winner(self.game.winner, "gold2")
        if winner == "2":
            print("red won")
            self.winner(self.game.winner, "red3")

        # row_save = 0
        # for row in range(len(self.p)):
        #     if self.p[0][col].fill == "red" or self.p[0][col].fill == "yellow":
        #         return
        #
        #     if self.p[row][col].fill == "red" or self.p[row][col].fill == "yellow":
        #         self.p[row - 1][col].changeCollor(self.fill)
        #         row_save = row
        #
        #         break
        #
        #     elif row == len(self.p) - 1:
        #         self.p[row][col].changeCollor(self.fill)
        #         row_save = row
        #
        #         break
        # print(row_save, " -", col)
        # if cur_p ==
        # if self.player == 1:
        #     self.player = 2
        #     info.t.config(text="red make a move")
        #     self.fill = "red"
        #
        # else:
        #     # self.player == 2  # or only else
        #     self.player = 1
        #     info.t.config(text="yellow make a move")
        #     self.fill = "yellow"

        # self.winner((2, 2), (0, 1), "red2")

    def winner(self, pos_winner, collor):
        print(pos_winner)
        for i in pos_winner:
            self.p[i[0]][i[1]].changeCollorWinner(collor)


root = Tk()
root.geometry("500x550")
root.title("The most epic game ever!!!!")
# ---------- collors
root["bg"] = "cyan"
# root.resizable(False, False)

info = Info(root)
info.grid(row=0, column=0)

t = Terrain(root)
t.grid(row=1, column=0)


# ------------------------------------------------------------------------------
def rein():
    global info
    info.t.config(text="")

    info = Info(root)
    info.grid(row=0, column=0)

    t = Terrain(root)
    t.grid(row=1, column=0)


Button(root, text="options", bg="pink", command=rein).grid(row=2, column=0, pady=10)

root.mainloop()

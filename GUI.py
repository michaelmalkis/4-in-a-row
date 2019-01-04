from tkinter import *
from tkinter import font
from collors import Collors


class Info(Frame):
    def __init__(self, master=None):
        Frame.__init__(self)
        self.configure(width=500, height=100)
        writing_profile = font.Font(self, size=20, family='Arial')
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


class Terrain(Canvas):

    def __init__(self, master=None):
        Canvas.__init__(self)
        self.configure(width=500, height=400, bg="blue")

        self.player = 1
        self.fill = "yellow"
        self.p = []
        self.perm = True
        for i in range(0, 340, int(400 / 6)):
            list_range = []
            for j in range(0, 440, int(500 / 7)):
                list_range.append(HolesInBoard(j, i, self))

            self.p.append(list_range)

        self.bind("<Button-1>", self.detCol)

    def detCol(self, event):
        if self.perm:
            col = int(event.x / 71)
            # lig = 0

            lig = 0
            # while lig < len(self.p):
            for row in range(len(self.p)):
                if self.p[0][col].fill == "red" or self.p[0][col].fill == "yellow":
                    return

                if self.p[row][col].fill == "red" or self.p[row][col].fill == "yellow":
                    self.p[row - 1][col].changeCollor(self.fill)
                    break

                elif row == len(self.p) - 1:
                    self.p[row][col].changeCollor(self.fill)
                    break

                # if self.p[row][col].fill != "red" and self.p[lig][col].fill != "yellow":
                # lig += 1

            if self.player == 1:
                self.player = 2
                info.t.config(text="red make a move")
                self.fill = "red"

            elif self.player == 2:  # or only else
                self.player = 1
                info.t.config(text="yellow make a move")
                self.fill = "yellow"


root = Tk()
root.geometry("500x550")
root.title("The most epic game ever!!!!")
# ---------- collors
root["bg"] = "cyan"
root.resizable(False, False)

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


Button(root, text="put bottons here", bg="pink", command=rein).grid(row=2, column=0, pady=30)

root.mainloop()

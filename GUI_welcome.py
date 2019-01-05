import tkinter as tk
import random
from GUIDefaults import *
class Connect4GUIStartup(object):
    # Performs the 'preamble' for running Connect4 by asking the user(s) for various details about their game.
    # Usage is:
    # c4 = Connect4GUIStartup()
    # c4.start() # <-- mainloop is called in here, so we won't print the next statement till it closes
    # values = c4.outd # <-- Values that the user(s) entered. Empty dict -> fail/they hit quit.
    def __init__(self, **kwargs):
        self.outd = None
        self.root = tk.Tk()
        self.root.configure(background=DEFAULT_WIDGET_BG)
        self.title_lab = tk.Label(master=self.root, text="Welcome to "\
                                  "Connect 4", font=DEFAULT_FONT,
                                  background=DEFAULT_WIDGET_BG)
        self.title_lab.grid(row=0, column=0, sticky=tk.EW, columnspan=4, padx=[50, 50], pady=[20, 20])

        self.players_frame = tk.Frame(master=self.root, background=DEFAULT_WIDGET_BG)
        self.players_frame.grid(row=3, column=0, sticky=tk.EW, columnspan=4, padx=[10, 10], pady=[10, 0])
        self.player1_name = tk.StringVar(master=self.players_frame)
        self.player1_name.trace("w", self.limit_player_len)
        self.player1_entry = tk.Entry(master=self.players_frame, textvariable=self.player1_name, font=DEFAULT_FONT,
                                      background=DEFAULT_ENTRY_COLOR, width=ENTRY_WIDTH)
        self.player1_entry.grid(row=0, column=1, sticky=tk.NW)
        self.cpu1_var = tk.IntVar(master=self.players_frame, value=0)
        self.cpu1_box = tk.Checkbutton(master=self.players_frame, text="CPU?", variable=self.cpu1_var,
                                       background=DEFAULT_WIDGET_BG, font=DEFAULT_FONT,
                                       activebackground=DEFAULT_WIDGET_BG, command=self.cpu1_check)
        self.cpu1_box.grid(row=0, column=2, sticky=tk.NSEW)

        self.player2_lab = tk.Label(master=self.players_frame, text="Player 2:", font=DEFAULT_FONT,
                                    background=DEFAULT_WIDGET_BG)
        self.player2_lab.grid(row=1, column=0, sticky=tk.NE)
        self.player2_name = tk.StringVar(master=self.players_frame)
        self.player2_name.trace("w", self.limit_player_len)
        self.player2_entry = tk.Entry(master=self.players_frame, textvariable=self.player2_name, font=DEFAULT_FONT,
                                      background=DEFAULT_ENTRY_COLOR, width=ENTRY_WIDTH)
        self.player2_entry.grid(row=1, column=1, sticky=tk.NW)

        self.cpu2_var = tk.IntVar(master=self.players_frame, value=0)
        self.cpu2_box = tk.Checkbutton(master=self.players_frame, text="CPU?", variable=self.cpu2_var,
                                       background=DEFAULT_WIDGET_BG, font=DEFAULT_FONT,
                                       activebackground=DEFAULT_WIDGET_BG, command=self.cpu2_check)
        self.cpu2_box.grid(row=1, column=2, sticky=tk.NSEW)

        self.confirm_button = tk.Button(master=self.root, text="Confirm", font=DEFAULT_FONT,
                                        background=DEFAULT_WIDGET_BG, command=self.confirm,
                                        activebackground=DEFAULT_HIGHLIGHT_COLOR)
        self.confirm_button.grid(row=4, column=3, sticky=tk.N)

        self.quit_button = tk.Button(master=self.root, text="Quit", font=DEFAULT_FONT,
                                     background=DEFAULT_WIDGET_BG, command=self.root.destroy,
                                     activebackground=DEFAULT_HIGHLIGHT_COLOR)
        self.quit_button.grid(row=4, column=2, sticky=tk.N)
        self.start()
        return

    def limit_player_len(self, *args):#TODO ADD WHILE KEY IS PRESSED
        p1name = self.player1_name.get()
        p2name = self.player2_name.get()
        n = NAME_LIMIT
        if len(p1name) > n: self.player1_name.set(p1name[:n])
        if len(p2name) > n: self.player2_name.set(p2name[:n])
        return

    def confirm(self):
        #DESTROY AND CALL SECOND GUI
        pass

    def cpu1_check(self):
        if self.cpu1_var.get():
            name = RANDOM_NAMES1[random.randint(0,1)]
            while name in [self.player1_name.get(), self.player1_name.get()]:
                name = RANDOM_NAMES1[random.randint(0,1)]
            self.player1_name.set(RANDOM_NAMES1[random.randint(0,1)])
            self.player1_entry.config(state="disabled")
        else:
            self.player1_entry.config(state="normal")
        return

    def cpu2_check(self):
        if self.cpu2_var.get():
            name = RANDOM_NAMES2[random.randint(0,1)]
            while name in [self.player1_name.get(), self.player2_name.get()]:
                name = RANDOM_NAMES2[random.randint(0,1)]
            self.player2_name.set(RANDOM_NAMES2[random.randint(0,1)])
            self.player2_entry.config(state="disabled")
        else:
            self.player2_entry.config(state="normal")
        return

    def start(self):
        self.root.resizable(False, False)
        self.root.mainloop()
        return

if __name__ == "__main__":
    setup_vars = {}
    while True:
        setup = Connect4GUIStartup(**setup_vars)
        setup_vars = setup.outd
        if setup_vars is None:
            break
import mastermind
from tkinter import *
from tkinter import ttk


# self.__root
class Interface:
    def __init__(self):
        self.__odpowiedzi_usun = []
        self.__game = mastermind.gameMastermind()
        self.__root = Tk()
        self.__root.title("Mastermind")
        self.__root.geometry("{}x{}".format(1200, 800))

        # two main columns
        self.__left_side = ttk.Frame(self.__root)
        self.__right_side = ttk.Frame(self.__root)

        self.__left_top_frame = ttk.Frame(self.__left_side)
        self.__left_bottom_frame = ttk.Frame(self.__left_side)

    def interfaceDraw(self):
        self.__root.rowconfigure(0, weight=1)
        self.__root.columnconfigure([0, 1], weight=1)

        self.__left_side.grid(row=0, column=0)
        self.__right_side.grid(row=0, column=1)

        # left side wit entry and buttons
        self.__left_side.rowconfigure([0, 1], weight=1)
        self.__left_side.columnconfigure(0, weight=1)

        self.__left_top_frame.grid(row=0, column=0)
        self.__left_bottom_frame.grid(row=1, column=0)

        # entry
        self.__left_top_frame.rowconfigure([0, 1], weight=1)
        self.__left_top_frame.columnconfigure(0, weight=1)
        entry_var = StringVar()
        entry_var.set("")
        Entry(
            self.__left_top_frame,
            textvariable=entry_var,
            font=("calibre", 20, "normal"),
        ).grid(row=1, column=0)

        self.__left_bottom_frame.rowconfigure(0, weight=1, minsize=70)
        self.__left_bottom_frame.columnconfigure([0, 1, 2], weight=1)

        self.__proby = ttk.Label(
            self.__left_top_frame,
            text="",
            font=("calibre", 20, "normal"),
        )
        self.__proby.grid(row=0, column=0)

        # przyciski
        ttk.Button(
            self.__left_bottom_frame,
            text="Sprawdź",
            command=lambda: self.writeAnswers(
                self.__game.userInputGuess(entry_var.get())
            ),
        ).grid(column=0, row=0)
        ttk.Button(
            self.__left_bottom_frame,
            text="Oszust",
            command=lambda: self.oszust(),
        ).grid(column=1, row=0)
        ttk.Button(
            self.__left_bottom_frame,
            text="Reset",
            command=lambda: self.resetGame(),
        ).grid(column=2, row=0)

        # answers column
        self.__right_side.rowconfigure([x for x in range(13)], weight=1, minsize=46)
        self.__right_side.columnconfigure([x for x in range(3)], weight=1, minsize=100)
        ttk.Label(
            self.__right_side,
            text="Właściwe |",
            font=("calibre", 18, "normal"),
        ).grid(row=0, column=0)
        ttk.Label(
            self.__right_side,
            text=" Odpowiedzi ",
            font=("calibre", 18, "normal"),
        ).grid(row=0, column=1)
        ttk.Label(
            self.__right_side,
            text="| Niewłaściwe",
            font=("calibre", 18, "normal"),
        ).grid(row=0, column=2)

        self.__root.mainloop()

    def writeAnswers(self, list):
        if list == -1:
            self.__proby.grid_remove()
            self.__proby = ttk.Label(
                self.__left_top_frame,
                text="Niepoprawny kod",
                font=("calibre", 20, "normal"),
            )
            self.__proby.grid(row=0, column=0)
            return
        if list != None:
            if list == "wygrana":
                self.__proby.grid_remove()
                self.__proby = ttk.Label(
                    self.__left_top_frame,
                    text="Wygrana(Reset jesli chcesz zagrac ponownie)",
                    font=("calibre", 20, "normal"),
                )
                self.__proby.grid(row=0, column=0)
                return

            self.__proby.grid_remove()
            self.__proby = ttk.Label(
                self.__left_top_frame,
                text="Pozostało " + str(list[2]) + " prób",
                font=("calibre", 20, "normal"),
            )
            self.__proby.grid(row=0, column=0)
            i = 12 - list[2]
            wlasciwe = ttk.Label(
                self.__right_side,
                text=str(list[0]),
                font=("calibre", 10, "normal"),
            )
            wlasciwe.grid(row=i, column=0)
            kod = ttk.Label(
                self.__right_side,
                text=str(self.__game.returnUserGuesses()[i - 1]),
                font=("calibre", 10, "normal"),
            )
            kod.grid(row=i, column=1)
            niewlasciwe = ttk.Label(
                self.__right_side,
                text=str(list[1]),
                font=("calibre", 10, "normal"),
            )
            niewlasciwe.grid(row=i, column=2)

            self.__odpowiedzi_usun.append([wlasciwe, kod, niewlasciwe])
            if list[2] == 0:
                self.__proby.grid_remove()
                self.__proby = ttk.Label(
                    self.__left_top_frame,
                    text="Przegrana(Reset jesli chcesz zagrac ponownie)",
                    font=("calibre", 20, "normal"),
                )
                self.__proby.grid(row=0, column=0)
                return

    def resetGame(self):
        self.__game = mastermind.gameMastermind()
        self.__proby.grid_remove()
        for tabela in self.__odpowiedzi_usun:
            for czesc in tabela:
                czesc.grid_remove()

    def oszust(self):
        if isinstance(self.__game, mastermind.mastermind):
            self.__proby.grid_remove()
            self.__proby = ttk.Label(
                self.__left_top_frame,
                text="Tere fere",
                font=("calibre", 20, "normal"),
            )
            self.__proby.grid(row=0, column=0)
        else:
            self.__proby.grid_remove()
            self.__proby = ttk.Label(
                self.__left_top_frame,
                text="Złapałeś mnie!(Reset jesli chcesz zagrac ponownie)",
                font=("calibre", 20, "normal"),
            )
            self.__proby.grid(row=0, column=0)

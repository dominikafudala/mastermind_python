# from tkinter import *
# from tkinter import ttk

# # Tworzenie okna
# window = Tk()
# window.title("Skarbonka")
# # Tworzenie siatki na przyciski
# mainframe = ttk.Frame(window)
# # Umieszczenie siatki w oknie
# window.columnconfigure([0, 1, 2], minsize=100)
# window.rowconfigure([0, 1], minsize=100)
# # # Dodanie przycisków do wrzucania monet
# # i=0
# # for c in COINS:
# #     ttk.Button(mainframe, text="Wrzuć "+str(c)+"zł", command=lambda c=c: pb.add(Coin(c))).grid(column=2, row=i)
# #     i+=1
# # # Dodanie przycisku sprawdzenia wartości zawartości
# ttk.Button(text="Przerwij", command=lambda: print("tekst")).grid(column=0, row=0)

# window.mainloop()

from tkinter import *
from tkinter import ttk

# root
class Interface:
    def __init__(self):
        root = Tk()
        root.title("Mastermind")
        root.geometry("{}x{}".format(1200, 800))

        # two main columns
        left_side = ttk.Frame(root)
        right_side = ttk.Frame(root)

        root.rowconfigure(0, weight=1)
        root.columnconfigure([0, 1], weight=1)

        left_side.grid(row=0, column=0)
        right_side.grid(row=0, column=1)

        # left side wit entry and buttons
        left_side.rowconfigure([0, 1], weight=1)
        left_side.columnconfigure(0, weight=1)

        left_top_frame = ttk.Frame(left_side)
        left_bottom_frame = ttk.Frame(left_side)

        left_top_frame.grid(row=0, column=0)
        left_bottom_frame.grid(row=1, column=0)

        # entry
        left_top_frame.rowconfigure([0, 1], weight=1)
        left_top_frame.columnconfigure(0, weight=1)
        entry_var = StringVar()
        entry_var.set("")
        text = ttk.Label(
            left_top_frame,
            text="Pozostało " + "x" + " prób",
            font=("calibre", 20, "normal"),
        ).grid(row=0, column=0)
        entry = Entry(
            left_top_frame, textvariable=entry_var, font=("calibre", 20, "normal")
        ).grid(row=1, column=0)

        left_bottom_frame.rowconfigure(0, weight=1, minsize=70)
        left_bottom_frame.columnconfigure([0, 1, 2], weight=1)
        ttk.Button(
            left_bottom_frame, text="Sprawdź", command=lambda: print(entry_var.get())
        ).grid(column=0, row=0)
        ttk.Button(
            left_bottom_frame, text="Oszust", command=lambda: print(entry_var.get())
        ).grid(column=1, row=0)
        ttk.Button(
            left_bottom_frame, text="Reset", command=lambda: print(entry_var.get())
        ).grid(column=2, row=0)

        # answers column
        right_side.rowconfigure([x for x in range(13)], weight=1, minsize=46)
        right_side.columnconfigure([x for x in range(3)], weight=1, minsize=100)
        ttk.Label(
            right_side,
            text="Właściwe |",
            font=("calibre", 18, "normal"),
        ).grid(row=0, column=0)
        ttk.Label(
            right_side,
            text=" Odpowiedzi ",
            font=("calibre", 18, "normal"),
        ).grid(row=0, column=1)
        ttk.Label(
            right_side,
            text="| Niewłaściwe",
            font=("calibre", 18, "normal"),
        ).grid(row=0, column=2)
        for i in range(12):
            ttk.Label(
                right_side,
                text="tu wlasciwe",
                font=("calibre", 10, "normal"),
            ).grid(row=i + 1, column=0)
            ttk.Label(
                right_side,
                text=str(i + 1) + " " + "kod",
                font=("calibre", 10, "normal"),
            ).grid(row=i + 1, column=1)
            ttk.Label(
                right_side,
                text="tu niewlasciwe",
                font=("calibre", 10, "normal"),
            ).grid(row=i + 1, column=2)

        root.mainloop()

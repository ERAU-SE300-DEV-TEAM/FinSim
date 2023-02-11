from MainSim import *
from MainSim import MainSim
from Menu import *
import tkinter as tk

from OtherPage import OtherPage
from Simulator import *
from OtherPage import *

TITLE_FONT = ("Helvetica", 18, "bold")


class Simulator(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        self.attributes("-fullscreen", True)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Menu, MainSim, OtherPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Menu)

    def show_frame(self, c):
        frame = self.frames[c]
        frame.tkraise()


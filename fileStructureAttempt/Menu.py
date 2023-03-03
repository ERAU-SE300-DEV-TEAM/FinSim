import tkinter as tk

import fileStructureAttempt.Menu as Menu
from fileStructureAttempt.MainSim import MainSim
from fileStructureAttempt.Menu import *
from fileStructureAttempt.OtherPage import *
from fileStructureAttempt.Simulator import *


class fileStructureAttempt.Menu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file="lottomoney.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=592, height=450)
        label = tk.Label(self, text="Menu")
        label.place(x=0, y=0, width=592, height=44)

        button1 = tk.Button(
            self, text="Simulator", command=lambda: controller.show_frame(MainSim)
        )
        button2 = tk.Button(
            self, text="Extra Page", command=lambda: controller.show_frame(OtherPage)
        )
        button3 = tk.Button(self, text="Exit", command=self.quit)
        button1.place(x=100, y=406, width=200, height=44)
        button2.place(x=300, y=406, width=200, height=44)
        button3.place(x=500, y=406, width=80, height=44)

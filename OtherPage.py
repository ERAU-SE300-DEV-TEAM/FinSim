import Menu
from Menu import *
import tkinter as tk
from Simulator import *
from OtherPage import *


class OtherPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file="lottomoney.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=592, height=450)
        label = tk.Label(self, text="Extra")
        label.place(x=0, y=0, width=592, height=44)

        button1 = tk.Button(self, text="Menu",
                            command=lambda: controller.show_frame(Menu))
        # button2 = tk.Button(self, text="Go to Page two",
        #                   command=lambda: controller.show_frame(PageTwo))
        button3 = tk.Button(self, text="Exit",
                            command=self.quit)
        button1.place(x=100, y=406, width=200, height=44)
        button3.place(x=300, y=406, width=200, height=44)

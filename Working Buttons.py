import tkinter as tk
from tkinter import ttk
from FinSimController import *

LARGE_FONT = ("Verdana", 12)


# Define image
#bg = tk.PhotoImage(file="CBGR.png")

# Add image file
#bg = PhotoImage( file = "CBGR.png")

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Menu", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="New Game", bg="Light blue", font='Helvetica 18 bold',
                           command=lambda: [controller.show_frame(PageOne), menu()])
        button.pack()

        button2 = tk.Button(self, text="Continue", bg="Light blue", font='Helvetica 18 bold')
        button2.pack()

        button2 = tk.Button(self, text="Exit", bg="black", fg='white', font='Helvetica 18 bold')
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="- Fin Sim -", font='Helvetica 24 bold')
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Spend money", bg="Light blue", font='Helvetica 18 bold',)

        button1.pack()

        button2 = tk.Button(self, text="Return to Main Menu", bg="black", fg='white', font='Helvetica 18 bold',
                            command=lambda: controller.show_frame(StartPage))
        button2.pack()


app = SeaofBTCapp()
app.mainloop()
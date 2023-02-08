import tkinter as tk

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
        for F in (StartPage, MainSim, OtherPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, c):
        frame = self.frames[c]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file="lottomoney.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=592, height=450)
        label = tk.Label(self, text="Menu", font=TITLE_FONT)
        label.place(x=0, y=0, width=592, height=44)

        button1 = tk.Button(self, text="Simulator",
                            command=lambda: controller.show_frame(MainSim))
        button2 = tk.Button(self, text="Extra Page",
                            command=lambda: controller.show_frame(OtherPage))
        button3 = tk.Button(self, text="Exit",
                            command=self.quit)
        button1.place(x=100, y=406, width=200, height=44)
        button2.place(x=300, y=406, width=200, height=44)
        button3.place(x=500, y=406, width=80, height=44)


class MainSim(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file="lottomoney.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=592, height=450)
        label = tk.Label(self, text="Simulator", font=TITLE_FONT)
        label.place(x=0, y=0, width=592, height=44)

        button1 = tk.Button(self, text="Menu",
                            command=lambda: controller.show_frame(StartPage))
        # button2 = tk.Button(self, text="Go to Page two",
        #                   command=lambda: controller.show_frame(PageTwo))
        button3 = tk.Button(self, text="Exit",
                            command=self.quit)
        button1.place(x=100, y=406, width=200, height=44)
        button3.place(x=300, y=406, width=200, height=44)


class OtherPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file="lottomoney.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=592, height=450)
        label = tk.Label(self, text="Extra", font=TITLE_FONT)
        label.place(x=0, y=0, width=592, height=44)

        button1 = tk.Button(self, text="Menu",
                            command=lambda: controller.show_frame(StartPage))
        # button2 = tk.Button(self, text="Go to Page two",
        #                   command=lambda: controller.show_frame(PageTwo))
        button3 = tk.Button(self, text="Exit",
                            command=self.quit)
        button1.place(x=100, y=406, width=200, height=44)
        button3.place(x=300, y=406, width=200, height=44)


if __name__ == "__main__":
    app = Simulator()
    app.mainloop()

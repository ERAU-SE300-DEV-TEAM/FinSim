import tkinter
import customtkinter

TITLE_FONT = ("Helvetica", 18, "bold")


class Simulator(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        customtkinter.CTk.__init__(self, *args, **kwargs)
        container = customtkinter.Frame(self)
        self.attributes("-fullscreen", True)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, c):
        frame = self.frames[c]
        frame.tkraise()


class StartPage(customtkinter.Frame):
    def __init__(self, parent, controller):
        customtkinter.Frame.__init__(self, parent)
        logo = customtkinter.PhotoImage(file="lottomoney.png")
        BGlabel = customtkinter.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=592, height=450)
        label = customtkinter.Label(self, text="This is the start page", font=TITLE_FONT)
        label.place(x=0, y=0, width=592, height=44)

        button1 = customtkinter.Button(self, text="Go to Page One",
                                       command=lambda: controller.show_frame(PageOne))
        button2 = customtkinter.Button(self, text="Go to Page two",
                                       command=lambda: controller.show_frame(PageTwo))
        button3 = customtkinter.Button(self, text="Exit",
                                       command=self.quit)
        button1.place(x=100, y=406, width=200, height=44)
        button2.place(x=300, y=406, width=200, height=44)
        button3.place(x=500, y=406, width=80, height=44)


class PageOne(customtkinter.Frame):
    def __init__(self, parent, controller):
        customtkinter.Frame.__init__(self, parent)
        logo = customtkinter.PhotoImage(file="lottomoney.png")
        BGlabel = customtkinter.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=592, height=450)
        label = customtkinter.Label(self, text="This is page one", font=TITLE_FONT)
        label.place(x=0, y=0, width=592, height=44)

        button1 = customtkinter.Button(self, text="Go to Start Page",
                                       command=lambda: controller.show_frame(StartPage))
        # button2 = tk.Button(self, text="Go to Page two",
        #                   command=lambda: controller.show_frame(PageTwo))
        button3 = customtkinter.Button(self, text="Exit",
                                       command=self.quit)
        button1.place(x=100, y=406, width=200, height=44)
        button3.place(x=300, y=406, width=200, height=44)


class PageTwo(customtkinter.Frame):
    def __init__(self, parent, controller):
        customtkinter.Frame.__init__(self, parent)
        logo = customtkinter.PhotoImage(file="lottomoney.png")
        BGlabel = customtkinter.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=592, height=450)
        label = customtkinter.Label(self, text="This is page two", font=TITLE_FONT)
        label.place(x=0, y=0, width=592, height=44)

        button1 = customtkinter.Button(self, text="Go to Start Page",
                                       command=lambda: controller.show_frame(StartPage))
        # button2 = tk.Button(self, text="Go to Page two",
        #                   command=lambda: controller.show_frame(PageTwo))
        button3 = customtkinter.Button(self, text="Exit",
                                       command=self.quit)
        button1.place(x=100, y=406, width=200, height=44)
        button3.place(x=300, y=406, width=200, height=44)


if __name__ == "__main__":
    app = Simulator()
    app.mainloop()

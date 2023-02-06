import tkinter
import customtkinter


LARGE_FONT = ("Verdana", 12)


class SeaofBTCapp(tkinter.Tk):

    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)
        container = tkinter.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, MainPage):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(customtkinter.Frame):
    # Define image
    bg = tkinter.PhotoImage(file="lottomoney.png")

    # Create a canvas
    my_canvas = tkinter.Canvas(root, width=800, height=500)
    my_canvas.pack(fill="both", expand=True)

    # Set image in canvas
    my_canvas.create_image(0, 0, image=bg, anchor="nw")

    # Add a label
    my_canvas.create_text(350, 100, text="Welcome!", font=("Helvetica", 50), fill="Black")

    new_sim = customtkinter.CTkButton(master=root, text="New Simulation", fg_color="violet", text_color="Black")
    new_sim.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

    cont = customtkinter.CTkButton(master=root, text="Continue", fg_color="Green")
    cont.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)

    leave = customtkinter.CTkButton(master=root, text="Exit Simulation", fg_color="red")
    leave.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = tkinter.Button(self, text="Visit Page 1",
                           command=lambda: controller.show_frame(MainPage))
        button.pack()


class MainPage(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = customtkinter.Label(self, text="Main Page!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tkinter.Button(self, text="Back to Home",
                                 command=lambda: controller.show_frame(StartPage))
        button1.pack()


root = SeaofBTCapp()
root.mainloop()

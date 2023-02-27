from tkinter import *

# Create object
root = Tk()

# Adjust size
root.geometry("1960x1080")

# Add image file
bg = PhotoImage(file="CBGRBaked03.png")

# Show image using label
label1 = Label(root, image=bg)
label1.place(x=0, y=0)

#root.create_image(1960/2, 150, image=image, options) and root.create_text(x, y, text="Some text", options)
#root.create_text(1960/2, 150, text="Sim Fin",)

# Add text
#label2 = Label(root, text="Sim Fin", bg="white", font='Helvetica 70 bold')

#label2.pack(pady=150)

# Create Frame
#frame1 = Frame(root, bg="#88cffa")
#frame1.pack(pady=20)

# Button action
def button1Function() :
    print('Submit button is clicked.')

# Add buttons
button1 = Button(text="New Simulation", bg="Light blue", font='Helvetica 18 bold')
button1.place(relx=0.45, rely=0.5)
#button1.place(x=590, y=1300)
#button1.pack(pady=30)

button2 = Button(text="Continue", bg="Light blue", font='Helvetica 18 bold')
#button2.pack(pady=30)
#button2.place(x=590, y=1500)
button2.place(relx=0.473, rely=0.6)

button3 = Button(text="Exit", bg="black", fg='white', font='Helvetica 18 bold')
#button3.pack(pady=30)
#button3.place(x=590, y=1700)
button3.place(relx=0.491, rely=0.7)

class SeaofBTCapp(root.Tk):

    def __init__(self, *args, **kwargs):
        root.Tk.__init__(self, *args, **kwargs)
        container = root.Frame(self)

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
        frame.rootraise()


class StartPage(root.Frame):

    def __init__(self, parent, controller):

        root.Frame.__init__(self, parent)
        label = root.Label(self, text="Menu", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = root.Button(self, text="New Game", bg="Light blue", font='Helvetica 18 bold',
                           command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = root.Button(self, text="Continue", bg="Light blue", font='Helvetica 18 bold')
        button2.pack()

        button2 = root.Button(self, text="Exit", bg="black", fg='white', font='Helvetica 18 bold')
        button2.pack()


class PageOne(root.Frame):

    def __init__(self, parent, controller):
        root.Frame.__init__(self, parent)
        label = root.Label(self, text="Main Screen", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = root.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = root.Button(self, text="Page Two")
        button2.pack()


app = SeaofBTCapp()

# Execute tkinter
root.mainloop()
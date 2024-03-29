import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class SimFin(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("1960x1080")
        self.title("Sim Fin")
        self.background_image = tk.PhotoImage(file="CBGRBaked03.png")
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.container = tk.Frame(self, width=1200, height=600, bg="white")
        self.container.place(relx=0.5, rely=0.5, anchor="center")

        self.frames = {}
        for F in (MainPage, NewGamePage):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.place(x=0, y=0, relwidth=1, relheight=1)

        self.show_frame("MainPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        style_red = ttk.Style()
        style_red.configure("Custom.TButton.Red", background="red", font='Helvetica 18 bold')

        layout_red = ttk.Style()
        layout_red.layout("Custom.TButton.Red", [("Button.padding", {"side": "left", "sticky": ''}),
                                                 ("Button.label",
                                                  {"side": "left", "sticky": ''})])

        style_blue = ttk.Style()
        style_blue.configure("Custom.TButton.Blue", background="light blue", font='Helvetica 18 bold')

        layout_blue = ttk.Style()
        layout_blue.layout("Custom.TButton.Blue", [("Button.padding", {"side": "left", "sticky": ''}),
                                                   ("Button.label",
                                                    {"side": "left", "sticky": ''})])

        style_black = ttk.Style()
        style_black.configure("Custom.TButton.Black", background="black", font='Helvetica 18 bold', foreground="white")

        layout_black = ttk.Style()
        layout_black.layout("Custom.TButton.Black", [("Button.padding", {"side": "left", "sticky": ''}),
                                                     ("Button.label",
                                                      {"side": "left", "sticky": ''})])

        new_game_button = ttk.Button(self, text="New Game", width=80, style="Custom.TButton.Blue",
                                     command=lambda: controller.show_frame("NewGamePage"))
        new_game_button.configure(style="Custom.TButton.Blue")
        new_game_button.pack(pady=10)

        continue_button = ttk.Button(self, text="Continue", style="Custom.TButton.Blue")
        continue_button.pack(pady=10)

        leaderboard_button = ttk.Button(self, text="Leaderboards", style="Custom.TButton.Red")
        leaderboard_button.configure(style="Custom.TButton.Red")
        leaderboard_button.pack(pady=10)

        exit_button = ttk.Button(self, text="Exit", style="Custom.TButton.Black",
                                 command=self.exit_game)
        exit_button.configure(style="Custom.TButton.Black")
        exit_button.pack(pady=10)

    def exit_game(self):
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            self.controller.destroy()


class NewGamePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #style_black = ttk.Style()
        #style_black.configure("Custom.TButton.Black", background="black", font='Helvetica 18 bold')

        label = tk.Label(self, text="Enter your name:")
        label.pack(pady=10)

        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=10)

        submit_button = ttk.Button(self, text="Submit", command=self.save_name)
        submit_button.pack(pady=10)

    def save_name(self):
        name = self.name_entry.get()
        with open("names.txt", "a") as file:
            file.write(name + "\n")
        messagebox.showinfo("Success", f"Name {name} saved!")
        self.controller.show_frame("MainPage")

class mainApp(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        # Set up the label and button for page one
        label = tk.Label(self, text="This is Page One")
        label.pack(pady=10,padx=10)

        button = ttk.Button(self, text="Go to Start Page",
                            command=lambda: controller.show_frame("StartPage"))
        button.pack()


app = SimFin()
app.mainloop()
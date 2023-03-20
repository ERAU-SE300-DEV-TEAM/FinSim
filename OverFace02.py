import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
#

class SimFin(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("1960x1080")
        self.title("Sim Fin")
        self.background_image = tk.PhotoImage(file="CBGRBaked04.png")
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.container = tk.Frame(self, width=300, height=650, bg="white")
        self.container.place(relx=0.5, rely=0.5, anchor="center")

        self.frames = {}
        for F in (MainPage, NewGamePage, MainApp, MainApp2):
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
        style_blue.configure("Custom.TButton.Blue", background="#ADD8E6", font='Helvetica 18 bold')

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

        new_game_button = ttk.Button(self, text="New Game", width=20, style="Custom.TButton.Blue",
                                     command=lambda: controller.show_frame("NewGamePage"))
        new_game_button.configure(style="Custom.TButton.Blue")
        new_game_button.pack(pady=50)

        continue_button = ttk.Button(self, text="Continue", width=20, style="Custom.TButton.Blue")
        continue_button.pack(pady=50)

        leaderboard_button = ttk.Button(self, text="Leaderboards", width=20, style="Custom.TButton.Red")
        leaderboard_button.configure(style="Custom.TButton.Red")
        leaderboard_button.pack(pady=50)

        exit_button = ttk.Button(self, text="Exit", width=20, style="Custom.TButton.Black",
                                 command=self.exit_game)
        exit_button.configure(style="Custom.TButton.Black")
        exit_button.pack(pady=50)

    def exit_game(self):
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            self.controller.destroy()


class NewGamePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Enter your name:")
        label.pack(pady=10)

        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=10)

        submit_button = ttk.Button(self, text="Submit", command=self.save_name)
        submit_button.pack(pady=10)

        submit_button = ttk.Button(self, text="Start", command=lambda: controller.show_frame("MainApp"))
        submit_button.pack(pady=10)

        submit_button = ttk.Button(self, text="Main Page", command=lambda: controller.show_frame("MainPage"))
        submit_button.pack(pady=10)

    def save_name(self):
        name = self.name_entry.get()
        with open("names.txt", "a") as file:
            file.write(name + "\n")
        messagebox.showinfo("Success", f"Name {name} saved!")
        # self.controller.show_frame("MainApp")


class MainApp(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # display a text block
        label4 = tk.Label(self, font='Helvetica 24 bold', text="Month 1")
        label4.pack(pady=5)

        label0 = tk.Label(self, text="Your total money is: ")
        label0.pack(pady=25)

        label5 = tk.Label(self, font='Helvetica 14 bold', text="$1500")
        label5.pack(pady=25)

        label1 = tk.Label(self, text="Your living expenses are: ")
        label1.pack(pady=25)

        label6 = tk.Label(self, font='Helvetica 14 bold', text="$1200")
        label6.pack(pady=25)

        label2 = tk.Label(self, text="Enter in how much you want to spend:")
        label2.pack(pady=10)

        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=10)

        submit_button = ttk.Button(self, text="Submit", command=self.spend_amount)
        submit_button.pack(pady=10)

        style_red = ttk.Style()
        style_red.configure("Custom.TButton.Red2", background="red", font='Helvetica 14 bold', foreground="white")

        layout_red2 = ttk.Style()
        layout_red2.layout("Custom.TButton.Red2", [("Button.padding", {"side": "left", "sticky": ''}),
                                                 ("Button.label",
                                                  {"side": "left", "sticky": ''})])

        next_month = ttk.Button(self, text="Next Month", width=20, style="Custom.TButton.Red2",
                                command=lambda: controller.show_frame("MainApp2"))
        next_month.configure(style="Custom.TButton.Red2")
        next_month.pack(pady=20)

        style_black2 = ttk.Style()
        style_black2.configure("Custom.TButton.Black2", background="black", font='Helvetica 14 bold', foreground="white")

        layout_black2 = ttk.Style()
        layout_black2.layout("Custom.TButton.Black2", [("Button.padding", {"side": "left", "sticky": ''}),
                                                     ("Button.label",
                                                      {"side": "left", "sticky": ''})])

        exit_button = ttk.Button(self, text="Save and Exit", width=20, style="Custom.TButton.Black2",
                                 command=self.exit_game)
        exit_button.configure(style="Custom.TButton.Black2")
        exit_button.pack(pady=20)

    def spend_amount(self):
        spend = self.name_entry.get()
        with open("spend.txt", "a") as file:
            file.write(spend + "\n")
        messagebox.showinfo("You paid your bills!", f"Kino paid {spend}!")
        self.controller.show_frame("mainApp2")

    def exit_game(self):
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            self.controller.destroy()


class MainApp2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # display a text block
        label4 = tk.Label(self, font='Helvetica 24 bold', text="Month 2")
        label4.pack(pady=5)

        label0 = tk.Label(self, text="Your total money is: ")
        label0.pack(pady=25)

        label5 = tk.Label(self, font='Helvetica 14 bold', text="$1800")
        label5.pack(pady=25)

        label1 = tk.Label(self, text="Your living expenses are: ")
        label1.pack(pady=25)

        label6 = tk.Label(self, font='Helvetica 14 bold', text="$1200")
        label6.pack(pady=25)

        label2 = tk.Label(self, text="Enter in how much you want to spend:")
        label2.pack(pady=10)

        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=10)

        submit_button = ttk.Button(self, text="Submit", command=self.spend_amount)
        submit_button.pack(pady=10)

        style_red2 = ttk.Style()
        style_red2.configure("Custom.TButton.Red2", background="red", font='Helvetica 14 bold', foreground="white")

        layout_red2 = ttk.Style()
        layout_red2.layout("Custom.TButton.Red2", [("Button.padding", {"side": "left", "sticky": ''}),
                                                 ("Button.label",
                                                  {"side": "left", "sticky": ''})])

        next_month2 = ttk.Button(self, text="Next Month", width=20, style="Custom.TButton.Red2",
                                command=lambda: controller.show_frame("MainApp"))
        next_month2.configure(style="Custom.TButton.Red2")
        next_month2.pack(pady=20)

        style_black2 = ttk.Style()
        style_black2.configure("Custom.TButton.Black2", background="black", font='Helvetica 14 bold', foreground="white")

        layout_black2 = ttk.Style()
        layout_black2.layout("Custom.TButton.Black2", [("Button.padding", {"side": "left", "sticky": ''}),
                                                     ("Button.label",
                                                      {"side": "left", "sticky": ''})])

        exit_button = ttk.Button(self, text="Save and Exit", width=20, style="Custom.TButton.Black2",
                                 command=self.exit_game)
        exit_button.configure(style="Custom.TButton.Black2")
        exit_button.pack(pady=20)

    def spend_amount(self):
        spend = self.name_entry.get()
        with open("spend.txt", "a") as file:
            file.write(spend + "\n")
        messagebox.showinfo("You paid your bills!", f"Kino paid {spend}!")
        self.controller.show_frame("mainApp2")

    def exit_game(self):
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            self.controller.destroy()

app = SimFin()
app.mainloop()
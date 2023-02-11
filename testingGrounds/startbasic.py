import tkinter

# THIS IS THE START MENU SCREEN


root = tkinter.Tk()  # create CTk window like you do with the Tk window
root.geometry("700x800")

new_sim = tkinter.Button(master=root, text="New Simulation")
new_sim.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

cont = tkinter.Button(master=root, text="Continue")
cont.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)

leave = tkinter.Button(master=root, text="Exit Simulation")
leave.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

root.mainloop()

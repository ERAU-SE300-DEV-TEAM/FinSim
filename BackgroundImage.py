import tkinter
import customtkinter

# TODO THIS CODE DOESNT RUN YET!!!
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

# Add image file
bg = tkinter.PhotoImage(file="Phoenix.JPG")

root = customtkinter.CTk()  # create CTk window like you do with the Tk window
root.geometry("700x800")

new_sim = customtkinter.CTkButton(master=root, text="New Simulation", fg_color="violet", text_color="Black")
new_sim.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

cont = customtkinter.CTkButton(master=root, text="Continue", fg_color="Green")
cont.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)

leave = customtkinter.CTkButton(master=root, text="Exit Simulation", fg_color="red")
leave.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

root.mainloop()

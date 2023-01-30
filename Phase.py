import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()  # create CTk window like you do with the Tk window
root.geometry("700x800")

# def button_function():
#     print("button pressed")
#
#
# # Use CTkButton instead of tkinter Button
# button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
# button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

menu = customtkinter.CTkButton(master=root, text="MENU", fg_color="red")
menu.place(relx=0.1, rely=0.02, anchor=tkinter.CENTER)

# cont = customtkinter.CTkButton(master=app, text="Continue")
# cont.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)
#
# exit = customtkinter.CTkButton(master=app, text="Exit Simulation")
# exit.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

root.mainloop()

import tkinter
import customtkinter

# THIS IS THE START MENU SCREEN
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


root = tkinter.CTk()  # create CTk window like you do with the Tk window
root.geometry("700x800")

#button = tk.Button(self, text="Visit Page 1",
#                           command=lambda: controller.show_frame(PageOne))


new_sim = tkinter.Button(master=root, text="New Simulation", fg_color="violet", text_color="Black")
new_sim.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

cont = tkinter.Button(master=root, text="Continue", fg_color="Green")
cont.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)

leave = tkinter.Button(master=root, text="Exit Simulation", fg_color="red")
leave.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

root.mainloop()

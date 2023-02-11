import tkinter
import customtkinter

# THIS IS THE START MENU SCREEN
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


root = tkinter.Tk()  # create CTk window like you do with the Tk window
root.geometry("700x800")

#button = tk.Button(self, text="Visit Page 1",
#                           command=lambda: controller.show_frame(PageOne))


#variable_name = Button(parent, bg=’your_color’)
#btn = Button(root, fg='red') #Creates a button with red text
#labelPryProt = Label(frame1, text='TEXTTEXT', font='Helvetica 18 bold')


new_sim = tkinter.Button(master=root, text="New Simulation", bg="Light blue", font='Helvetica 18 bold')
new_sim.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

cont = tkinter.Button(master=root, text="Continue", bg="Light blue", font='Helvetica 18 bold')
cont.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)

leave = tkinter.Button(master=root, text="Exit Simulation", bg="black", fg='white', font='Helvetica 18 bold')
leave.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

root.mainloop()

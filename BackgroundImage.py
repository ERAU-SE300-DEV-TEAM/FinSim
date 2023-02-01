import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()
root.title('Background Image')
root.geometry("700x800")

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

'''
# Create a label
my_label = Label(root, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)
# Add something to the top of our image
my_text = Label(root, text="Welcome!", font=("Helvetica", 50), fg="white", bg="#2a1863")
my_text.pack(pady=50)
# create a frame
my_frame = Frame(root, bg='#6b88fe')
my_frame.pack(pady=20)
# Add some buttons
my_button1 = Button(my_frame, text="Exit")
my_button1.grid(row=0, column=0, padx=20)
my_button2 = Button(my_frame, text="Start")
my_button2.grid(row=0, column=1, padx=20)
my_button3 = Button(my_frame, text="Reset")
my_button3.grid(row=0, column=2, padx=20)
'''

root.mainloop()

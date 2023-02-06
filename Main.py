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

# Create text widget and specify size.
T = tkinter.Text(root, height=5, width=52)

# Create label
l = tkinter.Label(root, text="Fact of the Day")
l.config(font=("Courier", 14))

Fact = """A man can be arrested in
Italy for wearing a skirt in public."""

# Create button for next text.
b1 = tkinter.Button(root, text="Next", )

# Create an Exit button.
b2 = tkinter.Button(root, text="Exit", command=root.destroy)

l.pack()
T.pack()
b1.pack()
b2.pack()

# Insert The Fact.
T.insert(customtkinter.END, Fact)

root.mainloop()

# Import module
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

# Execute tkinter
root.mainloop()
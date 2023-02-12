# Import module
from tkinter import *

# Create object
root = Tk()

# Adjust size
root.geometry("1960x1080")

# Add image file
bg = PhotoImage(file="CBGRBaked02.png")

# Show image using label
label1 = Label(root, image=bg)
label1.place(x=0, y=0)

# Button action
def button1Function() :
    print('Submit button is clicked.')


def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")

B = root.Button(top, text ="Hello", command = helloCallBack)

B.pack()

# Add buttons
button1 = Button(text="New Simulation", bg="Light blue", font='Helvetica 18 bold')
button1.place(relx=0.45, rely=0.5)

button2 = Button(text="Continue", bg="Light blue", font='Helvetica 18 bold')
button2.place(relx=0.473, rely=0.6)

button3 = Button(text="Exit", bg="black", fg='white', font='Helvetica 18 bold')
button3.place(relx=0.491, rely=0.7)

# Execute tkinter
root.mainloop()
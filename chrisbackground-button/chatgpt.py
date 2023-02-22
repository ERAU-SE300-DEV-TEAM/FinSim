import tkinter as tk

root = tk.Tk()
root.geometry("600x400")
root.title("My Desktop App")

bg_image = tk.PhotoImage(file="hello.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

frame1 = tk.Frame(root, bg='white')
frame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.4)

frame2 = tk.Frame(root, bg='white')
frame2.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.4)

button1 = tk.Button(frame1, text="Button 1", fg='black', bg='white')
button1.pack(side="left", padx=10, pady=10)

button2 = tk.Button(frame1, text="Button 2", fg='black', bg='white')
button2.pack(side="left", padx=10, pady=10)

button3 = tk.Button(frame2, text="Button 3", fg='black', bg='white')
button3.pack(side="left", padx=10, pady=10)

button4 = tk.Button(frame2, text="Button 4", fg='black', bg='white')
button4.pack(side="left", padx=10, pady=10)

root.mainloop()

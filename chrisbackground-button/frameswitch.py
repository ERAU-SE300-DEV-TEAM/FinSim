import tkinter as tk


def show_frame(frame):
    frame.tkraise()


window = tk.Tk()
window.state("zoomed")

# # Adjust size
# window.geometry("1960x1080")

# # Add image file
# bg = tk.PhotoImage(file="CBGRBaked03.png")
# label1 = tk.Label(window, image=bg)
# label1.place(x=0, y=0)

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)

for frame in (frame1, frame2, frame3):
    frame.grid(row=0, column=0, sticky="nsew")

# ==================Frame 1 code
frame1_title = tk.Label(frame1, text="Main Menu", font="times 35", bg="cyan")
frame1_title.pack(fill="both", expand=True)

frame1_btn = tk.Button(frame1, text="New Simulation", command=lambda: show_frame(frame2))
frame1_btn.place(relx=0.45, rely=0.5)

frame2_btn = tk.Button(frame1, text="Continue")
frame2_btn.place(relx=0.473, rely=0.6)

frame3_btn = tk.Button(frame1, text="Exit")
frame3_btn.place(relx=0.491, rely=0.7)

# ==================Frame 2 code
frame2_title = tk.Label(frame2, text="Simulation", font="times 35", bg="violet")
frame2_title.pack(fill="both", expand=True)

frame1_btn = tk.Button(frame2, text="Spend Money")
frame1_btn.place(relx=0.45, rely=0.5)

frame3_btn = tk.Button(frame2, text="Return to Main Menu", command=lambda: show_frame(frame1))
frame3_btn.place(relx=0.491, rely=0.7)

# ==================Frame 3 code
frame3_title = tk.Label(frame3, text="Page 3", font="times 35", bg="green")
frame3_title.pack(fill="both", expand=True)

frame1_btn = tk.Button(frame3, text="Enter")
frame1_btn.place(relx=0.45, rely=0.5)

show_frame(frame1)

window.mainloop()

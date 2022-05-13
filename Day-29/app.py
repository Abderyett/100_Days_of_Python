from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
logo = PhotoImage(file="./logo.png")
canvas = Canvas(width=400, height=400)
canvas.create_image(200, 200, image=logo)
canvas.grid()

window.mainloop()

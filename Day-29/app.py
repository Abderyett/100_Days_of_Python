from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def submit():
    with open("passwords.txt", mode="a") as file:
        file.write(
            f"{website_input.get()} | {username_input.get()} | {password_input.get()}\n")

        website_input.delete(0, END)
        password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
logo = PhotoImage(file="./logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)
# Website Label
website_label = Label(text="Website:").grid(column=0, row=1)
# Website Entery
website_input = Entry(width=35)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)

# username Label
username_label = Label(text="Email/Username:").grid(column=0, row=2)
# username Entery
username_input = Entry(width=35)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(0, "abderyett@gmail.com")


# password Label
password_label = Label(text="Password:").grid(column=0, row=3)
# Password Entery
password_input = Entry(width=35)
password_input.grid(column=1, row=3, columnspan=1)
# Button generate Password
pass_btn = Button(text="Generate Password").grid(column=3, row=3)

# Add Button
add_btn = Button(text="Add", width=35, command=submit).grid(column=1, row=4)

window.mainloop()

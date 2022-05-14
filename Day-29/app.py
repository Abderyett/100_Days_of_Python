from dataclasses import field
from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def submit():
    website = website_input.get()
    email = username_input.get()
    password = password_input.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(
            title="Empty field", message="Please fill the empty field")
    else:

        is_ok = messagebox.askokcancel(
            title=website, message=f"These are details entred :\nUsername: {email}\nPassword:{password}\n Do you want to save?")
        if is_ok:
            with open("passwords.txt", mode="a") as file:
                file.write(
                    f"{website} | {email} | {password}\n")

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

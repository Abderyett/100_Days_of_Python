
from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters)
                     for _ in range(randint(8, 10))]

    symbols_list = [choice(symbols)
                    for _ in range(randint(2, 4))]

    numbers_list = [choice(numbers)
                    for _ in range(randint(2, 4))]

    password_list = password_list + symbols_list + numbers_list

    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def submit():
    global new_data
    website = website_input.get()
    email = username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }, }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(
            title="Empty field", message="Please fill the empty field")
    else:
        open_file()


def open_file():

    try:
        with open("passwords.json", "r") as file:
            # Reading File
            data = json.load(file)

    except FileNotFoundError:
        with open("passwords.json", "w") as file:
            json.dump(new_data, file, indent=4)
            # Update data

    else:
        # Saving data
        data.update(new_data)
        with open("passwords.json", "w") as file:
            json.dump(data, file, indent=4)
    finally:
        website_input.delete(0, END)
        password_input.delete(0, END)
        # ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    try:
        with open("passwords.json", "r") as file:
            # Reading File
            data = json.load(file)
            website = website_input.get()

            if website in data:
                item = data[website]

                messagebox.showinfo(
                    title=website, message=f"Email: {item['email']}\nPassword: {item['password']} ")

            else:

                messagebox.showwarning(
                    title="Error", message="password not found")

    except FileNotFoundError:
        open_file()


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
# Search Buttons
search_btn = Button(text="Search", width=15, command=find_password)
search_btn.grid(column=3, row=1)


# username Label
username_label = Label(text="Email/Username:").grid(column=0, row=2)
# username Entery
username_input = Entry(width=35)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(0, "abderyett@gmail.com")


# password Label
password_label = Label(text="Password:").grid(column=0, row=3)
# Password Entry
password_input = Entry(width=35)
password_input.grid(column=1, row=3, columnspan=1)
# Button generate Password
pass_btn = Button(text="Generate Password",
                  command=generate_password).grid(column=3, row=3)

# Add Button
add_btn = Button(text="Add", width=35, command=submit).grid(column=1, row=4)

window.mainloop()

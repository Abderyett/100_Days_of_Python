from tkinter import *
import pandas as pd
import random
current_card = {}
BACKGROUND_COLOR = "#B1DDC6"
current_card_index = 0
# ---------------------------- CARD FUNCTIONALITY ------------------------------- #
try:
    data = pd.read_csv('./data/word_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('./data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


def next_card():
    global current_card, flip_timer, current_card_index
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card['French'], fill='black')
    canvas.itemconfig(card_img, image=fr_img)

    flip_timer = window.after(3000, flip)


def known_word():

    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("./data/word_to_learn.csv", index=False)
    next_card()


def flip():

    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_img, image=en_img)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, flip)
canvas = Canvas(width=800, height=526,
                bg=BACKGROUND_COLOR, highlightthickness=0)
fr_img = PhotoImage(file='./images/card_front.png')
en_img = PhotoImage(file='./images/card_back.png')
card_img = canvas.create_image(400, 263, image=fr_img)
card_title = canvas.create_text(
    400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(
    400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


# Cross Button image
cross_btn_img = PhotoImage(file='./images/wrong.png')
unknown_btn = Button(image=cross_btn_img, command=next_card)
unknown_btn.grid(row=1, column=0)

# Valid Button image
valid_btn_img = PhotoImage(file='./images/right.png')
valid_btn = Button(image=valid_btn_img, command=known_word)
valid_btn.grid(row=1, column=1)

next_card()

window.mainloop()

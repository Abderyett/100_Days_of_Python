from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
# ---------------------------- CARD FUNCTIONALITY ------------------------------- #

data = pd.read_csv('./data/french_words.csv')
to_learn = data.to_dict(orient='records')


def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French')
    canvas.itemconfig(card_word, text=current_card['French'])


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
canvas = Canvas(width=800, height=526,
                bg=BACKGROUND_COLOR, highlightthickness=0)
fr_img = PhotoImage(file='./images/card_front.png')
canvas.create_image(400, 263, image=fr_img)
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
unknown_btn = Button(image=valid_btn_img, command=next_card)
unknown_btn.grid(row=1, column=1)

next_card()

window.mainloop()

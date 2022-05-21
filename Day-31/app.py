from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
canvas = Canvas(width=800, height=526,
                bg=BACKGROUND_COLOR, highlightthickness=0)
fr_img = PhotoImage(file='./images/card_front.png')
canvas.create_image(400, 263, image=fr_img)
canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


# Cross Button image
cross_btn_img = PhotoImage(file='./images/wrong.png')
unknown_btn = Button(image=cross_btn_img)
unknown_btn.grid(row=1, column=0)

# Valid Button image
valid_btn_img = PhotoImage(file='./images/right.png')
unknown_btn = Button(image=valid_btn_img)
unknown_btn.grid(row=1, column=1)


window.mainloop()

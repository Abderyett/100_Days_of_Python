from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(bg=YELLOW)
window.title("Pomodoro")
window.config(padx=100, pady=50)
tomato_img = PhotoImage(file="./tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white",
                   font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)
# Lablel
label = Label(text="Timer", font=(FONT_NAME, 60, "bold"), fg=GREEN, bg=YELLOW)
label.grid(column=2, row=1)

label_check = Label(text="✓", font=(FONT_NAME, 40, "bold"),
                    fg=GREEN, bg=YELLOW).grid(column=2, row=8)
# Buttons

start_btn = Button(text="Start", fg="white",
                   highlightbackground=GREEN, cursor="hand", highlightthickness=0).grid(column=1, row=8)
reset_btn = Button(text="reset", fg="white",
                   highlightbackground=RED, cursor="hand", highlightthickness=0).grid(column=9, row=8)
canvas.grid()

window.mainloop()

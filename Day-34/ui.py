from tkinter import *


THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, background='white')
        self.canvas.grid(row=1, column=1)
        self.score_text = Label(
            text="Score:", bg="white")
        self.score_text.grid(row=0, column=1)
        self.window.mainloop()

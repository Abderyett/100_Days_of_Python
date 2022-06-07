from tkinter import *


THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_text = Label(
            text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_text.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250,
                             bg='white')
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Some dummy text", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.check_path = PhotoImage(file='./images/true.png')
        self.valid_btn = Button(image=self.check_path, highlightthickness=0)
        self.valid_btn.grid(row=2, column=0)

        self.false_path = PhotoImage(file='./images/false.png')
        self.wrong_btn = Button(image=self.false_path, highlightthickness=0)
        self.wrong_btn.grid(row=2, column=1)

        self.window.mainloop()

from tkinter import *

window = Tk()
window.minsize(width=300, height=150)
window.title("Mile to KM Converter")
window.config(padx=20, pady=20)

# Input
input = Entry(width=10)
input.grid(column=3, row=0)

# Mile Label

label = Label(text="Mile", padx=10)
label.grid(column=4, row=0)

# Equal label
label = Label(text="is equal to")
label.grid(column=2, row=1)


# Button


def convert():
    text = int(input.get())
    result = round(text*1.60934)
    res.config(text=result)


button = Button(text="Convert", highlightbackground="#7c3aed",
                fg="white", font=("Monolisa", 14, "normal"), command=convert)
button.grid(column=2, row=3)

# Result
res = Label()
res.grid(column=3, row=1)

# Kim

km = Label(text="KM",)
km.grid(column=4, row=1)

window.mainloop()

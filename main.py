from tkinter import *
from pandas import *
from random import *

BACKGROUND_COLOR = "#B1DDC6"
FONT1 = ("Ariel", 40, "italic")
FONT2 = ("ariel", 60, "bold")
# RAND = randint(0, 101)
data = read_csv("./data/french_words.csv")
# new_dataframe = DataFrame(data)
new_dict = data.to_dict(orient="records")
timer = None
ch = {}
# ch = choice(new_dict)


def next_card():
    global ch
    global timer
    window.after_cancel(timer)
    ch = choice(new_dict)
    new_dict.remove(ch)
    word_to_learn = {(ch.get(val1), ch.get(val2)) for (val1, val2) in new_dict}

    # rand = randint(0, 101)
    canvas.itemconfig(cards, image=card_front)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=f"{ch["French"]}", fill="black")
    timer = window.after(3000, flip_card)


def flip_card():
    global timer
    # window.after_cancel(timer)
    canvas.itemconfig(cards, image=card_back)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=f"{ch["English"]}", fill="white")
    timer = window.after(3000, next_card)


window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR)
timer = window.after(3000, flip_card)
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)

wrong_image = PhotoImage(file="./images/wrong.png")
right_image = PhotoImage(file="./images/right.png")
card_back = PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")
cards = canvas.create_image(400, 263, image=card_front)

title_text = canvas.create_text(400, 150, text="", font=FONT1)
word_text = canvas.create_text(400, 263, text="", font=FONT2)

canvas.grid(column=0, row=0, columnspan=2, pady=50, padx=50)


wrong_button = Button(image=wrong_image, highlightthickness=0, padx=50, command=next_card)
wrong_button.grid(column=0, row=1)
right_button = Button(image=right_image, highlightthickness=0, padx=50, command=next_card)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()

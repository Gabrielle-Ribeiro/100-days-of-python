from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    df_words = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df_words = pd.read_csv("data/french_words.csv")

words_dictionary = df_words.to_dict(orient="records")
current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_dictionary)
    card.itemconfig(card_title, text="French", fill="black")
    card.itemconfig(card_text, text=current_card["French"], fill="black")
    card.itemconfig(card_background, image=front_card_image)
    flip_timer = window.after(3000, func=flip_card)
  
def flip_card():
    card.itemconfig(card_title, text="English", fill="white")
    card.itemconfig(card_text, text=current_card["English"], fill="white")
    card.itemconfig(card_background, image=back_card_image)

def remove_word():
    words_dictionary.remove(current_card)
    data = pd.DataFrame(words_dictionary)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")

flip_timer = window.after(3000, func=flip_card)

front_card_image = PhotoImage(file="images/card_front.png")
back_card_image = PhotoImage(file="images/card_back.png")

card = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_background = card.create_image(400, 263, image=front_card_image)
card_title = card.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_text = card.create_text(400, 263, text="", font=("Arial", 60, "bold"))
next_card()
card.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=remove_word)
right_button.grid(column=1, row=1)

window.mainloop()
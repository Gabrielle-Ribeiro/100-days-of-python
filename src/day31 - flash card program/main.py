from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")

front_card_image = PhotoImage(file="images/card_front.png")

card = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card.create_image(400, 263, image=front_card_image)
card.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
card.create_text(400, 263, text="trouve", font=("Arial", 60, "bold"))
card.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(column=1, row=1)

window.mainloop()
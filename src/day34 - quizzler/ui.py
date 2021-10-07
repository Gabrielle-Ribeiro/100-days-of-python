from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_label = Label(text='Score: 0', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canva = Canvas(width=300, height=250)
        self.question = self.canva.create_text(150, 125, text='question', font=('Arial', 20, 'italic'))
        self.canva.grid(row=1, column=0, columnspan=2)

        self.right_buttom = Button()

        self.window.mainloop()
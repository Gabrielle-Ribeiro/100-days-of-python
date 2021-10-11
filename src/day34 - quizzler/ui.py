from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_label = Label(text='Score: 0', bg=THEME_COLOR, fg='white')
        self.score_label.grid(row=0, column=1, sticky=E)

        self.canva = Canvas(width=300, height=250)
        self.question = self.canva.create_text(
            150,
            125,
            width=280,
            text='question', 
            font=('Arial', 20, 'italic')
        )
        self.canva.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.right_buttom = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.right_buttom.grid(row=2, column=0)

        false_image = PhotoImage(file='images/false.png')
        self.wrong_buttom = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.wrong_buttom.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canva.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            question_text = self.quiz.next_question()
            self.canva.itemconfig(self.question, text=question_text)
        else:
            self.canva.itemconfig(self.question, text="You've reached the end of the quiz.")
            self.right_buttom.config(state="disable")
            self.wrong_buttom.config(state="disable")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canva.config(bg="green")
        else:
            self.canva.config(bg="red")
        self.window.after(1000, self.get_next_question)
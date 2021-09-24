from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repetition = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    check_marks.config(text="")
    global repetition
    repetition = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global repetition
    repetition += 1

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if repetition % 8 == 0:
        label.config(text="Break", fg=RED)
        count_down(long_break_seconds)
    elif repetition % 2 == 0:
        label.config(text="Break", fg=PINK)
        count_down(short_break_seconds)
    else:
        label.config(text="Work", fg=GREEN)
        count_down(work_seconds)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_minute = count // 60
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")
    if count > 0:
        global timer 
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        if repetition % 2 == 0:
            mark = ""
            for _ in range(repetition//2):
                mark += "X"
            check_marks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 135, text='00:00', fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
label.grid(column=1, row=0)

start_button = Button(text='Start', bg=YELLOW, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', bg=YELLOW, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 14, "bold"))
check_marks.grid(column=1, row=3)

window.mainloop()
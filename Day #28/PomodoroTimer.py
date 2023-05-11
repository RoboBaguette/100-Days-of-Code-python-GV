"""
Pomodoro Timer, when the start button is hit a 25-minute timer is started for work,
when the timer is up another timer for 5-minutes is started for a break,
after 4 cycles there is a long break timer of 30-minutes
"""
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
REPS = 0
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_time():
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_mark.config(text="")
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1
    if REPS % 2 == 1:
        title_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)
    elif REPS % 8 == 0:
        title_label.config(text="Long Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    else:
        title_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 5)
        REPS += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(REPS / 2)):
            mark += "✔"
        check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
# window initialization
window = Tk()
window.title("Pomodoro")
window.config(padx=120, pady=80, bg=YELLOW)
window.minsize(width=500, height=500)

# canvas initialization
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(103, 132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

# Labels
title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
title_label.grid(column=2, row=1)

# buttons
start_button = Button(text="start", highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text="reset", highlightthickness=0, command=reset_time)
reset_button.grid(column=3, row=3)

# Label
check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=2, row=4)

window.mainloop()

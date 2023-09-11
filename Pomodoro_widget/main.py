from tkinter import *
import math


# CONSTANTS
PINK = "#eccdb4"
RED = "#fea1a1"
GREEN = "#b3c890"
YELLOW = "#ffffdd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
SEC_MIN = 60
check_text = "✓"
reps = 0
timer = None


def popup():
    win = Tk()
    win.title("Pomodoro")
    win.config(padx=100, pady=50, bg=YELLOW)
    Label(win, text = "Have a break!", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold")).pack()
    win.attributes('-topmost', True)
    win.mainloop()


# TIMER RESET
def reset():
    # stop the timer
    window.after_cancel(timer)
    timer_label.config(text="Pomodoro Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")
    global reps
    reps = 0


# TIMER MECHANISM
def start():
    global reps
    global work_reps
    reps += 1
    work_sec = WORK_MIN * SEC_MIN
    short_break_sec = SHORT_BREAK_MIN * SEC_MIN
    long_break_sec = LONG_BREAK_MIN * SEC_MIN
    if reps % 2 != 0 :
        count_down(work_sec)
        timer_label.config(text="Happy work!", fg=GREEN)
    elif reps == 8:
        count_down(long_break_sec)
        timer_label.config(text="Long break!", fg=RED)
    else:
        count_down(short_break_sec)
        timer_label.config(text="Short break!", fg=PINK)


# COUNTDOWN MECHANISM
def count_down(count):
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start()
        if reps % 2 == 0:
            check_label.config(text=check_text * math.floor(reps / 2))
            popup()


# UI SETUP
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# canvas画布
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Pomodoro_widget/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
canvas.grid(column=1, row=1)

# Label
timer_label = Label(text="Pomodoro Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=1, row=0)
timer_label.config(padx=10, pady=10)

check_label = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
check_label.grid(column=1, row=3)
check_label.config(padx=10, pady=10)

# check_label.config(text=)

# Botton
start_button = Button(text="Start", command=start)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", command=reset)
reset_button.grid(column=2, row=2)


window.mainloop()

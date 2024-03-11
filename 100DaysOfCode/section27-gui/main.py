from tkinter import *
import math
from datetime import time
from time import sleep

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK = "✓"
reps = 0
timer_running = None


def disable_start_botton():
    botton_start.config(state="disabled")

def enable_start_botton():
    botton_start.config(state="active")

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer_running)
    label_timer.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    label_check.config(text="")
    global reps
    reps = 0
    enable_start_botton()    
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_time():

    disable_start_botton()

    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label_timer.config(text='Long break', fg=RED)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_timer.config(text='Short break', fg=PINK)

    else:
        count_down(work_sec)
        label_timer.config(text='Work', fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    global reps

    count_min = math.floor(count / 60)
    count_sec = count % 60

    count_date_time = time(hour=0, minute=count_min, second=count_sec)
    count_time = count_date_time.strftime("%M:%S")
    canvas.itemconfig(timer_text, text=count_time)
    
    if count > 0:
        global timer_running
        timer_running = window.after(1000, count_down, count -1)

    else:
        start_time()

    if reps % 2 == 0:
        times = reps / 2
        checks_text = int(times) * CHECK
        label_check.config(text=checks_text)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(
    padx=100, 
    pady=50,
    bg=YELLOW)


# label timer
label_timer = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
label_timer.grid(row=0, column=1)


# creating image using canvas
canvas = Canvas(
    width=204,
    height=226,
    bg=YELLOW,
    highlightthickness=0
)

tomago_img = PhotoImage(file="100DaysOfCode/section27-gui/tomato.png")
canvas.create_image(102, 112, image=tomago_img)

# creating countdown label
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)



# label checks
check_text = CHECK
label_check = Label(font=(FONT_NAME, 25, "bold"), bg=YELLOW, fg=GREEN)
label_check.grid(row=3, column=1)


# botton start
botton_start = Button(text="Start", highlightthickness=0, command=start_time, )
botton_start.grid(row=2, column=0)


# botton stop
botton_stop = Button(text="Stop", highlightthickness=0, command=reset_timer)
botton_stop.grid(row=2, column=2)

window.mainloop()
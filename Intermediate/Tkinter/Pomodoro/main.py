from tkinter import * 
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset(): 
    window.after_cancel(timer)
    canvas.config(timer_text, text="00:00")
    title_label.config(text="Timer")

# ---------------------------- TIMER PAUSE ------------------------------- # 


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1 # first repeticion 

    work_sec =  WORK_MIN * 60 
    short_break_min =  SHORT_BREAK_MIN * 60 
    long_break_min = LONG_BREAK_MIN * 60 

    if reps & 8 == 0:
        title_label.config(text="Break", fg=RED)
        countdown(long_break_min)
    elif reps & 2 == 0:
        title_label.config(text="Break", fg=PINK)
        countdown(short_break_min)
    else:
        countdown(work_sec)
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
# import time 
def countdown(count):
    """ using timer_text (00:00) set count (example:5) 
    if count start in a number more than 0, being a decrease,
    call this method until count equal to 0
    """
    count_min = math.floor(count/60) # return min 
    count_sec = count % 60 # result the result of sec 
    if count_sec == 10:
        count_sec = f"0:{count_sec}" 
    # print(count_sec)

    canvas.itemconfig(timer_text, text =f"{count_min}:{count_sec}" )
    if count > 0:
        global timer
        # time ms (1000 - 1 seg), function to do 
        timer = window.after(1000, countdown, count - 1) # count decrease - 1
    else:
        start_timer()
        mark = ""
        work_sesion = math.floor(reps,2)
        for _ in range(work_sesion):
            # add chackmark
            mark += "✔"
        check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=100, pady=50, bg="#FFDB89")

# using for set images
canvas = Canvas(width=200, height=324, bg="#FFDB89", highlightthickness=0)
# load image file 
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 115, image=tomato)
canvas.grid(column=1, row=1)
timer_text = canvas.create_text(100,115, text="00:00", fill="white", font=(FONT_NAME, 20, "bold"))

# label check if timer is 0
title_label = Label(text="Timer", fg="#9bdeac", bg="#FFDB89", font=(FONT_NAME, 20, "bold"))
title_label.grid(column=1, row=0)

check_mark = Label(text="", fg="#9bdeac", bg="#FFDB89", font=(FONT_NAME, 20, "bold"))

# buttons 
start = Button(text="Start", command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", command=reset)
reset.grid(column=2, row=2)

window.mainloop()
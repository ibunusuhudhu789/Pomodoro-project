from tkinter import *
import math

# assigning the constant values
YELLOW = "#FBF9D1"
GREEN = "#93DA97"
RED = "#BF1A1A"
WHITE = "#F9F8F6"
PINK = "#E83C91"
WORK_MIN = 1
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 3
FONT = "Courier"
STYLE = "bold"
repeat = 0
timer_id = None


start = True


def start_timer():
    global repeat
    global start
    if start:
        repeat += 1
        if repeat == 1 or repeat == 3 or repeat == 5 or repeat == 7:
            heading.config(text="Work", font=(FONT, 40, STYLE), bg=YELLOW, fg=GREEN)
            count_down(WORK_MIN * 60)
        if repeat == 2 or repeat == 4 or repeat == 6:
            heading.config(text="Break", font=(FONT, 40, STYLE), bg=YELLOW, fg=PINK)
            count_down(SHORT_BREAK_MIN * 60)
        elif repeat == 8:
            heading.config(text="Break", font=(FONT, 40, STYLE), bg=YELLOW, fg=RED)
            count_down(LONG_BREAK_MIN * 60)


def reset_timer():
    global timer_id
    global repeat
    repeat = 0
    minutes = 0
    seconds = 0
    checkmark.config(text="", bg=YELLOW, font=(FONT, 15, STYLE))
    canvas.itemconfig(timer, text=f"{minutes:02d}:{seconds:02d}")
    heading.config(text="Timer", font=(FONT, 40, STYLE), bg=YELLOW, fg=GREEN)
    window.after_cancel(timer_id)
    timer_id = None


def count_down(count):
    global timer_id
    global repeat
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer, text=f"{minutes:02d}:{seconds}")
    if count > 0:
        timer_id = window.after(10, count_down, count - 1)
    else:
        if repeat == 2:
            checkmark.config(text="✅", bg=YELLOW, font=(FONT, 15, STYLE))
        elif repeat == 4 or repeat == 6 or repeat == 8:
            checkmark.config(text=checkmark["text"] + "✅", bg=YELLOW, font=(FONT, 15, STYLE))
        start_timer()


# creating the window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# creating the heading
heading = Label(text="Timer", font=(FONT, 40, STYLE), bg=YELLOW, fg=GREEN)
heading.grid(row=0, column=1)

# creating the canvas
tomato_image = PhotoImage(file="pomodoro_img.png")
canvas = Canvas(width=360, height=360, highlightthickness=0, bg=YELLOW)
canvas.create_image(180, 180, image=tomato_image)
timer = canvas.create_text(180, 208, text="00:00", font=(FONT, 40, STYLE), fill=WHITE)
canvas.grid(row=1, column=1)

# start button
start = Button(text="Start", padx=10, pady=10, font=(FONT, 10, STYLE), command=start_timer)
start.grid(row=2, column=0)

# reset button
reset = Button(text="Reset", padx=10, pady=10, font=(FONT, 10, STYLE), command=reset_timer)
reset.grid(row=2, column=2)

# checkmark label
checkmark = Label()
checkmark.grid(row=2, column=1)
window.mainloop()
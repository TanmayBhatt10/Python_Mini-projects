# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
flag=0
form = None
import math
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(f"{form}")
    canvas.itemconfig(canvas_display, text="00:00")
    label1.config(text="Timer")
    label2.config(text=""
                       "")
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global flag
    flag += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_min = LONG_BREAK_MIN*60

    if flag % 8 ==0:
        label1.config(text="Break", fg=RED)
        timer_count(long_break_min)
    elif flag % 2 ==0:
        label1.config(text="Break", fg=PINK)
        timer_count(short_break_sec)
    else:
        label1.config(text="Work",fg=GREEN)
        timer_count(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def timer_count(count):
    """to change the time of the countdown on the screen without using the time class"""
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec<10:
       count_sec = f"0{count_sec}"
    canvas.itemconfig(canvas_display, text=f"{count_min}:{count_sec}")
    if count>0:
       global form
       form = window.after(1000, timer_count, count - 1)
    else:
       start_timer()
       mark = ""
       work_session = math.floor(flag/2)
       for _ in range(work_session):
           mark += "✔"
       label2.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
from tkinter import Tk, Canvas, PhotoImage, Label, Button

window = Tk()
window.title("--Pomodoro 🍅--")
#window size can be set using padx and pady inside window.config()
window.config(padx=100,pady=50,bg=YELLOW)
#using canvas widget to put image in our window using layers
canvas = Canvas(width=200,height=240,bg=YELLOW,highlightthickness=0)
toma_img = PhotoImage(file="tomato.png")
# 102 is used to allow full image to be presented on the screen without any cuts
#toma_img is a variable used to store image format to be used ith canvas
canvas.create_image(100,120,image=toma_img)
#to place a text we use the method below with x and y coordinates accordingly
canvas_display = canvas.create_text(100,140,text="00:00",fill="white",font=("Courier",35,"bold"))
canvas.grid(column=1,row=1)

label1 = Label(text="Timer", fg=GREEN, bg=YELLOW, font=("Courier", 30, "bold"))
label1.grid(column=1, row=0)
label2 =Label(text="✔",fg=GREEN,bg=YELLOW)
label2.grid(column=1,row=3)

#use of higlightthickness() to remove any white border that may be appearing around our buttons
button1 = Button(text=" Start ",highlightthickness=0,command=start_timer)
button1.grid(column=0,row=3)
button2 = Button(text=" Reset ",highlightthickness=0,command=reset_timer)
button2.grid(column=2,row=3)


window.mainloop()
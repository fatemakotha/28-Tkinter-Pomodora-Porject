from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "CF0A0A"
GREEN = "#2B7A0B"
YELLOW = "#f7f5dd"
BLACK = "black"
ORANGE = "#DC5F00"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer) #we can only pass a variable in after_cancel(), so we name our after() function as timer = after() **
    #change timer_text:
    canvas.itemconfig(timer_text, text = "00:00")
    #change title_label to "Timer":
    title_label.config(text="Timer")
    #reset check_marks:
    check_marks.config(text="")
    #set reps to 0:
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1 #reps increase by 1 everytime the loop runs **

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    #If it's the 8th rep: **
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=RED)
    # If it's the 2nd/4th/6th rep: **
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Short Break", fg=PINK)
    # If it's the 1st/3rd/5th/7th rep: **
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """#Let's say we start from 245 mins. Then 245 / 60 = 4.083 MINS, which means 4MINS and 0.083SECS
       #Now if we do 245 % 60 = 5
       #Now every time the loops runs, the count_min and count_secs DECREASES by 1"""

    count_min = math.floor(count / 60) #math.floor() returns the largest whole number that is less <= x. IN THIS CASE ITS 4 **
    count_seconds = count % 60 #gives the remainder number of seconds WHICH IS 5 **
    #when count_seconds = 0, it's assigned to a string that's "00" using DYNAMIC TYPING
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    if count_seconds == 0:
        count_seconds = "00"

    #Changing an item in canvas is different than changing a Label: **
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_seconds}") #timer_text is the name of the item to be configured, and text is what it is to be configured into
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1) #starts after 1000ms and starts from 5, as count_down(5) is given as input. And decreases by 1
    elif count == 0:
        start_timer() #activates timer again after 1 rep **********
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions): #reps / 2 give the number of work sessions as there is one work one break in every rep
            marks += "✅"
        check_marks.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
#Creating a window:
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=BLACK) #bg changes background color


#Create a canvas using the canvas widget:
canvas = Canvas(width=200, height=224, bg=BLACK, highlightthickness=0) #bg changes background color #highlightthickness=0 removes the white border of canvas ***
#Putting an image in the background:
#Add image to canvas:
tomato_img = PhotoImage(file="tomato - Copy (2).png") #PhotoImage reads through a file and gets hold of an image
canvas.create_image(100, 112, image=tomato_img) #inserts image to the background at the x=12 and y=112
#Create text in canvas:
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")) #inserts text to the background at the x=12 and y=130
canvas.grid(column=1, row=1) #calls the canvas function to display


#Creating the "Timer" Label:
title_label = Label(text="Timer", fg=GREEN, bg=BLACK, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)


#Creating the START Button:
start_button = Button(text="Start", width=8, bg=ORANGE, fg="white", font=(FONT_NAME, 15, "bold"), command=start_timer)
start_button.grid(column=0, row=2)


#Creating the STOP Button:
reset_button = Button(text="Reset", width=8, bg=ORANGE, fg="white", font=(FONT_NAME, 15, "bold"), command=reset_timer)
reset_button.grid(column=2, row=2)


#Check mark Label:
check_marks = Label(text="", fg=GREEN, bg=BLACK, font=(FONT_NAME, 15, "bold"))
check_marks.grid(column=1, row=2)




window.mainloop()




























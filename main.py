from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "CF0A0A"
GREEN = "#2B7A0B"
YELLOW = "#f7f5dd"
BLACK = "black"
ORANGE = "#DC5F00"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
#You could do this using the following code:
# import time
# count = 5
# while True:
#     time.sleep(1)
#     count -= 1 #BUT SINCE window.mainloop() is ALREADY A LOOP, this WON'T WORK !! ****

#SO INSETAD WE DO THIS:
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    print(count)
    if count > 0:
        window.after(1000, count_down, count - 1) #starts after 1000ms and starts from 5, as count_down(5) is given as input. And decreases by 1







# ---------------------------- UI SETUP ------------------------------- #
#Creating a window:
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=BLACK) #bg changes background color
count_down(5) #starts at 5 seconds and then counts down **




#Create a canvas using the canvas widget:
canvas = Canvas(width=200, height=224, bg=BLACK, highlightthickness=0) #bg changes background color #highlightthickness=0 removes the white border of canvas ***
#Putting an image in the background:
#Add image to canvas:
tomato_img = PhotoImage(file="tomato - Copy (2).png") #PhotoImage reads through a file and gets hold of an image
canvas.create_image(100, 112, image=tomato_img) #inserts image to the background at the x=12 and y=112
#Create text in canvas:
canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")) #inserts text to the background at the x=12 and y=130
canvas.grid(column=1, row=1) #calls the canvas function to display

#Creating the "Timer" Label:
title_label = Label(text="Timer", fg=GREEN, bg=BLACK, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)


#Creating the START Button:
start_button = Button(text="Start", width=8, bg=ORANGE, fg="white", font=(FONT_NAME, 15, "bold"))
start_button.grid(column=0, row=2)


#Creating the STOP Button:
reset_button = Button(text="Stop", width=8, bg=ORANGE, fg="white", font=(FONT_NAME, 15, "bold"))
reset_button.grid(column=2, row=2)

#Check mark Label:
check_marks = Label(text="✅", fg=GREEN, bg=BLACK, font=(FONT_NAME, 15, "bold"))
check_marks.grid(column=1, row=2)




window.mainloop()




























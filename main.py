from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "CF0A0A"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLACK = "000000"
ORANGE = "DC5F00"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
#Creating a window:
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50)

#Putting an image in the background:
#Create a canvas using the canvas widget:
canvas = Canvas(width=200, height=224)

#Add image to canvas:
tomato_img = PhotoImage(file="tomato - Copy (2).png") #PhotoImage reads through a file and gets hold of an image
canvas.create_image(102, 112, image=tomato_img) #inserts image to the background at the x=12 and y=112

#Create text in canvas:
canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")) #inserts text to the background at the x=12 and y=130
canvas.pack() #calls the canvas function to display











window.mainloop()




























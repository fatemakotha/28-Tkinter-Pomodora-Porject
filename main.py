from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
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

#Putting an image in the background:
#Create a canvas using the canvas widget:
canvas = Canvas(width=200, height=224)
#Add image to canvas:
tomato_img = PhotoImage(file="tomato - Copy (2).png") #PhotoImage reads through a file and gets hold of an image
canvas.create_image(100, 112, image=tomato_img) #inserts image to the background
canvas.pack() #calls the canvas function to display











window.mainloop()




























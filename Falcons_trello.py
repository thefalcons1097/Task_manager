
from tkinter import *
import os
import random

window = Tk()
window.title("The Falcons's trello")
window['background']='#51a4d5'
y = 70
on_screen = FALSE
screen_width = 1920
screen_height = 1080


def create_entry_box():
    global on_screen, on_screen,entry,sumbit_button
    if not on_screen:

        entry = Entry(window, font=('Arial black',15,'bold'))
        entry.pack(side=RIGHT)
        sumbit_button = Button(text='sumbit',command=sumbit)
        sumbit_button.place(x=1600,y=screen_height//2 - 22.5)
        on_screen = TRUE

        
def create_task_label(name):
    global y
    if name != '':
        label_task = Label(text=name, font=('Arial',13,'bold'),background='black',fg='#00FF00')
        label_task.place(x=10, y=y)
        y += 34
        entry.destroy()
        sumbit_button.destroy()
        on_screen = TRUE
    

def sumbit():
    global name,on_screen
    task_name = entry.get()
    create_task_label(task_name)
    on_screen = FALSE

def create_task():
    create_entry_box()

window.geometry(f"{str(screen_width)}x{str(screen_height)}")

label = Label(text='Tasks',background='black',fg='#00FF00', font=('Arial',31,'bold'))
label.place(x=10)

button = Button(text='add tasks', command=create_task, background='black',fg='#00FF00', font=('Arial',17,'bold'))
button.place(x=screen_width // 2)

window.mainloop()
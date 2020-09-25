import time
import tkinter as tk
from tkinter import *


root=Tk()
root.geometry("500x200+0+0")
root.title("Real-time Digital Clock")
clock_frame=Label(root,font=('times',100,'bold'),bg='black',fg='red')
clock_frame.pack(fill='both',expand=1)
def ticks(time1=""):
    # Get the curreent local time from the system
    time2= time.strftime('%A\n%I:%M:%S\n%D')
    # if the time string has changes, update it
    if time2 !=time1:
        time1=time2
        clock_frame.config(text=time2)
        # calls itself every 200 milliseconds to update 
        clock_frame.after(200,ticks)

ticks()
mainloop()




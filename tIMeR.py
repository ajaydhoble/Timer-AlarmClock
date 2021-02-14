# ************* IMPORTING MODULES ************
import time
import tkinter
from tkinter import *
from tkinter import messagebox

# **************** BASIC GUI *************
wind = tkinter.Tk()
wind.title("Timer")
wind.geometry("400x400")
wind.configure(bg="CadetBlue")
wind.resizable(width=False, height=False)

# *************** FOR HOLDING TEXT *********
hour_txt = StringVar()
hour_txt.set("00")
min_txt = StringVar()
min_txt.set("00")
sec_text = StringVar()
sec_text.set("00")


def timer():  # **************FUNCTION FOR TIMER ********
    total_sec = int(hour_txt.get()) * 3600 + int(min_txt.get()) * 60 + int(sec_text.get())
    while total_sec:
        mins, secs = divmod(total_sec, 60)
        hrs, mins = divmod(mins, 60)
        hour_txt.set(hrs)
        min_txt.set(mins)
        sec_text.set(secs)
        wind.update()
        time.sleep(1)
        total_sec -= 1
        if total_sec == 0:
            messagebox.showinfo("Timer", "Times up!!")
            break


# ************** LABELS & BUTTONS ********
Hours_Label = tkinter.Label(wind, text="Hour", font="Ubuntu 20", bg="DarkSlateGrey", bd=5, relief=SUNKEN)
Hours_Label.place(x=50, y=20)
hours = tkinter.Entry(wind, bd=3, font="Calibri 20", textvariable=hour_txt, bg="Grey")
hours.place(x=70, y=70, width=45, height=70)

Minutes_Label = tkinter.Label(wind, text="Minute", font="Ubuntu 20", bg="DarkSlateGrey", bd=5, relief=SUNKEN)
Minutes_Label.place(x=145, y=20)
minutes = tkinter.Entry(wind, bd=3, font="Calibri 20", textvariable=min_txt, bg="Grey")
minutes.place(x=170, y=70, width=45, height=70)

Seconds_Label = tkinter.Label(wind, text="Second", font="Ubuntu 20", bg="DarkSlateGrey", bd=5, relief=SUNKEN)
Seconds_Label.place(x=253, y=20)
seconds = tkinter.Entry(wind, bd=3, font="Calibri 20", textvariable=sec_text, bg="Grey")
seconds.place(x=270, y=70, width=45, height=70)

start_button = tkinter.Button(wind, text="START TIMER", command=timer, bg="Grey", fg="green", relief=GROOVE)
start_button.place(x=150, y=250)

wind.mainloop()

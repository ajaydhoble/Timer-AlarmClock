import time
import tkinter
from tkinter import *
from tkinter import messagebox
import winsound
import datetime

wind = tkinter.Tk()
wind.title("Alarm Clock")
wind.geometry("400x400")
wind.configure(bg="CadetBlue")
wind.resizable(width=False, height=False)

hour_txt = StringVar()
hour_txt.set("00")

min_txt = StringVar()
min_txt.set("00")

sec_text = StringVar()
sec_text.set("00")


def alarm_clock():
    while True:
        alarm_time = hour_txt.get() + "," + min_txt.get() + "," + sec_text.get()
        # print(alarm_time)
        time.sleep(1)
        curr_time = datetime.datetime.now().strftime("%H,%M,%S")
        # print(curr_time)
        if curr_time == alarm_time:
            winsound.Beep(500, 2000)
            time.sleep(3)
            messagebox.showinfo("Alarm Clock", "Time UP!!")
            break


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

start_button = tkinter.Button(wind, text="SET ALARM", command=alarm_clock, bg="Grey", fg="green", relief=GROOVE)
start_button.place(x=150, y=250)

wind.mainloop()

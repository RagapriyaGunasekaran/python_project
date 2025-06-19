from tkinter import *
import datetime
import time
import winsound
from threading import *
import os

root = Tk()
root.geometry("400x200")
root.title("Alarm Clock")

def Threading():
    t1 = Thread(target=alarm)
    t1.start()

def alarm():
    while True:
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)
        if current_time == set_alarm_time:
            print("Time to Wake up")
            if os.path.exists("sound.wav"):
                winsound.PlaySound("sound.wav", winsound.SND_ASYNC | winsound.SND_FILENAME)
            else:
                print("Sound file not found!")
            break

Label(root, text="Alarm Clock", font=("Helvetica 20 bold"), fg="red").pack(pady=10)
Label(root, text="Set Time", font=("Helvetica 15 bold")).pack()

frame = Frame(root)
frame.pack()

hour = StringVar(root)
hours = tuple(f"{i:02}" for i in range(24))
hour.set(hours[0])
OptionMenu(frame, hour, *hours).pack(side=LEFT)

minute = StringVar(root)
minutes = tuple(f"{i:02}" for i in range(60))
minute.set(minutes[0])
OptionMenu(frame, minute, *minutes).pack(side=LEFT)

second = StringVar(root)
seconds = tuple(f"{i:02}" for i in range(60))
second.set(seconds[0])
OptionMenu(frame, second, *seconds).pack(side=LEFT)

Button(root, text="Set Alarm", font=("Helvetica 15"), command=Threading).pack(pady=20)

root.mainloop()

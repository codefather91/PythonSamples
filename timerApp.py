# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 10:05:14 2019

@author: kanavgulati
"""

import tkinter as tk
from tkinter import messagebox as mb

hourCounter=0
minCounter=0
secCounter=0
stopCounter=0

def showinfo():
    mb.showinfo(title="About", message="Countdown Timer using Tkinter by KVG.\nv1 Dec 2019")

def addHour():
    global hourCounter
    if hourCounter == 23:
        hourCounter = 0
    else:
        hourCounter+=1
    if hourCounter < 10:
        hourLabel.config(text="0"+str(hourCounter))
    else:
        hourLabel.config(text=str(hourCounter))

def addMinute():
    global minCounter
    if minCounter == 59:
        minCounter = 0
    else:
        minCounter+=1
    if minCounter < 10:
        minLabel.config(text="0"+str(minCounter))
    else:
        minLabel.config(text=str(minCounter))
        
def addSecond():
    global secCounter
    if secCounter == 59:
        secCounter = 0
    else:
        secCounter+=1
    if secCounter < 10:
        secLabel.config(text="0"+str(secCounter))
    else:
        secLabel.config(text=str(secCounter))

def timer_reset():
    global hourCounter
    global minCounter
    global secCounter
    global stopCounter
    hourCounter = 0
    minCounter = 0
    secCounter = 0
    stopCounter = 0
    hourLabel.config(text="00")
    minLabel.config(text="00")
    secLabel.config(text="00")
    appStatus.config(text="Timer Ready")

def timer_flag():
    global stopCounter
    stopCounter = 1

def timer_stop():
    global hourCounter
    global minCounter
    global secCounter
    global stopCounter
    if hourCounter < 10:
        hourLabel.config(text="0"+str(hourCounter))
    else:
        hourLabel.config(text=str(hourCounter))
    if minCounter < 10:
        minLabel.config(text="0"+str(minCounter))
    else:
        minLabel.config(text=str(minCounter))
    if secCounter < 10:
        secLabel.config(text="0"+str(secCounter))
    else:
        secLabel.config(text=str(secCounter))
    appStatus.config(text="Timer Stopped")
    if hourCounter == 0 and minCounter == 0 and secCounter == 0:
        appStatus.config(text="Time's up!")
        mb.showinfo(title="Info", message="Time's up!")
        print("\a")

def timer_run():
    global stopCounter
    appStatus.config(text="Timer running...")
    if stopCounter == 0 and (hourCounter > 0 or minCounter > 0 or secCounter > 0):
        countdown_sec()
    else:
        timer_stop()

def countdown_hours():
    global hourCounter
    global minCounter
    global secCounter
    if hourCounter > 0:
        hourCounter-=1
        minCounter = 59
        secCounter = 59
    else:
        timer_stop()
    if hourCounter < 10:
        hourLabel.config(text="0"+str(hourCounter))
    else:
        hourLabel.config(text=str(hourCounter))
    if minCounter < 10:
        minLabel.config(text="0"+str(minCounter))
    else:
        minLabel.config(text=str(minCounter))
    if secCounter < 10:
        secLabel.config(text="0"+str(secCounter))
    else:
        secLabel.config(text=str(secCounter))

def countdown_min():
    global minCounter
    global secCounter
    if minCounter > 0:
        minCounter-=1
        secCounter = 59
    else:
        countdown_hours()
    if minCounter < 10:
        minLabel.config(text="0"+str(minCounter))
    else:
        minLabel.config(text=str(minCounter))
    if secCounter < 10:
        secLabel.config(text="0"+str(secCounter))
    else:
        secLabel.config(text=str(secCounter))

def countdown_sec():
    global secCounter
    if secCounter > 0:
        secCounter-=1
    else:
        countdown_min()
    if secCounter < 10:
        secLabel.config(text="0"+str(secCounter))
    else:
        secLabel.config(text=str(secCounter))
    secLabel.after(1000, func=timer_run)

root = tk.Tk()
root.geometry('320x240')
root.title("Countdown Timer v1")

mainmenu = tk.Menu(root)
AboutMenu = tk.Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="About", menu=AboutMenu)
AboutMenu.add_command(label="About Timer", command=showinfo)
mainmenu.add_separator()
AboutMenu.add_command(label="Exit", command=root.destroy)
root.config(menu=mainmenu)

mainCanvas = tk.Frame(root, bg="white")

hourLabel = tk.Label(mainCanvas, text="00", fg="green", bg="black", font=("Courier",50), padx=5, pady=5)
hourLabel.grid(row=0, column=0, padx=5, pady=5)

minLabel = tk.Label(mainCanvas, text="00", fg="green", bg="black", font=("Courier",50), padx=5, pady=5)
minLabel.grid(row=0, column=1, padx=5, pady=5)

secLabel = tk.Label(mainCanvas, text="00", fg="green", bg="black", font=("Courier",50), padx=5, pady=5)
secLabel.grid(row=0, column=2, padx=5, pady=5)

addHour = tk.Button(mainCanvas, text="Add Hour", command=addHour, width=10, height=2, padx=2, pady=5, bd=2, bg="gray", fg="black")
addHour.grid(row=1, column=0, padx=5, pady=5)
addMin = tk.Button(mainCanvas, text="Add Minute", command=addMinute, width=10, height=2, padx=2, pady=5, bd=2, bg="gray", fg="black")
addMin.grid(row=1, column=1, padx=5, pady=5)
addSec = tk.Button(mainCanvas, text="Add Second", command=addSecond, width=10, height=2, padx=2, pady=5, bd=2, bg="gray", fg="black")
addSec.grid(row=1, column=2, padx=5, pady=5)

startButton = tk.Button(mainCanvas, text="Start Timer", command=timer_run, width=10, height=2, padx=2, pady=5, bd=2, bg="green", fg="black")
startButton.grid(row=2, column=0, padx=5, pady=5)

stopButton = tk.Button(mainCanvas, text="Stop Timer", command=timer_flag, width=10, height=2, padx=2, pady=5, bd=2, bg="red", fg="black")
stopButton.grid(row=2, column=1, padx=5, pady=5)

resetButton = tk.Button(mainCanvas, text="Reset Timer", command=timer_reset, width=10, height=2, padx=2, pady=5, bd=2, bg="black", fg="white")
resetButton.grid(row=2, column=2, padx=5, pady=5)

mainCanvas.pack()

appStatus = tk.Label(root, text="Timer Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
appStatus.pack(side=tk.BOTTOM, fill=tk.X)

root = tk.mainloop()

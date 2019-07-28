#!/usr/bin/python3

import tkinter as tk
from time import time
from time import sleep


WORK_TIME = 1200  # 20 minutes
BREAK_TIME = 30  # 30 seconds (20 seconds look + 10 seconds thinking time)
POSTPONE_TIME = 120  # 2 minutes

breakStart = time()
breakEnd = time()
currentPostpone = 0

running = True
currentWindow = "start"


def main():
    global running
    global currentWindow
    print("[STARTING] 20eyes")

    while running:
        if currentWindow == "start":
            startGUI()
        elif currentWindow == "timeElapsed":
            timeElapsedGUI()
        elif currentWindow == "breakElapsed":
            breakElapsedGUI()

        elif currentWindow == "running":
            timeRemaining = (breakEnd + WORK_TIME + currentPostpone) - time()
            print(f"WORK time remaining: {round(timeRemaining)} seconds")
            if (breakEnd + WORK_TIME + currentPostpone) <= time():
                currentWindow = "timeElapsed"
            sleep(1)
        elif currentWindow == "breakRunning":
            timeRemaining = (breakStart + BREAK_TIME) - time()
            print(f"BREAK time remaining: {round(timeRemaining)} seconds")
            if (breakStart + BREAK_TIME) <= time():
                currentWindow = "breakElapsed"
            sleep(1)

    print("[STOPPED] 20eyes")


def exitCallback(top):
    global running
    running = False
    top.destroy()


def startCallback(top):
    global currentWindow
    global breakEnd
    currentWindow = "running"
    breakEnd = time()
    top.destroy()


def startBreakCallback(top):
    global currentWindow
    global breakStart
    currentWindow = "breakRunning"
    breakStart = time()
    top.destroy()


def postponeCallback(top):
    global currentWindow
    global currentPostpone
    global breakEnd
    currentWindow = "running"
    breakEnd = time() - WORK_TIME + currentPostpone
    currentPostpone += POSTPONE_TIME
    print(f"Postponed for {POSTPONE_TIME} minutes")
    top.destroy()


def startGUI():
    top = tk.Tk()
    top.title("")
    top.geometry("200x80")

    tk.Label(top, text="20eyes - take care of your eyes").place(x=20, y=10)
    tk.Button(top, text="start work", command=lambda: startCallback(top)).place(x=25, y=40)
    tk.Button(top, text="exit", command=lambda: exitCallback(top)).place(x=120, y=40)

    top.mainloop()


def timeElapsedGUI():
    top = tk.Tk()
    top.title("")
    top.lift()
    top.geometry("300x100")

    tk.Label(top, text=f"20eyes - {WORK_TIME/60} minutes worked + {currentPostpone/60} minutes postponed").place(x=3, y=10)
    tk.Label(top, text=f"Look 20 feet (6 meters) away for 20 seconds :)").place(x=28, y=30)
    tk.Button(top, text="start break", command=lambda: startBreakCallback(top)).place(x=25, y=60)
    tk.Button(top, text=f"postpone {POSTPONE_TIME/60} min", command=lambda: postponeCallback(top)).place(x=115, y=60)
    tk.Button(top, text="exit", command=lambda: exitCallback(top)).place(x=245, y=60)

    top.mainloop()


def breakElapsedGUI():
    top = tk.Tk()
    top.title("")
    top.lift()
    top.geometry("200x80")

    tk.Label(top, text=f"20eyes - {BREAK_TIME} seconds break elapsed").place(x=10, y=10)
    tk.Button(top, text="start work", command=lambda: startCallback(top)).place(x=25, y=40)
    tk.Button(top, text="exit", command=lambda: exitCallback(top)).place(x=120, y=40)

    top.mainloop()


if __name__ == '__main__':
    main()
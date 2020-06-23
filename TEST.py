import winsound
import os
import time
import sys
import turtle as tk
os.chdir('C:\\teleport\\Code\\Multi-Snake')
def play():
    global running
    running = True
    while running:
        winsound.PlaySound("themesong.wav", winsound.SND_ASYNC)
        time.sleep(7)

def stop():
    global running
    running = False
    sys.exit()

import tkinter as tk
from turtle import RawTurtle, TurtleScreen, ScrolledCanvas

root = tk.Tk()
root.attributes("-alpha", 0.3)


root.mainloop()

#Multi-Snake
#credits.py

#NOTE: (delete after reading) go here for the main window: https://www.youtube.com/watch?v=C-t0nZ_8HeE
#import modules and scripts needed
import tkinter
from time import *
from tkinter import *



#getOUT
def getOUT():
      root1.destroy()

names = ['Justin Ge', 'Brian Wiggins', 'Max Vandershaaf', 'and Python (the programming language)', ' ']

#GUI('s)
def guiBack():
    global root1

    root1 = Tk()

    root1.title('Multi-Snake Credits')

    #set the color
    root1.config(bg='black')

    root1.attributes('-fullscreen', True)

    cred = Label(root1, text='Credits:')
    cred.config(fg='white', bg='black')
    cred.config(font=('Helvetica', 40))
    cred.pack()

    name = Label(root1)
    name.config(fg='white', bg='black')
    name.config(font=('Helvetica', 35))
    name.pack()

    for i in range(len(names)):
        name['text']=names[i]
        root1.update()
        sleep(4)

    cred.pack_forget()

    exi = Button(root1, text='Back', command=getOUT)
    exi.config(fg='black', bg='white')
    exi.config(font=('Helvetica', 20))
    exi.pack(side=BOTTOM)


    root1.mainloop()

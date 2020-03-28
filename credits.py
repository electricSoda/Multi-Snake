#Multi-Snake
#credits.py

#NOTE: (delete after reading) go here for the main window: https://www.youtube.com/watch?v=C-t0nZ_8HeE
#import modules and scripts needed
import tkinter
from time import *
from tkinter import *
import tkHyperlinkManager
import webbrowser

#GUI('s)
def guiBack():
    global root1, icon

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
        sleep(2)

    cred.pack_forget()
    name.pack_forget()

    linkCredits = Label(root1, text = 'Credits with Links')
    linkCredits.config(fg='white', bg='black')
    linkCredits.config(font=('Helvetica', 35))
    linkCredits.pack()


    #icon1
    icon1 = Text(root1)

    #hyper links
    hyperlink = tkHyperlinkManager.HyperlinkManager(icon1)

    icon1.pack()
    icon1.insert(INSERT, 'Icon made by ')
    icon1.insert(INSERT, 'monkik', hyperlink.add(monkik))
    icon1.insert(INSERT, '\n')
    icon1.insert(INSERT, 'Icon provided by ')
    icon1.insert(INSERT, 'flaticon.com', hyperlink.add(flaticon))
    icon1.config(state = DISABLED)

    exi = Button(root1, text='Back', command=getOUT)
    exi.config(fg='black', bg='white')
    exi.config(font=('Helvetica', 20))
    exi.pack(side=BOTTOM)


    root1.mainloop()

#getOUT
def getOUT():
      root1.destroy()

names = ['Justin Ge', 'Blank Space for kids...']

def monkik():
    webbrowser.open('https://www.flaticon.com/authors/monkik')

def flaticon():
    webbrowser.open('https://www.flaticon.com/')

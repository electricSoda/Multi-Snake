#Multi-Snake
#mainScreen.py

#print that main.py has connected
print('"main.py" has connected to all scripts')

#import modules and scripts
import game
import credits
from time import *
import tkinter
from tkinter import *

def e():
    root.resizable(height=True, width=True)
    text.pack_forget()
    te.pack_forget()
    ab.pack_forget()

    gameLabel.pack(side = TOP)
    sep.pack(side = TOP)
    play.pack(padx=5, pady=10)
    shop.pack(padx=5, pady=10)
    how.pack(padx=5, pady=10)
    credi.pack(padx=5, pady=10)
    exit1.pack(padx=5)


def instr():
    transition()
    global text, te, ab

    root.resizable(height = False, width = False)

    text = Text(root)
    text.pack()
    #put all of the text here:
    with open('instructions.txt') as ins:
        a = ins.read()
        text.insert(INSERT, a)

    ###
    text.config(state='disabled')

    te = Label(root, text='Multi-Snake')
    te.config(font=('Helvetica', 40))
    te.config(bg='white')
    te.pack()

    ab = Button(root, text='Back', command=e)
    ab.config(fg='black', bg='white')
    ab.pack(side=BOTTOM)


def transition():
    exit1.pack_forget()
    credi.pack_forget()
    how.pack_forget()
    shop.pack_forget()
    play.pack_forget()
    sep.pack_forget()
    gameLabel.pack_forget()


#terminate function
def terminate():
    root.destroy()
    quit()
    exit()

#optia function
def optia():
    credits.guiBack()

characters = ['.', '..', '...', '.', '..', '...']

#define start
def start():
    transition()

    load = Label(root, text='Loading Game')
    load.config(fg='black', bg='white')
    load.config(font=('Helvetica', 40))
    load.pack(side=TOP, padx=5, pady=10)

    for i in range(len(characters)):
        load['text']='Loading Game' + characters[i]
        root.update()
        sleep(0.2)

    load.config(text='Success!')
    root.update()

    game.oof('Starting')

#colors
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet red', 'purple', 'white',
         'red', 'orange', 'yellow', 'green', 'blue', 'violet red', 'purple', 'white',
         'red', 'orange', 'yellow', 'green', 'blue', 'violet red', 'purple', 'white',
         ]

#rainbow
def rainbow():
    for i in range(len(colors)):
        root.config(bg=colors[i])
        root.update()
        sleep(1)


#scriptGot function
def scriptGot(event):
    got = content.get()
    if got == 'hinghong':
        rainbow()


def easter(event):
    global content

    content = StringVar()
    entity = Entry(root, textvariable = content)
    #bindings
    entity.bind('<Return>', scriptGot)
    entity.pack()
    bool = True





#start the main screen ( or the play and options screen)

def startScrn(name, bag):
    #set global variables
    global root, exit1, credi, how, shop, play, sep, gameLabel, log, bool

    #root
    root = Tk()

    #setting width and height
    w = 800
    h = 740

    #set the color
    root.config(bg=bag)

    #get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()

    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    # set the dimensions of the screen and where it is placed
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #minsize
    root.minsize(800, 740)

    #set title
    root.title(name)

    #initial code

    gameLabel = Label(root, text=name)
    gameLabel.config(font=("Helvetica", 60))
    gameLabel.config(fg='green', bg='light green')
    gameLabel.pack(side=TOP)

    sep1 = '->' * 21

    sep = Label(root, text=sep1)
    sep.config(font=("Helvetica", 60))
    sep.config(fg='green', bg='light green')
    sep.pack(side=TOP)

    play = Button(root, text='▓  Play  ▓', command=start)
    play.config(font=("Comic Sans MS", 45))
    play.config(fg='light green', bg='dark green')
    play.pack(padx=5, pady=10)

    shop = Button(root, text='▓ Shop [Coming Soon!] ▓')
    shop.config(font=("Comic Sans MS", 30))
    shop.config(fg='yellow', bg='purple')
    shop.config(state=DISABLED)
    shop.pack(padx=5, pady=10)

    how = Button(root, text='▓ How To Play ▓', command = instr)
    how.config(font=("Comic Sans MS", 25))
    how.config(fg='light blue', bg='dark blue')
    how.pack(padx=5, pady=10)

    credi = Button(root, text='▓ Credits ▓', command=optia)
    credi.config(font=("Comic Sans MS", 25))
    credi.config(fg='light grey', bg='black')
    credi.pack(padx=5, pady=10)

    exit1 = Button(root, text='▓ Exit ▓', command=terminate)
    exit1.config(font=("Comic Sans MS", 20))
    exit1.config(fg='white', bg='dark red')
    exit1.pack(padx=5)

    #root bindings
    root.bind('<Control-b>', easter)

    #mainloop
    root.mainloop()

    return

def hinghong(of):
    print(of, 'is a HINGHONG')

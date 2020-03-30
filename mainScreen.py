#Multi-Snake
#mainScreen.py

#print that main.py has connected
print('"main.py" has connected to all scripts')

#import modules and scripts
#import game
import credits
import winsound
from time import *
import tkinter
from tkinter import *
import webbrowser
import tkHyperlinkManager
import game

def link():
    webbrowser.open('https://www.example.com')

def e():
    root.resizable(height=True, width=True)
    text.pack_forget()
    te.pack_forget()
    ab.pack_forget()

    gameLabel.pack(side = TOP)
    sep.pack(side = TOP)
    play.pack(padx=5, pady=10)
    shop.pack(padx=5, pady=10)
    stats.pack(padx=5, pady=10)
    how.pack(padx=5, pady=10)
    credi.pack(padx=5, pady=10)
    exit1.pack(padx=5)

def e2():
    root.resizable(height=True, width=True)
    st.pack_forget()
    bb.pack_forget()

    gameLabel.pack(side = TOP)
    sep.pack(side = TOP)
    play.pack(padx=5, pady=10)
    shop.pack(padx=5, pady=10)
    stats.pack(padx=5, pady=10)
    how.pack(padx=5, pady=10)
    credi.pack(padx=5, pady=10)
    exit1.pack(padx=5)


def instr():
    transition()
    global text, te, ab

    root.resizable(height = False, width = False)

    text = Text(root)
    text.pack()

    hyperlink = tkHyperlinkManager.HyperlinkManager(text)

    #put all of the text here:
    with open('instructions.txt') as ins:
        a = ins.read()
        text.insert(INSERT, a)

    text.insert(INSERT, 'example.com', hyperlink.add(link))

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
    stats.pack_forget()


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

    root.destroy()
    game.snake()


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
        try:
            rainbow()
        except:
            pass
    elif got == 'whoopwhoop':
        #print("Whoop! Whoop! It's the sound of de police!")
        winsound.PlaySound('Sound-Of-The-Police.wav', winsound.SND_ASYNC)
    elif got == 'glitchreturn':
        root.config(bg='white')
    else:
        print('U SUCK')

#twenty_one
twenty_one = 21
#start the main screen

def startScrn(name, bag):
    #set global variables
    global root, exit1, credi, how, shop, play, sep, gameLabel, log, make, sep1, stats

    #root
    root = Tk()

    #setting width and height
    w = 800
    h = 700

    #set the color
    root.config(bg=bag)

    #set icon
    root.iconbitmap(r'snake_icon.ico')

    #get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()

    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    # set the dimensions of the screen and where it is placed
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #minsize
    root.minsize(800, 700)

    #set title
    root.title(name)

    #local functions
    def stats():
        global st, bb

        transition()

        root.resizable(height = False, width = False)

        st = Label(root, text='Game Stats')
        st.config(font=('Helvetica', 45, 'bold', 'underline'))
        st.config(bg='white')
        st.pack(side=TOP)



        bb = Button(root, text='Back', command=e2)
        bb.pack(side=BOTTOM)

    #initial code

    gameLabel = Label(root, text=name)
    gameLabel.config(font=("Helvetica", 50))
    gameLabel.config(fg='green', bg='light green')
    gameLabel.pack(side=TOP)

    sep1 = '->' * twenty_one

    sep = Label(root, text=sep1)
    sep.config(font=("Helvetica", 45))
    sep.config(fg='green', bg='light green')
    sep.pack(side=TOP)

    play = Button(root, text='▓  Play  ▓', command=start)
    play.config(font=("Comic Sans MS", 35))
    play.config(fg='light green', bg='dark green')
    play.pack(padx=5, pady=10)

    shop = Button(root, text='▓ Shop [Coming Soon!] ▓')
    shop.config(font=("Comic Sans MS", 25))
    shop.config(fg='yellow', bg='purple')
    shop.config(state=DISABLED)
    shop.pack(padx=5, pady=10)

    stats = Button(root, text='▓ Stats ▓', command=stats)
    stats.config(font=('Comic Sans MS', 25))
    stats.config(fg='white', bg='blue')
    stats.pack(padx=5, pady=10)

    how = Button(root, text='▓ How To Play ▓', command = instr)
    how.config(font=("Comic Sans MS", 18))
    how.config(fg='light blue', bg='dark blue')
    how.pack(padx=5, pady=10)

    credi = Button(root, text='▓ Credits ▓', command=optia)
    credi.config(font=("Comic Sans MS", 18))
    credi.config(fg='light grey', bg='black')
    credi.pack(padx=5, pady=10)

    exit1 = Button(root, text='▓ Quit Game ▓', command=terminate)
    exit1.config(font=("Comic Sans MS", 18))
    exit1.config(fg='white', bg='dark red')
    exit1.pack(padx=5)


    make = False
    #root bindings
    root.bind('<Control-b>', easter)

    #mainloop
    root.mainloop()

    return


def easter(event):
    global content, make, entity

    if not make:
        content = StringVar()
        entity = Entry(root, textvariable = content)
        #bindings
        entity.bind('<Return>', scriptGot)
        entity.pack()
        make = True
    else:
        entity.pack_forget()
        make = False

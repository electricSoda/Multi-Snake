#Multi-Snake
#credits.py

#NOTE: (delete after reading) go here for the main window: https://www.youtube.com/watch?v=C-t0nZ_8HeE
#import modules and scripts needed
import tkinter
from tkinter import *



#getOUT
def getOUT():
      root1.destroy()
      


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

      name = Label(root1, text='Justin Ge')
      name.config(fg='white', bg='black')
      name.config(font=('Helvetica', 35))
      name.pack()

      name1 = Label(root1, text='Brian Wiggins')
      name1.config(fg='white', bg='black')
      name1.config(font=('Helvetica', 35))
      name1.pack()

      name2 = Label(root1, text='Max Vandershaf')
      name2.config(fg='white', bg='black')
      name2.config(font=('Helvetica', 35))
      name2.pack()

      exi = Button(root1, text='Back', command=getOUT)
      exi.config(fg='black', bg='white')
      exi.pack(side=BOTTOM)


      root1.mainloop()

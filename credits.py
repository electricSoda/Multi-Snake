#Multi-Snake
#credits.py

#NOTE: (delete after reading) go here for the main window: https://www.youtube.com/watch?v=C-t0nZ_8HeE
#import modules and scripts needed
import tkinter
from tkinter import *
import mixer
import time


#getOUT
def getOUT():
      root.destroy()
      exit()
      quit()


#GUI('s)
def guiBack():
      global root

      mixer.pla()
      
      root = Tk()

      root.title('Multi-Snake Credits')

      #set the color
      root.config(bg='black')

      root.attributes('-fullscreen', True)

      cred = Label(root, text='Credits:')
      cred.config(fg='white', bg='black')
      cred.config(font=('Helvetica', 40))
      cred.pack()

      name = Label(root, text='Justin Ge')
      name.config(fg='white', bg='black')
      name.config(font=('Helvetica', 35))
      name.pack()

      name1 = Label(root, text='Brian Wiggins')
      name1.config(fg='white', bg='black')
      name1.config(font=('Helvetica', 35))
      name1.pack()
      
      name2 = Label(root, text='Max Vandershaf')
      name2.config(fg='white', bg='black')
      name2.config(font=('Helvetica', 35))
      name2.pack()

      exi = Button(root, text='Back', command=getOUT)
      exi.config(fg='black', bg='white')
      exi.pack(side=BOTTOM)
            
      
      root.mainloop()



#to be deleted (only used for testing)
guiBack()

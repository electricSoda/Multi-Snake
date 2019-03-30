#Multi-Snake
#doc.py

#this is the document of how to properly play the game of multi-snake

#import libraries scripts etc.
import tkinter
from tkinter import *

def main():
      root = Tk()

      root.title('How to play')

      root.geometry('600x650')
      root.resizable(height=False, width=False)

      root.config(bg='white')

      
      text = Text(root)
      text.pack()
      #put all of the text here:
      with open('instructions.txt') as ins:
            a = ins.read()
            text.insert(INSERT, a)

      ###
      text.config(state='disabled')

      root.mainloop()

main()

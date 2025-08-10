from tkinter import *
from tkinter import messagebox
Windows=Tk()
Windows.title('Event handler')
Windows.geometry('200x200')
b1=Button(text='click on me',fg='black',bg='yellow')
b1.pack()


def msg():
    messagebox.askquestion("questionbox","do you want to continue")
def ehv(event):
    
    print('the button has been click')
b1.bind("<Button-1>",ehv)
b1=Button(text='click on me',fg='black',bg='yellow',command=msg)
b1.pack()

Windows.mainloop()
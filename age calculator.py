from tkinter import *
Window=Tk()
Window.title
Window.geometry('500x400')
Window.configure(bg='blue')

L1=Label(text='Age calculator app',fg='black',bg='grey',height=2,width=15)
L2=Label(text='Name',fg='black',bg='grey',height=2,width=20)
L3=Label(text='Date',fg='black',bg='grey',height=2,width=20)
L4=Label(text='Month',fg='black',bg='grey',height=2,width=20)
L5=Label(text='Year',fg='black',bg='grey',height=2,width=20)

e1=Entry(bg='grey',fg='white',width=25)
e2=Entry(bg='grey',fg='white',width=25)
e3=Entry(bg='grey',fg='white',width=25)
e4=Entry(bg='grey',fg='white',width=25)

b1=Button(text='calculator',fg='grey',bg='white',height=2,width=10)

L1.pack()
L2.pack()
L3.pack()
L4.pack()
L5.pack()
e1.pack()
e2.pack()
e3.pack()
e4.pack()
b1.pack()

L2.place(x=20,y=100)
L3.place(x=20,y=150)
L4.place(x=20,y=200)
L5.place(x=20,y=250)

e1.place(x=300,y=100)
e2.place(x=300,y=150)
e3.place(x=300,y=200)
e4.place(x=300,y=250)

b1.place(x=200,y=315)

Window.mainloop()
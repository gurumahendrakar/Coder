import tkinter
from tkinter import ttk,Tk as tk
from tkinter import *

icon = r"C:\Users\mahen\Downloads\Papirus-Team-Papirus-Mimetypes-App-x-designer.ico"
window = tk()
window.iconbitmap(icon)
window.title("Calculater")
window.geometry('340x450')


frame1 = Frame(window,width=320,height=120,bg='black')
frame1.grid(row=0,column=0,padx=0)

numberinputer = Text(frame1,width=13,height=2,border=0, foreground='white',bg='black',font=('myfont.ttf',35))
numberinputer.pack(side=BOTTOM)
numberinputer.insert(1.0,'                                                                                              ')

frame2 = Frame(window,width=350,height=420,bg='green')
frame2.grid(row=1,column=0,columnspan=25)

frame3 = Frame(window, width=350,height=4200,bg='blue')
frame3.grid(row=2,column=0,columnspan=25)

def button(frame,text,side,anchor=None):
    button1 = Button(frame,text=text,font='myfont.ttf 19 bold',width=7,bg='green',fg='white')
    button1.pack(side=side,anchor=anchor)


button(frame2,'1',LEFT)
button(frame2,'2',LEFT)
button(frame2,'3',LEFT)
button(frame3,'4',LEFT)
button(frame3,'5',LEFT)
button(frame3,'6',LEFT)
window.mainloop()

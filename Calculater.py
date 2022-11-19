import tkinter
from tkinter import ttk,Tk as tk
from tkinter import *

icon = r"C:\Users\mahen\Downloads\Papirus-Team-Papirus-Mimetypes-App-x-designer.ico"
window = tk()
window.iconbitmap(icon)
window.title("Calculater")

window.geometry('333x385')



def Entered():
    print()


frame1 = Frame(window,width=275,height=120,bg='black',highlightcolor='black',highlightthickness=1,pady=3)
frame1.grid(row=0,column=0,padx=0)

Entryy = Entry(frame1,width=54,background='black',fg='white')
Entryy.pack(side=BOTTOM,fill=BOTH)

frame2 = Frame(window,width=300,height=420,bg='green',highlightcolor='black',highlightthickness=2,background='white')
frame2.grid(row=1,column=0,sticky=tkinter.W)

def button(frame,text,*,row,column,width=None,sticky=None,padx=None):
    
    button1 = Button(frame,text=text,font='myfont2.ttf 16 ',height=1,width=width,bg='black',fg='white',command=lambda : numberinputer.insert(END,'guru'))
    button1.grid(row=row,column=column,sticky=sticky)
    
col = 1
for row in range(3):
    for column in range(3):
        button(frame2,col,row=row,column=column,sticky=tkinter.W,width=6)
        col+=1

else:
    for index,columns in enumerate(['*','**',"%","/",'+',"-"]):
        button(frame2,columns,row=index,column=4,width = 6,sticky=tkinter.W)

col = 0
for row in range(3,6):
    for column in range(3):
        button(frame2,['(',')','0','Clear','back','color','-','X','=',][col],row=row,column=column,sticky=tkinter.W,width=6)
        col+=1

window.mainloop()

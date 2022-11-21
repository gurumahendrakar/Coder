import tkinter
from tkinter import ttk,Tk as tk
from tkinter import *

icon = r"C:\Users\mahen\Downloads\Papirus-Team-Papirus-Mimetypes-App-x-designer.ico"
window = tk()
window.iconbitmap(icon)
window.title("Calculater")
window.geometry('309x400')

# window.resizable(width=False,height=False)


frameOone = Frame(window,bg='black',highlightcolor='gray',highlightthickness=3)
frameOone.grid(row=0,column=0,sticky='nw')

entrycalc = Entry(frameOone,width=25,bg='black',fg='white',borderwidth=0,font='15')
entrycalc.grid(row=0, column=0,pady=(90,0),sticky='nw')



frameOtwo = Frame(window,width=100,height=200)
frameOtwo.grid( row=1,column=0,sticky='nw')

button = Button(frameOtwo,text='C',width=11,height=3,justify='center',font='myfont.ttf 8')
button2 = Button(frameOtwo,text=2,width=11,height= 3,justify='center',font='myfont.ttf 8',foreground='red')
button3 = Button(frameOtwo,text=3,width=11,justify='center',font='myfont.ttf 8',height=3,)
button4 = Button(frameOtwo,text=4,width=11,justify='center',font='myfont.ttf 8',height=3,)
button5 = Button(frameOtwo,text=5,width=11,height=3,justify='center',font='myfont.ttf 8')
button6 = Button(frameOtwo,text=6,width=11,height=  3,justify='center',font='myfont.ttf3 8',foreground='red')
button7 = Button(frameOtwo,text=7,width=11,justify='center',font='myfont.ttf 8',height=3,)
button8 = Button(frameOtwo,text=8,width=11,justify='center',font='myfont.ttf 8',height=3,)

button.config(command= lambda  : entrycalc.insert(END, button.cget('text')),bg='green',fg='black')
button2.config(command= lambda  : entrycalc.insert(END,button2.cget('text')),bg='green',fg='black')
button3.config(command= lambda  : entrycalc.insert(END,button3.cget('text')),bg='green',fg='black')
button4.config(command= lambda  : entrycalc.insert(END,button4.cget('text')),bg='green',fg='black')
button5.config(command= lambda  : entrycalc.insert(END, button.cget('text')),bg='green',fg='black')
button6.config(command= lambda  : entrycalc.insert(END,button2.cget('text')),bg='green',fg='black')
button7.config(command= lambda  : entrycalc.insert(END,button3.cget('text')),bg='green',fg='black')
button8.config(command= lambda  : entrycalc.insert(END,button4.cget('text')),bg='green',fg='black')
b = button.grid(row=0,column=0)
b2 = button2.grid(row=0,column=1)
b3 = button3.grid(row=0,column=2)
b4 = button4.grid(row=0, column=3)
b5 = button5.grid(row=1,column=0)
b6 = button6.grid(row=1,column=1)
b7 = button7.grid(row=1,column=2)
b8 = button8.grid(row=1, column=3)

window.mainloop()

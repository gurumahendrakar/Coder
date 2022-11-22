import tkinter
from tkinter import ttk,Tk as tk
from tkinter import *

icon = r"C:\Users\mahen\Downloads\Papirus-Team-Papirus-Mimetypes-App-x-designer.ico"
window = tk()
window.iconbitmap(icon)
window.title("Calculater")
window.geometry('305x387')

# window.resizable(width=False,height=False)


frameOone = Frame(window,bg='black',highlightcolor='gray',highlightthickness=3)
frameOone.grid(row=0,column=0,sticky='nw')

entrycalc = Entry(frameOone,width=27,bg='black',fg='white',borderwidth=0,font='15',state='normal')
entrycalc.grid(row=0, column=0,pady=(90,0),sticky='nw')



frameOtwo = Frame(window,width=100,height=200)
frameOtwo.grid( row=1,column=0,sticky='nw')

buttonmod = Button(frameOtwo,text='%',width=11,height=3,justify='center',font='myfont.ttf 8')
buttonc = Button(frameOtwo,text='C',width=11,height= 3,justify='center',font='myfont.ttf 8',foreground='red')
buttonce = Button(frameOtwo,text='CE',width=11,justify='center',font='myfont.ttf 8',height=3,)
buttonx = Button(frameOtwo,text='X',width=11,justify='center',font='myfont.ttf 8',height=3,)
button1 = Button(frameOtwo,text=1,width=11,height=3,justify='center',font='myfont.ttf 8')
button2 = Button(frameOtwo,text=2,width=11,height=  3,justify='center',font='myfont.ttf3 8',foreground='red')
button3 = Button(frameOtwo,text=3,width=11,justify='center',font='myfont.ttf 8',height=3,)
button4 = Button(frameOtwo,text='/',width=11,justify='center',font='myfont.ttf 8',height=3,)
button5 = Button(frameOtwo,text=4,width=11,justify='center',font='myfont.ttf 8',height=3,)
button6 = Button(frameOtwo,text=5,width=11,justify='center',font='myfont.ttf 8',height=3,)
button7 = Button(frameOtwo,text=6,width=11,justify='center',font='myfont.ttf 8',height=3,)
button8 = Button(frameOtwo,text='*',width=11,justify='center',font='myfont.ttf 8',height=3,)
button9  = Button(frameOtwo,text=7,width=11,justify='center',font='myfont.ttf 8',height=3,)
button10 = Button(frameOtwo,text=8,width=11,justify='center',font='myfont.ttf 8',height=3,)
button11 = Button(frameOtwo,text=9,width=11,justify='center',font='myfont.ttf 8',height=3,)
button12 = Button(frameOtwo,text='-',width=11,justify='center',font='myfont.ttf 8',height=3,)
button13  = Button(frameOtwo,text='**',width=11,justify='center',font='myfont.ttf 8',height=3,)
button14 = Button(frameOtwo,text='//',width=11,justify='center',font='myfont.ttf 8',height=3,)
button15 = Button(frameOtwo,text='.',justify='center',font='myfont.ttf 8',height=3,width=11)
button16 = Button(frameOtwo,text='=',width=11,justify='center',font='myfont.ttf 8',height=3,)

def calculate():

    if entrycalc:
        a,sign,b = entrycalc.get().partition('*' or '/' or '%' or '+' or '-' or '**' or '//')

        if sign == '*':
            entrycalc.delete(0,END)
            entrycalc.insert(0,int(a)*int(b))
            # entrycalc.insert(0)











def X():
    entrycalc.delete(len(entrycalc.get())-1,END)

def C():
    entrycalc.delete(0,END)



buttonmod.config( command= lambda  : entrycalc.insert(END, buttonmod.cget('text')),bg='green',fg='white')
buttonc.config(command=C,bg='green',fg='white')
buttonce.config(command= lambda  : entrycalc.insert(END,buttonce.cget('text')),bg='green',fg='white')
buttonx.config(command= X,bg='green',fg='white')
button1.config(command= lambda  : entrycalc.insert(END, button1.cget('text')),bg='green',fg='white')
button2.config(command= lambda  : entrycalc.insert(END,button2.cget('text')),bg='green',fg='white')
button3.config(command= lambda  : entrycalc.insert(END,button3.cget('text')),bg='green',fg='white')
button4.config(command= lambda  : entrycalc.insert(END,button4.cget('text')),bg='green',fg='white')
button5.config(command= lambda  : entrycalc.insert(END,button5.cget('text')),bg='green',fg='white')
button6.config(command= lambda  : entrycalc.insert(END,button6.cget('text')),bg='green',fg='white')
button7.config(command= lambda  : entrycalc.insert(END,button7.cget('text')),bg='green',fg='white')
button8.config(command= lambda  : entrycalc.insert(END,button8.cget('text')),bg='green',fg='white')
button9.config(command= lambda  : entrycalc.insert(END,button9.cget('text')),bg='green',fg='white')
button10.config(command= lambda  : entrycalc.insert(END,button10.cget('text')),bg='green',fg='white')
button11.config(command= lambda  : entrycalc.insert(END,button11.cget('text')),bg='green',fg='white')
button12.config(command= lambda  : entrycalc.insert(END,button12.cget('text')),bg='green',fg='white')
button13.config(command= lambda  : entrycalc.insert(END,button13.cget('text')),bg='green',fg='white')
button14.config(command= lambda  : entrycalc.insert(END,button14.cget('text')),bg='green',fg='white')
button15.config(command= lambda  : entrycalc.insert(END,button15.cget('text')),bg='green',fg='white')
button16.config(command=calculate,bg='green',fg='white')


buttonmod.grid(row=0,column=0)
b2 = buttonc.grid(row=0,column=1)
b3 = buttonce.grid(row=0,column=2)
b4 = buttonx.grid(row=0, column=3)
b5 = button1.grid(row=1,column=0)
b6 = button2.grid(row=1,column=1)
b7 = button3.grid(row=1,column=2)
b8 = button4.grid(row=1, column=3 )
b9 = button5.grid(row=2,column=0)
b10 = button6.grid(row=2,column=1)
b11 = button7.grid(row=2,column=2)
b12 = button8.grid(row=2, column=3)
b13 = button9.grid(row=3,column=0)
b14 = button10.grid(row=3,column=1)
b15 = button11.grid(row=3,column=2)
b16 = button12.grid(row=3, column=3)
b17 = button13.grid(row=4, column=0)
b18 = button14.grid(row=4,column=1)
b19 = button15.grid(row=4,column=2)
b20 = button16.grid(row=4, column=3)
window.mainloop()

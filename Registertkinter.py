import tkinter
from tkinter import ttk,colorchooser
import tkinter.font

framecolor = 'black'
window = tkinter.Tk()
window.config(bg='white')
window.geometry('500x500')
# window.resizable(False,False)
RegisterFrame = tkinter.Frame(window,highlightbackground='gray',highlightthickness=3, bg='white')
RegisterFrame.grid(row=0,column=0,sticky=tkinter.W)
fontt = tkinter.font.Font(family='myfont.ttf',size=11,weight='bold')

def MyLabel(text,row,column,color=framecolor,bg=None,padx= 0,pady=0,rowspan=None,columnspan=None,show=None):

    labell = tkinter.Label(RegisterFrame,text=text,font=fontt,fg=color,bg='white',padx=padx,pady=pady,background=bg)
    labell.grid(row=row,column=column,rowspan=rowspan,columnspan=columnspan)

def MyEnterybox(frame,row,column,width=14,show=None,pady=None,padx=None):
    Entryboxx = tkinter.Entry(frame,width=width,show=show)
    Entryboxx.grid(row=row,column=column,pady=pady,padx=padx)




MyLabel("REGISTER STUDENT",0,0,'green',padx=80,pady=14,columnspan=2)
MyLabel('Name    : ',1,0,'black',padx=30,pady=10)
MyLabel('Sirname :',2,0,'black',pady=10)
MyLabel('Email   :',3,0,'black',pady=10)
MyLabel('Phone   :',4,0,'black',pady=10)
MyLabel('Teacher ID :',5,0,'black',pady=10)
MyEnterybox(RegisterFrame,1,1,width=25,padx=10)
MyEnterybox(RegisterFrame,2,1,width=25)
MyEnterybox(RegisterFrame,3,1,width=25)
MyEnterybox(RegisterFrame,4,1,width=25,pady=14)
MyEnterybox(RegisterFrame,5,1,width=25,show='*',pady=14)

def ColoChangerFrame():
    colo = colorchooser.askcolor()
    RegisterFrame.config(background=colo[1])
    if colo[1]!='#ffffff':
        MyLabel("REGISTER STUDENT", 0, 0, 'white',bg=colo[1], padx=30, pady=14, columnspan=2)
        MyLabel('Name    : ', 1, 0,'white',bg=f'{colo[1]}', padx=30, pady=10)
        MyLabel('Sirname    : ', 2, 0, 'white', bg=f'{colo[1]}', padx=30, pady=10)
        MyLabel('Email    : ', 3, 0, 'white', bg=f'{colo[1]}', padx=30, pady=10)
        MyLabel('Phone    : ', 4, 0, 'white', bg=f'{colo[1]}', padx=30, pady=10)
        MyLabel('Teacher ID 5 :', 5, 0, 'white', bg=f'{colo[1]}',show='-', padx=80, pady=15)

MenuColor = tkinter.Menu(RegisterFrame)
MenuColor.add_command(label="Color",command=ColoChangerFrame)
window.config(menu = MenuColor)

frame3 = tkinter.Frame(bg='white',width=5,height=5,pady=25)
frame3.grid(row=1,column=0)


frame2 = tkinter.Frame(window,highlightbackground='gray',highlightthickness=3,bg='white')
frame2.grid(row=2,column=0)


Text2 = tkinter.Text(RegisterFrame,width=25,height=10,background='green',font='myfont2.ttf')
Text2.grid(row=0,column=2,sticky=tkinter.E)

a = tkinter.font.Font(frame2,family='myfont2.ttf',size='19',underline=1)
textinputer = tkinter.Text(frame2,width=120,height=25,bg='black',fg='white',font=a)
textinputer.pack(side=tkinter.LEFT,fill=tkinter.BOTH)


frame3 = tkinter.Frame(window,bg='green',width=100,height=100)
frame3.grid(row=3,column=0,sticky=tkinter.W)


frame4 = tkinter.Frame(window,bg='pink',width=100,height=200)
frame4.grid(row=4,column=0,sticky=tkinter.NSEW)


a = tkinter.Text(frame4,width=110,height=6)
a.pack(side=tkinter.LEFT)

a = tkinter.Label(frame4,text="Cool Brother",fg='blue',bg='yellow')
a.pack(side=tkinter.RIGHT,fill=tkinter.BOTH)




scroolbar = tkinter.Scrollbar(frame2,orient=tkinter.VERTICAL)
scroolbar.pack(side=tkinter.RIGHT,fill=tkinter.BOTH)


window.mainloop()

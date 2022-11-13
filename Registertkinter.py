import tkinter
from tkinter import ttk,colorchooser
import tkinter.font

framecolor = 'black'
window = tkinter.Tk()
window.config(bg='white')
window.geometry('500x500')
RegisterFrame = tkinter.Frame(window,highlightbackground='gray',highlightthickness=3,bg='white',pady=25)
RegisterFrame.grid(row=0,column=0)
fontt = tkinter.font.Font(family='myfont.ttf',size=11,weight='bold')

def MyLabel(text,row,column,color=framecolor,bg=None,padx= 0,pady=0,rowspan=None,columnspan=None,show=None):

    labell = tkinter.Label(RegisterFrame,text=text,font=fontt,fg=color,bg='white',padx=padx,pady=pady,background=bg)
    labell.grid(row=row,column=column,rowspan=rowspan,columnspan=columnspan)

def MyEnterybox(frame,row,column,width=14,show=None,pady=None,padx=None):
    Entryboxx = tkinter.Entry(frame,width=width,show=show)
    Entryboxx.grid(row=row,column=column,pady=pady,padx=padx)




MyLabel("REGISTER STUDENT",0,0,'green',padx=30,pady=14,columnspan=2)
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
        MyLabel('Teacher ID 5 :', 5, 0, 'white', bg=f'{colo[1]}',show='-', padx=30, pady=15)

MenuColor = tkinter.Menu(RegisterFrame)
MenuColor.add_command(label="Color",command=ColoChangerFrame)
window.config(menu = MenuColor)

frae = tkinter.Frame(window,bg="yellow",highlightbackground='white',highlightthickness=5,width=100)
frae.grid(row=1,column=0,columnspan=35,rowspan=15)

aa = tkinter.Scrollbar(frae,orient=tkinter.VERTICAL)

a = tkinter.Text(frae,bg='gray',xscrollcommand=aa.set,width=20)
for i in range(100):
    a.insert(tkinter.END,'ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo')
aa.config(command=a.xview)
a.grid(row=0,column=0)

aa.place(x=0,y=60)

window.mainloop()
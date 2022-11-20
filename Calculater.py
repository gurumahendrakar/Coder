import tkinter
from tkinter import ttk,Tk as tk
from tkinter import *

icon = r"C:\Users\mahen\Downloads\Papirus-Team-Papirus-Mimetypes-App-x-designer.ico"
window = tk()
window.iconbitmap(icon)
window.title("Calculater")
window.geometry('302x400')
# window.resizable(width=False,height=False)


frameOone = Frame(window,bg='black',highlightcolor='gray',highlightthickness=3)
frameOone.grid(row=0,column=0)

entrycalc = Entry(frameOone,width=49,bg='black',fg='white',borderwidth=0,font='15')
entrycalc.grid(row=0, column=0,pady=(90,0))
window.mainloop()

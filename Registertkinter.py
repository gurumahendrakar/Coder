import tkinter
from tkinter import ttk,colorchooser
import tkinter.font

framecolor = 'black'
window = tkinter.Tk()
window.config(bg='white')
window.geometry('500x500')



frame1 = tkinter.Frame(window,bg="yellow",highlightbackground='white',highlightthickness=5)
frame1.pack(fill='y')

a = tkinter.Label(frame1,text='Guru Mahendrkar')
a.pack(side=tkinter.TOP,fill='y')

window.mainloop()
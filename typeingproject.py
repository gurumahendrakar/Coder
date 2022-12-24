import tkinter
from tkinter import ttk
import PyPDF2
import re
from tkinter import  Canvas,Label,Menu,Button,Checkbutton,Tk,Frame,Text,colorchooser,Entry,messagebox,Toplevel
import threading
import ttkthemes
import time


class TEXT_FRAME():

    def __init__(self,Typing):
        self.Typing = Typing
        self.window = tkinter.Tk()
        self.window.title('TYPING-MASTER')
        self.window.config(bg='black')
        self.window.geometry('800x400')
        self.menu = Menu(self.window)
        self.menu.add_command(label='Settings',command=self.text_bg_changer)
        self.window.config(menu=self.menu)
        self.Text_ = None
        self.stvar = tkinter.IntVar()
        self.cbutton = Checkbutton(self.window,variable=self.stvar,text='HOW MANY WORDS PER MINUTE =',bg='black',fg='white')
        self.cbutton.pack(side='top',anchor='nw')

    def Text_show(self):



        text_frame = Frame(self.window,
                           highlightthickness=3,
                           highlightbackground='black',
                           highlightcolor='black')

        text_ = Entry(text_frame,
                      bg='black',
                      fg='white',
                      font='myfont.ttf 25')

        self.Text_ = text_
        print(self.Text_)


        text_2 = Entry(text_frame,
                      bg='black',
                      fg='white',
                      font='myfont.ttf 25')

        text_2.pack(fill='x',side='bottom')

        text_er = PyPDF2.PdfFileReader('levt101.pdf')

        for x in range(text_er.numPages):
            text_x = text_er.getPage(x).extractText()

        a = re.findall('([A-Z][a-z]{0,}|[a-z]{0,})', text_x)


        self.book_text = a

        text_.pack(expand=True,fill='both')
        text_frame.pack(expand=True,fill='both')

        self.text_readerObject = text_2
        self.text_showerObject = text_

        Spell_handle_thread = threading.Thread(target=frame_.spell_checker)
        Spell_handle_thread.daemon = True
        Spell_handle_thread.start()


    def spell_checker(self):


        top_levelwindow = Toplevel()
        top_levelwindow.configure(bg='black')
        top_levelwindow.geometry('%dx%d' % (200, 200))


        x = Label(top_levelwindow, text='HOW MANY WORDS PER MINUTE', bg='black', fg='white')
        x.pack(pady=20)

        o = Entry(top_levelwindow,)

        o.pack()

        def toplevel_destroy():
            self.Text_.insert(tkinter.END, [x for x in self.book_text if x][:int(o.get())])

            top_levelwindow.destroy()

        sumbit_ = ttk.Button(top_levelwindow,width=10,text='Submit',command=toplevel_destroy)
        sumbit_.pack(pady=8)

        xx  = 0
        list__ = [x for x in self.book_text if x]




        while xx <len(list__[:int(13)]):
            print(list__[xx])
            if self.text_readerObject.get()==list__[xx]:
                self.text_showerObject.delete(0,len(list__[xx])+1)
                self.text_readerObject.delete(0,'end')
                print(list__[xx])
                xx+=1





    def text_bg_changer(self):
        color_ = colorchooser.askcolor()
        print(color_)
        if color_[1]=='#ffffff':
            self.Text_['bg'] = 'black'

        else:
            self.Text_['bg'] = color_[-1]
            self.Text_['fg'] = 'white'

    def __mainloop__(self):
        self.Text_show()
        self.Typing.__init__(self, self.window)
        self.window.mainloop()




class TypingButtons(TEXT_FRAME):

    def __init__(self,window):
        self.frame2 = Frame(window,bg='black')
        self.frame3 = Frame(window,bg='black')
        self.frame4 = Frame(window,bg='black')
        self.frame2.pack(side='top',anchor='nw',fill='x')
        self.frame3.pack(side='top',anchor='nw',fill='x',padx=35)
        self.frame4.pack(side='top',anchor='nw',fill='x',padx=(50,30))

        for x in range(len('QWERTYUIOP')):
            self.button_slot_a = Label(self.frame2,text='QWERTYUIOP'[x],bg='black',fg='white',width=4,height=3)
            self.button_slot_a.pack(side='left',expand=True)

        for x in range(len('ASDFGHJKL;')):
            self.button_slot_a = Label(self.frame3, text='ASDFGHJKL;'[x], bg='black', fg='white', width=4, height=3)
            self.button_slot_a.pack(side='left', expand=True)

        for x in range(len('ZXCVBNM,./')):
            self.button_slot_a = Label(self.frame4, text='ZXCVBNM,./'[x], bg='black', fg='white', width=4, height=3)
            self.button_slot_a.pack(side='left', expand=True)

if __name__== '__main__':
    frame_ = TEXT_FRAME(TypingButtons)

    frame_.__mainloop__()




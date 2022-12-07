from tkinter import ttk,Tk,Frame,Button,LabelFrame,filedialog
import tkinter 
from PIL import Image,ImageTk
import os



pause_of_check = "On"

# 1	Button
# 2	Canvas
# 3	Checkbutton
# 4	Entry
# 5	Frame
# 6	Label
# 7	Listbox
# 8	Menubutton
# 9	Menu
# 10 Message
# 11 Radiobutton
# 12 Scale
# 13 Scrollbar
# 14 Text
# 15 Toplevel
# 16 Spinbox
# 17 PanedWindow
# 18 LabelFrame
# 19 tkMessageBox


window = Tk()
window.geometry('480x390')
window.iconbitmap(r"C:\Users\mahen\Downloads\musicincon.ico")
window.iconname('Musicplayer')
window.wm_title('Music_player')
window.config(background='black')


image_frame = Frame(window,bg='black')
image_frame.pack(side='top',anchor='nw',fill='both')


image01 = Image.open(r"C:\Users\mahen\bitepy\OIP (1).jpeg")
image01 = image01.resize((250,300))
image01 = ImageTk.PhotoImage(image01)

label_image = tkinter.Label(image_frame,
                            image=image01,
                            highlightbackground='gray',
                            highlightcolor='black',
                            highlightthickness=3,
                            compound='left',
                            text = "𝓜𝓾𝓼𝓲𝓬𝓟𝓵𝓪𝔂𝓮𝓻",
                            font=(r"C:\Users\mahen\bitepy\allfiles\myfont4.ttf 16 bold"),
                            bg='black',fg='white',
                            wraplength=4)


label_image.pack(side= 'left',anchor='nw',fill='both')



listboxx = tkinter.Listbox(image_frame,
                            highlightbackground='black',
                            highlightcolor='gray',
                            highlightthickness=3,
                            height=19)

listboxx.pack(side='top',anchor='nw',fill='x')

def folder_open():
    
    folder_musi = filedialog.askdirectory(initialdir='C:/Users')
    for music in os.listdir(folder_musi):
        if music.endswith('.mp3'):
            listboxx.insert('end',music)

    


menu_ = tkinter.Menu(window,tearoff=False)
menu_.add_command(label='𝓕𝓸𝓵𝓭𝓮𝓻𝓒𝓱𝓸𝓸𝓞𝓼𝓮𝓻',
                activebackground='gray',
                activeforeground='white',
                background='white',
                command=folder_open,
                )




menu_2 = tkinter.Menu(menu_)
menu_2.add_cascade(label='𝓢𝓮𝓽𝓽𝓲𝓷𝓰𝓼',menu=menu_)

window.config(menu=menu_2)


os.chdir('allfiles')
for music in os.listdir(os.getcwd()):
        if music.endswith('.mp3'):
            listboxx.insert('end',)


# pause__ = tkinter.StringVar()
# pause__.set('sooo.png')


def pause_():
    global button_pause
    if pause_of_check!="On":
        image03  = Image.open(r"OIP (2).jpeg")
        image03 = image03.resize((40,40))
        image03 = ImageTk.PhotoImage(image03)
        
        button_pause.config(image=image03)

    else:
        button_pause.config(image=image03)
    
frame2 = Frame(window,bg='black')
frame2.pack(side='left')

image02  = Image.open('sooo.png')
image02 = image02.resize((40,40))
image02 = ImageTk.PhotoImage(image02)

image03  = Image.open(r"OIP (2).jpeg")
image03 = image03.resize((40,40))
image03 = ImageTk.PhotoImage(image03)



button_left = tkinter.Button(frame2,
                            image=image02,
                            bg='black',
                            cursor='hand2')
button_left.pack(side='left',anchor='nw',padx=3)

button_pause = tkinter.Button(frame2,
                            image=image02,
                            bg='black',command=pause_,
                            cursor='hand2',
                        )

button_pause.pack(side='left',anchor='nw',padx=3)

button_right = tkinter.Button(frame2,
                            image=image02,
                            bg='black',
                            cursor='hand2')


button_right.pack(side='left',anchor='nw',padx=3)



if __name__ == '__main__':
    window.mainloop()
    pass
   
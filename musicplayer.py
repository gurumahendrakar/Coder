from tkinter import ttk,Tk,Frame,Button,LabelFrame,filedialog
import tkinter 
from PIL import Image,ImageTk
import os
import playsound



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
window.geometry('740x550')
window.iconbitmap(r"C:\Users\mahen\Downloads\musicincon.ico")
window.iconname('Musicplayer')
window.wm_title('Music_player')
window.config(background='black')


image_frame = Frame(window,bg='black')
image_frame.pack(side='top',anchor='nw',fill='both')


image01 = Image.open(r"C:\Users\mahen\bitepy\allfiles\maxresdefault (1).jpg")
image01 = image01.resize((350,200))
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


sc = tkinter.Scrollbar(image_frame,orient='vertical',activebackground='green')

listboxx = tkinter.Listbox(image_frame,
                            highlightbackground='black',
                            highlightcolor='gray',
                            width=30,
                            highlightthickness=3,
                            height=19,
                            bg='black',
                            fg='white',
                            font='myfont4.ttf 14 italic underline')

listboxx.pack(side='left',anchor='nw')

sc.config(command=listboxx.yview)
listboxx.config(yscrollcommand=sc)
sc.pack(side='left',fill='y')

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


index = 0 
os.chdir('allfiles')
for music in os.listdir(os.getcwd()):
        if music.endswith('.mp3'):
            listboxx.insert('end',str(index)+'.  ' + music)
            index+=1

index = 0 

for music in os.listdir(os.getcwd()):
        if music.endswith('.mp3'):
            listboxx.insert('end',str(index)+'.  ' + music)
            index+=1

index = 0 

for music in os.listdir(os.getcwd()):
        if music.endswith('.mp3'):
            listboxx.insert('end',str(index)+'.  ' + music)
            index+=1

def pause_():
    global pause_of_check

    if pause_of_check!='On':
        button_pause.config(image=image02)
        pause_of_check = 'On'
        import audioplayer

        
        


    else:
        import audioplayer
        button_pause.config(image=image03)
        pause_of_check = 'off'
        import playsound

        playsound.playsound(r"C:\Users\mahen\bitepy\allfiles\Ghani-Syaani.mp3")    
frame2 = Frame(window,bg='black')
frame2.pack(side='left')

#--- PAUSE PLAY

image02  = Image.open(r"C:\Users\mahen\bitepy\allfiles\c054208e7a875849fb9849216103eb25-details.jpg")
image02 = image02.resize((40,40))
image02 = ImageTk.PhotoImage(image02)

image03  = Image.open(r"C:\Users\mahen\bitepy\allfiles\OIP (6).jpeg")
image03 = image03.resize((40,40))
image03 = ImageTk.PhotoImage(image03)




image04  = Image.open(r"C:\Users\mahen\bitepy\allfiles\pngtree-vector-back-icon-png-image_889628.jpg")
image04 = image04.resize((40,40))
image04 = ImageTk.PhotoImage(image04)

image05  = Image.open(r"C:\Users\mahen\bitepy\allfiles\pngtree-next-icon-isolated-on-background-png-image_1793111.jpg")
image05 = image05.resize((40,40))
image05 = ImageTk.PhotoImage(image05)

button_left = tkinter.Button(frame2,
                            image=image04,
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
                            image=image05,
                            bg='black',
                            cursor='hand2')


button_right.pack(side='left',anchor='nw',padx=3)



if __name__ == '__main__':
    window.mainloop()
    pass
   
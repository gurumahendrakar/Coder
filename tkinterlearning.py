from tkinter import *
from PIL import *
from PIL import Image,ImageTk


#---------------------------------------------------------Window Create-------------------------------------------------------------------------------
window = Tk() #Creating window
window.title("Practice")
window.iconbitmap(r"C:\Users\mahen\Downloads\icons8-wi-fi-fair-48 (1).ico")
window.geometry("400x400")


#------------------------------------------------------------Labels-------------------------------------------------------------------------------------------
#
#
#
#
#
#
# StringVar = StringVar()
# IntVar = IntVar()
# IntVar.set(8)
#
# StringVar.set("Hey What'app Buddy?")
#
# dog_image = Image.open("dogresize_image.png")
# dog_image = ImageTk.PhotoImage(dog_image)

# label = Label(window,
#               text="Hey Whats'app \n Guru Mahendrakar\nAge 18\nCollage : CB Collage Bhalki",
#               font='myfont4.ttf 15 bold italic overstrike underline',
#               image=dog_image,
#               underline=1,
#               wraplength=3,#........horizental letters ko vertical me likhta hai
#               disabledforeground='white',
#               cursor=('circle','spider','heart'),
#               compound='bottom',
#               state='normal',
#               justify='left',
#               padx=(20),
#               pady=(20),
#               background='black',
#               foreground='white',
#               borderwidth=15,
#               relief='ridge',
#               textvariable= StringVar,
#
#               )
# label.pack(side='left',fill='both',expand='True')
#
#








#--------------------------------------------------button------------------------------------------------------------------------------------------





# image = Image.open('dogresize_image.png')
# image = ImageTk.PhotoImage(image)
#
#
# def executed():
#     print("Clicked Me!")
#
#
# button = Button(window,
#                 text='Click Me',
#                 image=image,width=200,
#                 height=50,
#                 compound='left',
#                 bg='green',fg='black',
#                 activeforeground='red',
#                 activebackground='blue',
#                 border=5,
#                 borderwidth=5,
#                 relief='sunken',
#                 overrelief='raised',
#                 command=executed,
#                 # wraplength=5-> #........horizental letters ko vertical me likhta hai
#                 cursor='circle',
#                 state='normal',
#                 highlightcolor='black',
#                 highlightthickness=11,
#                 anchor='nw',
#                 )
# button.flash() # Thodi Der Tak Button Ko Invisble Rakhata Hai (miliseconds me wapas jaata hai)
# button.pack()









#---------------------------------------------------Frames------------------------------------------------------------------------------

#........................................................ Grid Help...........................................................................
#IMPORTANT READ FIRST : -> Frames Ke Saath Grid() Use Karke Aur Ek Frame Pe Pack Use Karsakte ho




#........................................................Frames Help.........................................................................................
#FRAME BANAKE KE BAAD :-> Frame Ke Grid() Ke Madat Se Kuch Bhi Spon Kiya To Sirf Grid() Hi Use karna Padega
# & Frame Me Pack() Ki Madat Se Kuch Bhi Spon Kiya To Sirf Pack Use Karna Padega
# place () Bhi O Dono Ki Taraha Hi Kaam Karta Hai



# ...............................................4 Frames Created Down..............................................................




# frameOne = Frame(window,bg='yellow',name='frameOone')
# frameOne.pack(side=LEFT,fill='both')
# label = Label(frameOne,text="Click Me!",bg='red',fg='green')
# label.pack(side=RIGHT)
#





# frameOne = Frame(window,bg='green',padx=25)
# frameOne.pack(side=LEFT,fill='both')
# label = Label(frameOne,text="Click Me!",bg='red',fg='green')
# label.grid(row=0,column=0)
#




# frameOne = Frame(window,bg='red',padx=25)
# frameOne.pack(side=LEFT,fill='both')
# label = Label(frameOne,text="Click Me!",bg='red',fg='green')
# label.grid(row=0,column=0)
#




# frameOne = Frame(window,bg='yellow',padx=25)
# frameOne.pack(side=LEFT,fill='both')
# label = Label(frameOne,text="Click Me!",bg='red',fg='green')
# label.grid(row=1,column=0)








#------------------------------------------------------CheckButton--------------------------------------------------------------------------------




#
#
# FrameOone = Frame(window,highlightthickness=3,highlightcolor='gray')
# FrameOone.grid(row=0,column=0)
#
#
# Dosa = StringVar()
# Chicken = IntVar()
# Idli = IntVar()
#
# Dosa.set(False)
#
#
# dog_image = Image.open("dogresize_image.png")
# dog_image = ImageTk.PhotoImage(dog_image)
#
#
# def OrderChecking():
#     print(Dosa.get())
#
#     print(f"Agent Ne {checkbox1.cget('text')} Order Kardiya Hai")
#
#
# checkbox1 = Checkbutton(FrameOone,text='Dosa',
#                         variable=Dosa,
#                         command=OrderChecking,
#                         onvalue='Dosa',
#                         offvalue='none',
#                         offrelief='solid',
#                         borderwidth=2,
#                         overrelief='solid',
#                         height=10,
#                         width=200,
#                         foreground='green',
#                         bg='gray',
#                         highlightthickness=3,
#                         highlightcolor='red',
#                         justify='right',
#                         image= dog_image,
#                         compound='right',
#                         state='normal',
#                         )
#
#
#
#
# checkbox1.grid(row=0,column=0)
#
#



#-------------------------------------------------------------Entrybox--------------------------------------------------------------------------------


# frameOone = Frame(window,width=0,height=1000,bg='blue')
# frameOone.pack(side='left',anchor='e',fill='y')
#
#
#
# scro = Scrollbar(frameOone,
#                  orient=HORIZONTAL,
#                  bg='blue',
#                  )
# scro.pack(side='bottom',fill='x')
#
# entry = Entry(frameOone,
#               width=100,
#               bg='black',
#               fg='white',
#               cursor='circle',
#               readonlybackground='black',
#               state='normal',
#               insertwidth=10,
#               insertbackground='white',
#               insertontime=40,
#               insertborderwidth=50,
#               selectborderwidth=5,
#               selectbackground='pink',
#               selectforeground='green',
#               font='myfont4.ttf 19 italic underline overstrike',
#               justify='left',
#               highlightthickness=3,
#               highlightbackground='yellow',
#               highlightcolor='green',
#               xscrollcommand=scro,
#               border=3,
#               borderwidth=6,
#               relief='sunken',
#               show='+'
#               )
#
#
#
# entry.pack(side='left',fill='y')
# scro.config(command=entry.xview)
#
#
#


#----------------------------------------------------Radiobutton--------------------------------------------------------------------------

#
# frameOone = Frame(window,bg='green',width=50,height=50)
# frameOone.pack(side=LEFT,anchor='nw',fill='y')
#
# image_ = Image.open('dogresize_image.png')
# image_ = ImageTk.PhotoImage(image_)
#
# IntVar = StringVar()
# IntVar.set(0)
#
# def command_():
#     print("Command Executed Brother")
#
#
# rdxbutton = Radiobutton(window,
#                         width=100,
#                         text='dosa',
#                         value=1,
#                         variable=IntVar,
#                         bg='red',
#                         fg='blue',
#                         underline=1,
#                         activebackground='green',
#                         activeforeground='yellow',
#                         overrelief='sunken',
#                         image=image_,
#                         compound='left',
#                         justify='right',
#                         command=command_,
#                         highlightcolor='black', # touch karne kaad  black color ayega radiobutton me....
#                         highlightbackground='pink',  #touch karne se pehle pink color ayega radiobutton me..
#                         borderwidth=15)
#
# rdxbutton.pack(side=LEFT, fill='y')
#



#--------------------------------------------------------------Listbox---------------------------------------------------------------------------

def __command(event=None):
    listbox.delete(len(listbox)-1,END)


listbox = Listbox(window,
                  bg='black',
                  fg='white',
                  border=3,
                  borderwidth=5,
                  relief='sunken',
                  cursor='hand2',
                  highlightbackground='yellow',
                  highlightcolor='green',
                  highlightthickness=5,
                  selectforeground='pink'
                  ,selectborderwidth=3,
                  selectbackground='white',
                  selectmode='multiple',
                  listvariable=['yo','gljf'] )

for products in ['aluvera','soda','cream','ponds','fairnlovely','lipstick']:
    listbox.insert(0,products)


listbox.pack()
# listbox.bind('<<ListboxSelect>>',__command)

dlt_button = Button(window,text='Delete',bg='green',command=__command)
dlt_button.pack()

window.mainloop()

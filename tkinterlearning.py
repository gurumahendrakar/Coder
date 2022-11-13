# import os
# import tkinter.messagebox
# from tkinter import Tk as tk
# from tkinter import *
# from tkinter import messagebox as msg
# from tkinter import Menu
# from tkinter import filedialog,ttk

#                 IMPORTANT

#Entrywidth -> 500
#Entryheight -> 500

#but......
#Frame kitni chahiye ye padx pady pe depend karta hai -> Frame badi choti karni hai to padx or pady change karo

# padx = screenwidth//2 hoti hai
#pady = screenheight//2 hoti hai



# # ...............................................listbox...................................................................
# #
# # window = tkinter.Tk()
# # window.geometry('555x555')
# # entry = tkinter.Entry(width=50,border=False)
# # entry.config(border=True,font="myfont.ttf 19 bold")
# # entry.place(x=150,y=(555//2)-35)
# #
# # def delete():
# #     entry.delete(len(entry.get())-1,tkinter.END)
# #
# # def backspace():
# #     entry.delete(0,tkinter.END)
# #
# # entry.insert(0,"Enter : -> ")
# # button = tkinter.Button(window,text="delete",borderwidth=7,fg='black',bg='grey',command=backspace).place(x=(555//2)-5,y=555//2)
# # window.mainloop()
#
# #_____________________________________________Finished Just For Knowledge Lisbox_______________________________________________________
# window = tk()
# window.geometry("500x700") # Display Size
# # window.resizable(False,False) # (Jo Display Hoga Ose Bada Kar Sakte Hai Na Chota)
# window.title("Practice") # window name
# window.configure(background = 'white')
#
# window.attributes('-alpha',1)
# # window.minsize(280,400) # window.minsize(Width,Height) # Is (width,height se chota nahi hoga)
# # window.maxsize(500,500) # window.maxsize(Width,Height) # Is (Width,Height) se Bada Nahi Hoga
#
# window.iconbitmap(r"C:\Users\mahen\Downloads\Dooffy-Characters-And.ico")
# # Ye Float Value Leta hai:-> window.attributes('-alpha,Float_Value(0.8))
# # 0.(8) -> Bracket wala integer (increase karoge to transpence bedegi --- decrese kiya to transpency ghategi)
# # matlab opticity ki tarha editing me jaisa hota hai vaisa
# name = "Name : "
# frame1 = Frame(window,bg='white',padx=50,pady=34)
# frame1.grid()
#
# #..........................................Labels.....................................................................
#
#
# Label(frame1,text = "Name : ",
#     foreground='black',
#     bg='white',
#     font="myfont.ttf 13").grid(row=0,column=2,padx=(0,55),rowspan=5)
#
# Label(frame1,
#     text = "Sirname : ",
#     foreground='black',
#     bg='white'
#     ,font="myfont.ttf 13").grid(row=1,column=2,padx=(0,55))
#
# b =Label(frame1,
#     text = "Roll No : ",
#     foreground='black',
#     bg='white',
#     font="myfont.ttf 13",)
#
# b.config(fg='black',activebackground='gray',activeforeground='green')
# b.grid(row=2,column=2,padx=(0,55))
#
# Button(frame1,text="sumbit")
# User = StringVar()
# Sirname = StringVar()
# Roll = StringVar()
# Checking_mark = IntVar()
# student_ = IntVar()
#
# # ........................................Entry ...................................................................
# name = Entry(frame1,textvariable=User
#     ,show="*",
#     font=('myfont.ttf',10,'bold'),)
#
# sirname = Entry(frame1
#     ,textvariable=Sirname,
#     show="*")
#
# roll = Entry(frame1,
#     textvariable=Roll,
#     show="*")
#
#
#
# name.grid(row=0,column=8,rowspan=6)
# sirname.grid(row=1,column=8)
# roll.grid(row=2,column=8)
#
# button_frame = Frame(window,bg='white')
# button_frame.grid(row=4,column=0)
# def sumbits():
#     print("Name Of User : {} \nSirname Of User : {} \nRollno Of the User : {} ".format(User.get(),Sirname.get(),Roll.get()))
#     print("Age Check",Checking_mark.get())
#     print(student_.get())
#     for index in list_box.curselection():
#         print(Cooking_items[index])
#
# def fuction():
#     print("Checking...........")
#
#     clg_students = {"Guru":{"Name":"Guru","Dad":"Baburao","Sirname":"Mahendrakar","Roll no":39}}
#     if clg_students.get(User.get(),0) and student_.get()==1 and  \
#         Checking_mark.get()==1 and \
#         Roll.get()== "39" and sirname.get()=="Mahendrakar":
#         msg.showinfo("Help",f"Guru Your Percentage Is {89.0}")
#         msg.showinfo("Thanks For Sharing" \
#                          if msg.askquestion("Rate us", "Experience Kaisa Raha Brother") == "yes" else \
#                          "Thanks Your Feedback", "Thanks For Your Feedback")
#     else:
#         msg.showinfo("Invalid Details","Please Check Your Name")
#         msg.showerror("Please Check Forms","Retry Sometime!")
#
#
# def saveus():
#     print("Save Us Brother")
#
#
# # filemenu1 = Menu(window)
# # window.config(menu=filemenu1)
#
# filemenu1 = Menu(window)
# window.config(menu=filemenu1)
#
# basket_menu= Menu(filemenu1,tearoff='off')
# window.config(menu=filemenu1)
# basket_menu2 = Menu(basket_menu)
# basket_menu2.add_command(label="Settings",foreground='black')
# basket_menu2.add_command(label='Help',foreground='black')
#
# basket_menu.add_cascade(label="Cool Drives",menu=basket_menu2)
#
# filemenu1.add_cascade(label = "Filelabel",menu=basket_menu)
#
#
#
#
# # ravan = PhotoImage(file = 'ravan.png')
#
# #.........................................frames & Buttons........................................
#
# fram2 = Frame(window,bg='white').grid()
# buton = Button(frame1,text="Sumbit",command=fuction,background='white',font=('myfont.ttf 14 bold'))
# buton.grid(row=4,column = 2)
# Checkbutton(frame1,text ='Your Age Is 18 Above',
#     variable=Checking_mark,
#     #image = None
#     activebackground='gray',
#     compound='bottom').grid(row=3,column = 20,)
# Radiobutton(frame1,
#     text="Student",
#     variable=student_,
#     value=1,
#     #image=
#     borderwidth=5,
#     relief='sunken').grid(row=5,column=2,pady=(15,0))
#
# Radiobutton(frame1,
#     #image =
#     text="Teacher",
#     variable=student_,
#     value=2).grid(columnspan=1, row=6,column=2,pady=(15,0))
#
#
# #compound='top',image=ravan,indicatoron=0
# #compound='top' image kaha pe dhikhana hai
# #image=ravan # image passing
# # indicatoron=0 image ke side me border hojayage
#
# #..................................Scaleing..................................................
# scaleint = IntVar()
#
# scale = Scale(window,variable= scaleint, from_=0,
#     to=555,
#     fg='black',
#     bg='white' ,
#     # tickinterval = 5,
#     resolution=10,
#     width=10,
#     sliderlength=10,
#     activebackground='white')
#
# scale.config(orient=VERTICAL,sliderlength=8,length=1000)
# print(scale.set(scale['from']-scale['to']//2 +scale['to']))
# scale.place(x= 1880,y=0)
#
# lis = StringVar()
# #............................................Listbox................................................
# list_box = Listbox(frame1,listvariable=lis,selectborderwidth=10, selectbackground='black',selectforeground='pink', selectmode='multiple',foreground='black',bg='white')
# list_box.grid(row=0,column=1)
#
#
#
# for index in range(4):
#     Cooking_items = ["Methi","Bhendi","PythonSabji","Allopartha"]
#     list_box.insert(index,Cooking_items[index])
#
# #.............................Combobox..........................
#
#
# a = ttk.Combobox(window,state = 'readonly',width=18,font='myfont.ttf 13 bold',foreground='black')
# a["values"] = ('𝒮𝓉𝓎𝓁𝒾𝓈𝒽 ,𝒩𝒶𝓂𝑒')
# a.place(x = 300,y=200)
#
# #...........................textwindow..................................
#
# text  = Text(window,font='myfont.ttf 15')
# text.grid(row=3,column=55)
#
# #...............................................fileddialog..................................................................
# # Ye File Directory Open Karta File Choose Kiya Ho Uska Path Return Karta Hai Osse Hum Kuch Bhi Kar sakte Hai
# #...............jaisi ki file reading maine niche kiya hai................
# import os
#
#
# def fileChooser():
#     directory_open = filedialog.askopenfilename(initialdir=r'C:\Users\mahen\bitepy',
#                                                 title='Open',
#                                                 filetypes=(('text files','*.txt'),('allfiles','*.*')))
#     print("Texting Writed Text",text.get(1.0,'end'))  # idhar ye hi likhne pe hi text mila hai change mat karna nahi none milega
#
#     if directory_open:
#         file = open(directory_open,'r')
#         print(file.read().strip('\n'))
#         file.close()
#
#     else:
#         msg.showerror("Choose File","Please Select a File")
#         fileChooser()
#
# s = StringVar()
#
# def background_changer():
#     from tkinter import colorchooser
#
#     # Two Method ColorChooser laneke waste
#     # color = colorchooser.Chooser(window)
#     # print(color.show())
#
#     Hexadecimal_value = colorchooser.askcolor()
#     print(Hexadecimal_value)
#     frame1.configure(background= Hexadecimal_value[1])
#
# background_changer()
#
# from tkinter import filedialog
# import os
#
# def func():
#     file= filedialog.asksaveasfilename(defaultextension='.txt',
#                                     #   initialfile='Yo'
#                                     initialdir= os.getcwd(),
#                                     filetypes=[("Textfile",".txt"),
#                                                 ("PythonFile",'.html'),
#                                                 ("All Files",".*")])
#
#     file = os.open('texting.txt',os.O_RDWR)
#     os.fdopen(file,'a').write("My Mission Was Completed Brother")
# # initialdir=r'C:\Users\mahen\bitepy\allfiles' ye wali directory open karta
# # initialfile=r'C:\Users\mahen\bitepy\allfiles' ye automatic file select kar leta hai directory open karke
#
# a = Button(fram2, text="Sumbit",
#            command=func,
#            fg='pink',
#            background='green'
#            , font=('myfont.ttf 14 bold'))
# a.grid(row=3)
#
# window.mainloop()
#
#
#
#_____________________________________Best Tutorial For Tkinter Start____________________________________________

from tkinter import *
from tkinter import ttk
import tkinter.font

#______________________________________________windows________________________________________________________



window =  Tk()
window.geometry('400x400')
window.title("Camera")
window.iconbitmap(r"C:\Users\mahen\Downloads\photographer_photo_camera_photography_icon_230640.ico") # window me icon set karenaka hai
#  


#______________________________________Labels_________________________________________________________________
# fontt = tkinter.font.Font(family= "myfont.ttf",weight='bold',size=13,underline=1,overstrike=1)
# label1 = Label(window, font=fontt, text="Cancel", padx=15, pady=50, bg='green', relief='raised').pack(fill=BOTH,expand="True")
# label2 = Label(window, font=fontt, text="Cancel", padx=15, pady=50, bg='green', relief='raised').pack(fill=BOTH,expand="True")
                  
#--------------------------------------------EntryBox------------------------------------------------------------------



Entry_StoredInputs = StringVar()

#Font.........
fontt = tkinter.font.Font(family= "myfont.ttf",weight='bold',size=13,underline=0,overstrike=1)

#EntryBox........
Entry_Box = Entry(window,textvariable=Entry_StoredInputs,relief='raised',font=fontt)
Entry_Box.config(show="_",fg='black')

def __sumbitbuttonForEntryBox():
    # Tune jo text maara O text lene ke do tarike hai
        # 1st :-> Direct text Lena  Ka Tarika-> Entry_Box.get() # Text Aajayenge
        # 2nd :-> String.var() -> Is variable ko create kar (EntryBox) Me textvariable = String.var bana huva variable daal de

    print(Entry_Box.get())
    print(Entry_StoredInputs.get())

#Button....
Submit_Button = Button(window,font=fontt,command=__sumbitbuttonForEntryBox(),text='Submit')
Submit_Button.config(width=25,fg='black',bg='white',activebackground='green')


Entry_Box.pack()
Submit_Button.pack()




#-----------------------------------------RadioButton----------------------------------------------------------


Radion_text_Store =  IntVar()
Radion_text_Store2 = IntVar()
Radion_text_Store3 = IntVar()


Radion = Radiobutton(window, text="Samosa",value=1,variable=Radion_text_Store,state='normal')
Radion.pack(side=LEFT,anchor='nw')
Radion2 = Radiobutton(window, text="Dosa",value=2,variable=Radion_text_Store2)
Radion2.pack(side=BOTTOM,anchor='nw')
Radion3 = Radiobutton(window, text="Chicken",value=3, variable=Radion_text_Store3)
Radion3.pack(side=RIGHT,anchor='nw')

#Radionbutton Import :

#1) -> State = Disbled or Normal :-> Radio Button show hota hai ose select nahi karsakte hai

#cget() -> keyword arguement ye text return karta hai jo radiobutton text diya ho
#get() -> jo value set ki hai radionbutton me o value return karti hai

def __sumbitbuttonForRadionButton():

    print("This is Radion",Radion.cget('text'))
    if Radion_text_Store.get()==1:
        print(" Order : Samosa ")

    if Radion_text_Store2.get()==2:
        print(" Ordered : Dosa ")

    if Radion_text_Store3.get()==3:
        print("Ordered : Chicken")

#Button.....
Button(window,text='Order',command=__sumbitbuttonForRadionButton).pack()


#--------------------------------------------Checkbutton-------------------------------------------------------------------

#cget() -> keyword arguement ye text return karta hai jo radiobutton text diya ho
#get() -> jo value set ki hai radionbutton me o value return karti hai


Checkbutton_Stored_Data1 = IntVar()
Checkbutton_Stored_Data2 = IntVar()
Checkbutton_Stored_Data3 = IntVar()

Checkbutton1 = Checkbutton(window,selectcolor='green',text='Idli',fg='black',bg='pink',variable=Checkbutton_Stored_Data1,offvalue=0,onvalue=34)
Checkbutton1.pack(side=LEFT,anchor='nw')

Checkbutton2 = Checkbutton(window,selectcolor='white',text='Idli',fg='black',bg='pink',variable=Checkbutton_Stored_Data2,offvalue=0,onvalue=34)
Checkbutton2.pack(side=LEFT,anchor='w')

Checkbutton3 = Checkbutton(window,selectcolor='white',text='Idli',fg='black',bg='pink',variable=Checkbutton_Stored_Data3,offvalue=0,onvalue=34)
Checkbutton3.pack(side=LEFT,anchor='w')


def __SubmitbuttonForCheckbutton():
    if Checkbutton_Stored_Data1.get():
        print("You Are Ordered Idli")
        Checkbutton1.deselect()

    if Checkbutton_Stored_Data2.get():
        print(("You Are Ordered : Dosa"))
        Checkbutton2.deselect()

    if Checkbutton_Stored_Data3.get():
        print("You Are Ordered : Bonde")
        Checkbutton3.deselect()
    print(Checkbutton1.cget('text'))



OrderedCheckbox = Button(window,command= __SubmitbuttonForCheckbutton,text="Please Order",fg='Black')
OrderedCheckbox.pack(side=LEFT, anchor='n')



#------------------------------------------------Combobox-------------------------------------------------------------
def Combobox_selected(Event):
    print("You Are Selected",food_selected.get())

food_selected = StringVar()
Comboboxx = ttk.Combobox(window,width = 25,   state='readonly',textvariable=food_selected,values=("Dosa","Allu","Bonde","Battery","Background"))
Comboboxx.bind("<<ComboboxSelected>>",Combobox_selected)
Comboboxx.pack()

#-----------------------------------------------Listbox--------------------------------------------------------------------
Listboxx = Listbox(window,selectmode=EXTENDED)
Foodnames = ["dosa","idli","Samosa","Visualcode","Python"]

def ListBox_selected(event):
    print("You Are Selected {} ".format(Listboxx.get(ANCHOR)))
    print(Listboxx.curselection())
    
    



for names in Foodnames:
    Listboxx.insert(END,names)
    
def Delete_and_Backspace(uou):
    # Listboxx.delete(0,END) # listbox clear kardega 0 se last tak
    # Listboxx.delete(Listboxx.curselection()) # jo delete karna hai uska name daalo 
    pass


Listboxx.bind("<<ListboxSelect>>",ListBox_selected)
# Listboxx.bind("<<ListboxSelect>>",Delete_and_Backspace)



Listboxx.pack(side=LEFT,anchor='nw')
window.mainloop()
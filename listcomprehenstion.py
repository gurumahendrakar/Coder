# name = "Shivaji"
# a  = "Name is Guru Brother" if name=="Guru" else  "Naam Guru Nahi Hai" if name=="Shivaji"  else -3
#
# print(a)
#
# # list comprestion me oske under likha hamesha left me likhate hai
#
#
# #normal comprehenstion and nested comprehenstion...
#
# #Nested Comprehenstion....
# a  = "Name is Guru Brother" if name=="Guru" else  "Naam Guru Nahi Hai" if name=="Shivaji"  else -3
#
# #Normal Comprehenstion....
# b = ["Guru" for i in range(5) if i==2]
# print(b)
#
#
# # Tuple me comprehenstion karte ho to o genrator object bana hai jis aapp ek hi baar use kar sakte ho
#
# genrator_listcomprehenstion = (i for i in range(8))
# for i in a:
#     print(i,end=" ")
#
#
# # list empty now sab value foor loop me madat se use kar liye
# #no iteration is list is empty
# for i in a:
#     print(i)
#
#
#
# # list comprehesntion....
#
# list_comprehenstion = [i for  i in range(8)]

<<<<<<< HEAD

# a = []

# [a.append(x) for x in range(0,100) if x%2!=0 if x%27==0]

# print(a)




# de = lambda x:x*x


# def ca__(func,iterable):
#     store_ = []

#     for x in iterable:
#         store_.append(de(x))

    
#     return store_


# value = ca__(de,[1,2,3,4,5])
# print(list(value))


# import itertools
# import functools
# one = [[1,2,3],[3,2,1]]
# reduce  = functools.reduce(lambda x,y: x+y ,one)
# print(reduce)



#-------------------------------Important----------------------------------------

#
# / isse pehle keyword arguments nahi de sakte
# * iske baad keyword arguments dene padenge

def fun(one,/,*,two,three,four):
    print('hlo brother')


fun(2,two=2,three=3,four=3)


#----------------------------------------------------------------------------------------------------------

import tkinter

window = tkinter.Tk()



menu = tkinter.Menu(window)
menu2 = tkinter.Menu(menu)

menu.add_command(label='hlo brother')
menu.add_cascade(label='File',menu=menu2)
menu.add_separator()
menu2.add_command(label='C Drive')


window.config(menu=menu)

window.mainloop()




=======
>>>>>>> a61a249b50f3ad60a15e2e96bd630d1606ad1418

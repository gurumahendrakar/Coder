
#
# class class_help:
#
#     def __init__(self):
#
#         self.Mobile = "Samsung Company"
#

    # def __class__dict__help(self):

    #     """
    #     print(class_help.__dict__) #changes not possible (access only )  <class 'mappingproxy'> hai
    #     print(self.__dict__) #changes possible 'class __dict__'
    #     """
    #     print(class_help.__dict__) #changes not possible (access only )  <class 'mappingproxy'> hai
    #     print(self.__dict__) #changes possible 'class __dict__'

    # def __doc__help(self):
    #     """isme Bataya hai ki class type me classObject  ---- __dict__ me kya farak hai


    #     # (normal function and proctecter) me hi aap __doc__ string acces  kar sakte hai
    #     # private me aap __doc__string access nahi kar sakte hai

    #     """

    # def __setitem__(self,key,value):
    #     # ye Object()[key] = value
    #     # isko add karne ke liye ek dict chahiye  : dict_name = {"Guru":"Mahendrakar"}

    #     #before dict_name  = {"Guru":"Mahendrakar"}
    #     self.dict_name = {"Guru":"Mahendrakar"}

    #     #Key = "clg"
    #     #value = "Cb collage"

    #     self.dict_name[key] = value

        #after : -> dict_name = {"Guru":"Mahendrakar","Clg":"Cb Collage"}

        # print("Updated Your Details")

    # def __getitem__(self,Key):

    #     #Object()[Key] # His Return dict value
    #     dict_name = {"Guru":"Mahendrakar"}

    #     return dict_name.get(Key,"No One Have Key") #Returne Key Value

    # def __setattr__(self, name,set_value):
    #     # Note important
    #     #object().a = "guru" (object se kitne bhi value bannege hame batayega)

    #     print(" Name : {}  Key : {} ".format(name,set_value))
    #     self.__dict__[name] = set_value
    #     print(" Object __dict__ KEY Was Added Succusfully")



    # def __str__(self):
    #     # __str __ aur __repr __ dono Hai to __repr__ First Call Hoga

    #     return "Good Morning My Owner"

    # def __repr__(self):

    #     # __str __ aur __repr __ dono Hai to __repr__ First Call Hoga
    #     print("Welcome My Owner")


    # def __getattr__(self, name):
    #     "Object Deleted "
    #     return "Attribute Is Not Present in Object or Class"

#
#     def __set__(self,key,value):
#         print("Setting Your Value...")
#         self.__dict__[key] = value
#
#     def __get__(self,name):
#         return "Abe Chootiye"
#
#     def __delattr__(self, __name):
#         del self.__dict__[__name]
#         print("Succusfully Deleted")
#
#     def __getattribute__(self,attribute):
#             return self.__dict__[attribute]

#     def __del__(self):
#         print("Garbage Collecter Is Executed")
		  # Ye Automaticlly __call__ hota hai jab program pura khatam hojata hai

# class_helps = class_help()
# class_helps.Guru = "Mahendrakar"
# del class_helps.Guru
#__str__()
#__repr__() # __repr__ call first


# class_helps["Clg"] = "Mahendrakar" # __setitem__
# class_helps['Clg'] # __getitem__

# __set__ and __get__ practice is not completed




#___________________________________________________________________________________________________________________________
#.......................................__slots__..........................................................................





# class slotss:
#     __slots__ = ["x","y","z","__dict__"]


# slot = slotss()
# slot.x = 10
# #__slots__('x','y','z')

# #slot.l =20 # Attribute error dega slot me jo variable daala hai vahi varible attributes bana sakte ho
# slot.y = 20
# slot.z = 30
# slot.x = 100 # changes possible defined varibles

# #changes_slots...
# #__slots__ = ["x","y","z"] # before

# #__slots__ = ['x','y','z','__dict__'] __dict__ likhanne ke baad aap konse bhi attribute bana sakte ho
# # ... __slots__ me jo variables hai o show nahi karega ouput dhekho niche hai waise

# slot.name = "Guru Mahendrakar"
# #output = {'name': 'Guru Mahendrakar'}
# print(slot.__dict__) # 



#-------------------------------------------Slots One More Examples_________________________________________________________________________________


# class uou:
#     __slots__ = ['x','y']
#
#
# u = uou()
# u.x = 1
# u.y = 2
#
#
# class uou2(uou):
#
#     def __init__(self):
#         self.name = "Guru Mahendrakar"
#
#
#
# uu = uou2()
# uu.x = 1
# uu.y = 2
# uu.g = 3
#
#
#
# print(uou2.__dict__.get('__slots__',-1)) # jisme solt dala huva hai usko interhated karte ho to jisme daala hai usme class ke dict me __slots__ avilabel nahi rehta hai



#----------------------------------------------- __get__ & __set__ & __set_name__ --------------------------------------------------------------

#This is Also Important Please Leran Brother

# class function:
# 	def __set_name__(self, object, name):
# 		print( " Owner : {}  OwnerClass_name :  {} ".format(object,object.__name__))
# 		print("Object Created Name :  {} ".format(name))
#
# 	def __get__(self, instance,name):
# 		return 'Guru'
#
#
# 	def __set__(self, instance, value):
# 		self.__dict__.update({instance:value})
# 		print(self.__dict__)
#
#
#
# class function2:
# 	function1  = function()
#
#
#
# fu = function2()
#
# fu.function1 = "Guru Mahendrakar"
#





#-----------------------------------------isintance & issubclass--------------------------------------------------------

#
# class one:
#
# 	def __Yobrother(self):
# 		print("Hey Man ! How Are You Brother")
#
#
# class two(one):
# 	pass
#
#
# class three(two):
# 	pass
#
# class four():
# 	pass
#
# oneObject = one()
# twoObject = two()
# threeobject = three()
#
#
# print(isinstance(oneObject,(one))) # oneObject  one class ka object hai kya -> True
# print(isinstance(oneObject,(one,two))) # oneObject object (one or two) Me se kisika object hai -> True
# print(isinstance(oneObject, (two))) # oneObject two Class Object Hai Kya -> False
#
# print(issubclass(two,one)) # -> two class ne one class inheritate kiya hai kya -> True
# print(issubclass(one,two)) # -> one ne two class ko in inheritate kiya hai kya -> False
# print(issubclass(three,(one,two,three))) #-> In Teeno Me Kisike Inheritate Kiya Hai Kya
#
#
# print(help(three)) # Ye Batayega ki Konse Konse Class me jaake check karega -> (His return Docomention)
#
# # ----help--- docomention-----
# #  |  Method resolution order:
# #  |      three
# #  |      two
# #  |      one
# #  |      builtins.object
# #  |
# #  |  Data descriptors inherited from one:
# #  |
# #  |  __dict__
# #  |      dictionary for instance variables (if defined)
# #  |
# #  |  __weakref__
# #  |      list of weak references to the object (if defined)
#
#
#
# print(three.mro()) # Ye list return karta hai


# ---MRO LIST------
# [<class '__main__.three'>, <class '__main__.two'>, <class '__main__.one'>, <class 'object'>]
	#ISKE SAARE CLASS ATTRIBUTES



#-------------------------------------------Private & Protectors-----------------------------------------

# __ Private
#_Protector


# class one:
#
# 	def __yo(self):
# 		return  ("Hey Man ! Whatsapp Buddy")
#
#
#
#
# class two(one):
# 	pass
#
# One = one()
# Two = two()
#
# print(one.__dict__)
#
# #---------------------------------
#
# #Private --- Accesing ---
# print(Two._one__yo())


#------------------------------------


#
# import collections
# from multipledispatch import dispatch
#
# class method:
#     __slots__ =  ['one','two','three']
#
#     @dispatch(int,int)
#     def _one(self,a,b):
#         return a+b
#     @dispatch(str,int,int)
#     def _one(self,a,b,c):
#         return a+str(b)+str(c)
#
# a = method()
# print(a._one(3,3))
# print(a._one('Guru',3,2))
#
#
#


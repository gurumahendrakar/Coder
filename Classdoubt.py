
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


    #     # (normal function and proctecter) me hi aap __doc__ string acces nahi kar sakte hai
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




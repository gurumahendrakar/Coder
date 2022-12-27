from pandas import Series as panda

#...........................................................pandas.Series..................................................................

import sys

names = ['Guru','Chetan',"Pravin","Gundya","Ajay"]
dict = {'Guru':"Mahendrakar",'Pandas':"Python","Python":"WebDevelopment"}
data = panda(data=dict,copy=True)

print(data.axes) # #indexs return in list
print(data.dtype) # return object
print(data.flags)
print(data.index)
print(data.keys()) # return keys
print(data.values) # return values

print()




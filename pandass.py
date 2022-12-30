from pandas import Series as panda,read_csv

#...........................................................pandas.Series..................................................................

import sys

names = ['Guru','Chetan',"Pravin","Gundya","Ajay"]
dict = {'Guru':"Mahendrakar",
        'Pandas':"Python",
        "Python":"WebDevelopment",
        'Python':'Fucking'}
data = panda(data=dict,name='My Dream')

# print(data.name)
# print(data.size) # 3 bytes
# print(data.dtype) # object I Dont Know Y not return datatype
# print(data.is_unique)
# print(data.axes) # #indexs return in list
# print(data.dtype) # return object
# print(data.flags)
# print(data.index) # returning indexs
# print(data.keys()) # return keys
# print(data.values) # return values



#-------------------------------Read-csv-------------------------------------------------

csvdata = read_csv('S:/csvfiles/data.csv', encoding='latin-1',squeeze=panda)
print(csvdata['industry'].tail(10))





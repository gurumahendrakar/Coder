# import csv
#
#
# with open('texting.txt','r+',newline='') as csvfilee:
#     csvfilee = csv.writer(csvfilee) # Delimiter Argument Not Set Here
#
#     csvfilee.writerow(["Name","Roll"],)
#     csvfilee.writerow(["Guru",39])
#     csvfilee.writerow(["Nitin Mahendrakar",29])
#
#
#     csvfilee.writerows([["Name","Shubham"],["Pravin",29],["Deepak",39]])
#
#     with open('texting2.txt','w') as dictwrtr:
#         dictwr = csv.DictWriter(dictwrtr,fieldnames=["Firstname","Lastname","Roll"],delimiter="-")
#         dictwr.writeheader()
#
#         dictwr.writerow({"Firstname":"Guru","Lastname":"Mahendrakar",})
#
#         dictwr.writerows([{"Firstname":"Guru","Lastname":"Mahendrakar"},{"Firstname":"Shubham ","Lastname":"Kshirsagar",},{"Firstname":"Pravin","Lastname":"Mahendrakar",}])
#
#
#
#     with open('texting.txt') as reader:
#         print(list(csv.reader(reader))) # His Gives Iterator Object
#
#         #Writer...............
#         #[
#         #   ['Name', 'Roll'],
#         #   ['Guru', '39'],
#         #   ['Nitin Mahendrakar', '29'],
#         #   ['Name', 'Shubham'],
#         #   ['Pravin', '29'],
#         #   ['Deepak', '39']   ]
#
#     with open('texting2.txt') as dictreader:
#
#     # Dictreader Examples...............
#
#         # Delimiter : | ye Hone pe output...
#         #     {'Firstname|Lastname|Roll': 'Guru|Mahendrakar|'}
#         #     {'Firstname|Lastname|Roll': 'Guru|Mahendrakar|'}
#         #     {'Firstname|Lastname|Roll': 'Shubham |Kshirsagar|'}
#         #     {'Firstname|Lastname|Roll': 'Pravin|Mahendrakar|'}
#
#
#         #Delimiter : , (comma) Ye Hone Pe...
#             # {'Firstname': 'Guru', 'Lastname': 'Mahendrakar', 'Roll': ''}
#             # {'Firstname': 'Guru', 'Lastname': 'Mahendrakar', 'Roll': ''}
#             # {'Firstname': 'Shubham ', 'Lastname': 'Kshirsagar', 'Roll': ''}
#             # {'Firstname': 'Pravin', 'Lastname': 'Mahendrakar', 'Roll': ''}
#
#         for lists in (list(csv.DictReader(dictreader))):
#             print(lists)
#


# import csv
# def flower_finder(filename,flowername:str):
#     with open('texting.txt','r+',newline='') as csvfile:
#         csvwriter = csv.DictWriter(csvfile,fieldnames=["flowers","price"])
#         csvwriter.writeheader()

#         csvwriter.writerows([{'flowers':'petunia','price':200},
#                              {'flowers':'alyssum','price':2000},
#                              {'flowers':'begonia','price':3000},
#                              {'flowers':'sunflower','price':333},
#                              {'flowers':'coelius','price':333}])

#         with open(filename,'r+') as csvreader:
#             all_details = list(csv.DictReader(csvreader))

#             for o in all_details:
#                 print(o)


# flower_finder('texting.txt','petunia')


string = '200/2+77+2/2/2'
print(string)
index_ = []
new_string = ''
value = 0 

for txt in string:
    if txt in '*/-+':
        new_string+='-'
    else:
        new_string+=txt


for index,i in enumerate(string):

    if i in '+/-*':
        index_.append(string.index(i,index))

newlist = new_string.split('-')
newlist = list(map(int,newlist))
x,y,w,c,old,value = 0,1,0,0,newlist.copy(),0
print('_indexs len is : {}'.format(len(index_)))
while w<=len(index_)-1:
    
    if w <=len(index_)-1:
        print('Show Error--------------')
        print(newlist)
        if string[index_[w]]=='/':
            if string[index_[w+1]]=='/':
                if value==0 and string[index_[w+1]]=='/':
                    old_value = old[x]/old[y]
                    del newlist[y]
                    newlist.insert(y,old_value)
                    value+=1
                else:
                    del newlist[y]
                    newlist.insert(y,newlist[x]/newlist[y])
                    value=0

            else:
                print('Hey I\'m Another Oprator')

    x,y,w= x+1,y+1,w+1
        
print('Result---',newlist)
print('eval result',eval(string))

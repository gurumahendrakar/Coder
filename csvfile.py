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
import os

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



string_ = '33/3/3+5+3+5+3/33+99+6+658+5/8+9+62+972+5+586+58+8/8/5/58/8+99/8/8/8/8/8*8'

print(string_)
operator_index = []
new_string = ''
onemore_stirng_ = ''
twomore_string = ''
class Ool:



    def ___indexfinder(self,string):

        storer = []
        for index,i in enumerate(string):
            if i in '/+-*':
                storer.append(onemore_stirng_.index(i,index))

        else:
            return storer

    def spliting(self):
        global  new_string
        for txt in string_:
            if txt in '*/-+':
                new_string += '-'
            else:
                new_string += txt

    def indexing_adder(self):
        for index, i in enumerate(string_):
            if i in '+/-*':
                operator_index.append(string_.index(i, index))



    def devide_cal(self,index_list: list):
        global onemore_stirng_
        one_time = True

        x,y,idx_counter = 0,1,0
        devide_couting = 0
        count = 0
        while idx_counter<len(index_list):

            if string_[operator_index[idx_counter]]=='/':

                if operator_index[-1] == string_.index(string_[operator_index[idx_counter]],operator_index[idx_counter]):

                    onemore_stirng_ = onemore_stirng_[:self.___indexfinder(onemore_stirng_)[-1]]

                    onemore_stirng_+= string_[operator_index[idx_counter-(count+1)]] + str(numbers_index[x] / numbers_index[y])


                if y<=len(numbers_index)-2:

                    if string_[operator_index[idx_counter+1]]=='/':
                        count+=1
                        devide_couting = numbers_index[x] / numbers_index[y]
                        numbers_index[y] = devide_couting

                    else:
                        if onemore_stirng_:
                            onemore_stirng_ = onemore_stirng_[:self.___indexfinder(onemore_stirng_)[-1]]
                            

                            find_ = ''
                            if count==0:
                                onemore_stirng_+= string_[operator_index[idx_counter-1]] +   str(numbers_index[x] / numbers_index[y])

                        else:
                            onemore_stirng_ += string_[operator_index[idx_counter - (count+1)]] + str(numbers_index[x] / numbers_index[y])
                            count = 0

            else:
                if one_time:
                    one_time = False
                    onemore_stirng_+=  str(numbers_index[x]) + str(string_[operator_index[idx_counter]]) + str(numbers_index[y])
                else:
                    onemore_stirng_+= str(string_[operator_index[idx_counter]]) + str(numbers_index[y])

            x,y = x+1,y+1
            idx_counter+=1

Oo = Ool()
Oo.spliting()
Oo.indexing_adder()

numbers_index = list(map(int,new_string.split('-')))
Oo.devide_cal(operator_index)

print(onemore_stirng_)
print(onemore_stirng_.strip('/'))
print(eval(string_))

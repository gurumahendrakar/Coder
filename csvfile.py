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


import csv
def flower_finder(filename,flowername:str):
    with open('texting.txt','r+',newline='') as csvfile:
        csvwriter = csv.DictWriter(csvfile,fieldnames=["flowers","price"])
        csvwriter.writeheader()

        csvwriter.writerows([{'flowers':'petunia','price':200},
                             {'flowers':'alyssum','price':2000},
                             {'flowers':'begonia','price':3000},
                             {'flowers':'sunflower','price':333},
                             {'flowers':'coelius','price':333}])

        with open(filename,'r+') as csvreader:
            all_details = list(csv.DictReader(csvreader))

            for o in all_details:

                if o['flowers']==flowername:
                    print('Flower name  : {}---------- selling Price Is : {} '.format(o['flowers'],o['price']))
                    return
            else:
                print('--------------You Are Entered Flower is not here---------------')


flower_finder('texting.txt','petunia')
import csv
#
# with open('texting.txt','r+',newline='') as writing:
#     csv_writer = csv.writer(writing)
#     csv_writer.writerows([['Guru',"Gundya","Chetan"],['Guru',"Gundya","Chetan"],['Guru',"Gundya","Chetan"]])
#
#     with open('texting.txt','r') as reading:
#         csv_reader = csv.reader(reading) # return Genrator Object Only One time use
#
#         for x in csv_reader:
#             print(x)


#-----------------------------------------Dict Writer  & Dict Reader------------------------------------------------------------

with open('texting.txt2','r+',newline='') as dictwriteing:
    dict_writer = csv.DictWriter(dictwriteing,delimiter='-',fieldnames = ['firstname','secondname','thirdname'])

    dict_writer.writerow({'firstname':"Mahendrakar","secondname":"Mahendrakar",'thirdname':'yo'})
    dict_writer.writerow({'firstname':"1","secondname":"2",'thirdname':'3'})
    dict_writer.writerow({'firstname':"4","secondname":"5",'thirdname':'6'})

    with open('texting.txt2',newline='') as dictreader:
        dict_reader = csv.DictReader(dictreader)
        for x in dictreader:
            print(x)

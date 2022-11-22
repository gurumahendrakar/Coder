import csv



with open('texting2.txt','w',newline='') as csvfilee:
    # csvfilee = csv.writer(csvfilee)
    # #csvreader = csv.reader(csvfilee) # return iterator object
    
    # csvfilee.writerow(["Name","Roll"])
    # csvfilee.writerow(["Guru",39])
    # csvfilee.writerow(["Nitin Mahendrakar",29])

    # csvfilee.writerows([["Name","Roll"],["Guru",29],["Nitin",39]])

    with open('texting2.txt','w') as dictwrtr:
        dictwr = csv.DictWriter(dictwrtr,fieldnames=["Firstname","Lastname","Roll"],delimiter="|")
        dictwr.writeheader()

        dictwr.writerow({"Firstname":"Guru","Lastname":"Mahendrakar",})

        dictwr.writerows([{"Firstname":"Guru","Lastname":"Mahendrakar"},{"Firstname":"Guru","Lastname":"Mahendrakar",},{"Firstname":"Guru","Lastname":"Mahendrakar",}])


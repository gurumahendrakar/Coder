name = "Shivaji"
a  = "Name is Guru Brother" if name=="Guru" else  "Naam Guru Nahi Hai" if name=="Shivaji"  else -3

print(a)

# list comprestion me oske under likha hamesha left me likhate hai


#normal comprehenstion and nested comprehenstion...

#Nested Comprehenstion....
a  = "Name is Guru Brother" if name=="Guru" else  "Naam Guru Nahi Hai" if name=="Shivaji"  else -3

#Normal Comprehenstion....
b = ["Guru" for i in range(5) if i==2]
print(b)


# Tuple me comprehenstion karte ho to o genrator object bana hai jis aapp ek hi baar use kar sakte ho 

genrator_listcomprehenstion = (i for i in range(8))
for i in a:
    print(i,end=" ")


# list empty now sab value foor loop me madat se use kar liye
#no iteration is list is empty 
for i in a:
    print(i)



# list comprehesntion....

list_comprehenstion = [i for  i in range(8)]
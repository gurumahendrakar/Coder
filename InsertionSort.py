import time

x = 0
y = 1

# 1st Logic : Pehle Maine small index dhonda (highervalue,smallvalue)
<<<<<<< HEAD
# 2nd Logic : smallvalue  ki 0 hone ke tak loop chalaya (smallvalue<highervalue value ko exhange karenge) bada nahi/
# small_value aur higher value decrease karenge 
=======
# 2nd Logic : highervalue ki 0 hone ke tak loop chalaya (smallvalue<highervalue value ko exhange karenge) bada nahi/
# highervalue_decrease karenge
>>>>>>> a61a249b50f3ad60a15e2e96bd630d1606ad1418



array = [8,-3,5,2,5,6,67,36,3,3,6,7,7,89,9,-8,-4,6,-4,6,3,5,3,63,6,3,6]
print("Orginal Array : ",array)
class Insertionsort:

    def _indexfinder(self,array):
        global x,y
        while y<=len(array)-1:
            if array[x]<=array[y]:
                x+=1
                y+=1
            else:
                return x,y

    def _sorter(self):
        global x,y
        if x<=len(array)-1:
            if isinstance(self._indexfinder(array),tuple):
                i,j= self._indexfinder(array)
<<<<<<< HEAD

=======
>>>>>>> a61a249b50f3ad60a15e2e96bd630d1606ad1418
            else:
                i = -1

            while 0<=i:
                if array[i]<array[j]:
                    i-=1
                else:
                    array[i],array[j] = array[j],array[i]
                    j-=1
                    i-=1

        if x<len(array)-1:
            self._sorter()

Inser = Insertionsort()
Inser._sorter()
print(f"Manully Sorted Array : {sorted(array)}")
print(" My Sorted Array : ",array)

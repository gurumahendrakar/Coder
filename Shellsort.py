listt = [7,4,6,3,2,0,-8,2,5,-6]
i = len(listt)
print("origanal list",listt)

class shellsort:

    def shellsort(self,list):
        devided_integer = len(list)//2

        def cracking_sort(list):
            a = 0
            b = devided_integer

            while a!=devided_integer and b!=len(list)-1:
                if listt[a]>=listt[b]:
                    listt[a],list[b] = listt[b],listt[a]
                
                a+=1
                b+=1
            else:
                if listt[devided_integer]>listt[len(list)-1]:
                    listt[devided_integer],list[len(list)-1] = listt[len(list)-1],listt[devided_integer]
        cracking_sort(list)

        def split_sorting():
            global i
            list_len = len(listt)//2
            a,b = 0,list_len

            while 0!=i:
               
                c = (a-len(listt))>=list_len
                d = (b-len(listt))>=list_len
                while list_len!=0  and  c>=list_len and b>=list_len :

                    print("A    : {}  B      : {}".format(a,b))
                    print("AFter sorting list : {} ".format(listt))
                    if listt[a]>=listt[b]:
                        listt[a],list[b] = listt[b],listt[a]
                        a+=list_len
                        b+=list_len
                
                list_len = list_len//2
                i //=2

            else:
                a,b = 0,1
               
                
                while d<len(listt)-2:
                    if listt[a]>listt[b]:
                        listt[a],listt[b] = listt[b],listt[a]
                        

                    
                    
                                          

        split_sorting()
                
object = shellsort()
print(object.shellsort(listt))

print("After list : {listt}".format(listt = listt))
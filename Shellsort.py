listt = [8,35,3,4,3,43,3,44,23,4,234,2,5,235,324,234,23,42,34,125,25,42,34,2,5,2,42,34,24,214,12,5,5123,412342,134,234,23,4]
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
                c,d = 0,1
                while d<=len(listt)-1:
                    if listt[a]>listt[b]:
                        listt[a],listt[b] = listt[b],listt[a]
                        if (a-1)>=0 and (b-1)>=1:
                            b-=1
                            a-=1
                    else:
                        a = c+1
                        b= d +1
                        c,d = a,b



        split_sorting()
                
object = shellsort()
print(object.shellsort(listt))

print("After list : {listt}".format(listt = listt))
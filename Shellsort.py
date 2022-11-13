listt = [3,9,7,5,2,3,0,6,2,6,1,2]



class Shellsortt:

    def left_midle_right(self):

        if listt[0] > listt[len(listt) // 2]:
            listt[0], listt[len(listt) // 2] = listt[len(listt) // 2], listt[0]

        if listt[len(listt) // 2] > listt[len(listt) - 1]:
            listt[len(listt) // 2], listt[len(listt) - 1] = listt[len(listt) - 1], listt[len(listt) // 2]

        print("Orginal list :  ", listt)
    def firstsorting(self,list,negative,i,j,x,y):
        loopstop = False
        a,b = i,j
        self.left_midle_right()
        while not loopstop:
            if b!=len(listt):

                if listt[a] >= listt[b]:
                    listt[a], listt[b] = listt[b], listt[a]

                a,b= a+x,b+y

            else:
                loopstop = True




shel = Shellsortt()
shel.firstsorting(listt,1,1,(len(listt)//2)+1,1,1)
print("After List    : ",listt)
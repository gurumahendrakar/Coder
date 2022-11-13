
list = [i for i in range(50000)]

class mergesort_:
    def index_sorting(self,list):
        i = 0 
        j = 1
        while j<=len(list)-1:
            if list[i]>list[j]:
                list[i],list[j] = list[j],list[i]

            i+=2
            j+=2
        return list

    def breaks_list(self,list):
        left_ = 0
        right_ = 0
        if len(list)%2==0:
            left_ = list[:len(list)//2]
            right_ = list[len(list)//2:]
        
        else:
            left_ = list[:(len(list)//2)+1]
            right_ = list[(len(list)//2)+1:]
        return left_,right_
    
    def comparewhile_loop(self,list):
        list = mergesort_.index_sorting(list[0]),mergesort_.index_sorting(list[1])
        i = len(list[0])-1
        j = len(list[1])-1
        orginal_listlength  = len(list[0]+list[1])-1
        duplicate_list = [0]*(orginal_listlength+1)
        count  = 0 
        left_ = 0
        right_ = i+1
        list = list[0]+list[1]
        while left_<=i and right_<=orginal_listlength:
            if  list[left_]<=list[right_]:
                duplicate_list[count] = list[left_]
                left_+=1
            
            else:
                duplicate_list[count] = list[right_]
                right_+=1
            count+=1
        

        if left_>i:
            duplicate_list[count:] = list[right_:]

        else:
            duplicate_list[count:] = list[left_:i+1]

        return duplicate_list

    
    def all_sorted(self,list):
        left_list,right_list = self.breaks_list(list)
        left_mein_ka_left_ka_a ,left_mein_ka_right_ka_b = left_list,right_list
        left_meka_andar_ka_a  ,left_meka_andar_ka_b = self.breaks_list(left_mein_ka_left_ka_a)
        left_meka_andar_andar_ka_a,left_meka_andar_andar_ka_b = self.breaks_list(left_meka_andar_ka_a)
        lefttt_a =self.comparewhile_loop(( mergesort_.index_sorting(left_meka_andar_andar_ka_a) , mergesort_.index_sorting(left_meka_andar_andar_ka_b)))
        left_meka_andar_andar_ka_b,left_meka_andar_andar_ka_bb = self.breaks_list(left_meka_andar_ka_b)
        lefttt_b =self.comparewhile_loop((mergesort_.index_sorting(left_meka_andar_andar_ka_b) , mergesort_.index_sorting(left_meka_andar_andar_ka_bb)))
        left_sorted_a = self.comparewhile_loop((lefttt_a,lefttt_b))
        left_meka_andar_ka_a  ,left_meka_andar_ka_b = self.breaks_list(left_mein_ka_right_ka_b)
        left_meka_andar_andar_ka_a,left_meka_andar_andar_ka_b = self.breaks_list(left_meka_andar_ka_a)
        righttt_a =self.comparewhile_loop(( mergesort_.index_sorting(left_meka_andar_andar_ka_a) , mergesort_.index_sorting(left_meka_andar_andar_ka_b)))
        left_meka_andar_andar_ka_a,left_meka_andar_andar_ka_b = self.breaks_list(left_meka_andar_ka_b)
        righttt_b =self.comparewhile_loop(( mergesort_.index_sorting(left_meka_andar_andar_ka_a) , mergesort_.index_sorting(left_meka_andar_andar_ka_b)))
        left_sorted_b = self.comparewhile_loop((righttt_a,righttt_b))
        return self.comparewhile_loop((left_sorted_a,left_sorted_b))

    
mergesort_  = mergesort_()
import time
c = time.time()
a,b = mergesort_.breaks_list(list)
print(mergesort_.comparewhile_loop((mergesort_.all_sorted(a),mergesort_.all_sorted(b))))
ccc = (time.time()-c)

cc = time.time()
list.sort()
print(time.time()-cc)
print(ccc)
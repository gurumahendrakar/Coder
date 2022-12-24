import dataclasses
import numpyy
import logging
import time


@dataclasses.dataclass(frozen=True,init=True)
class binary:

    def assending__(self,list_,target_):

        assert not target_>list_[-1],'YOur Target is very high brother'

        x,y,z, = 0,len(list_),0

        while True:
            print(x,y)
            z = (x+y)//2

            if target_==list_[z]:
                return '__index__ is : {}'.format(z)
            #target__ = 8
            if target_<list_[z]:
                x,y = 0,z-1
                
            
            elif target_>list_[z]:
                x,y = z+1,y
            
            if x==y:
                return 'not found !'


    def desending__(self,list_,target_):
        

        x,y,z = 0,len(list_),0

        while list_[z]!=target_:
            z = (x+y)//2

            if list_[z]>target_:
                x = z+1

            elif list_[z]<target_:
                y = z-1

        else:
            return ' __index__ : {} '.format(z)

        
b = binary()
print(b.assending__([1,2,3,4,666,6666,77777,7777777],77777))
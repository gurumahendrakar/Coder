import dataclasses
import numpy
import logging
import time

@dataclasses.dataclass
class binary:

    def One__(self,list_,target_):

        assert not target_>list_[-1],'YOur Target is very high brother'

        x,y,z, = 0,len(list_),0

        while True:
            z = (x+y)//2

            if target_==list_[z]:
                return '__index__ is : {}'.format(z)
            #target__ = 8
            if target_<list_[z]:
                x,y = 0,z-1
                
            
            elif target_>list_[z]:
                x,y = z+1,y
            
            if x==z:
                return 'not found !'

                        
b = binary()
print(b.One__(list(range(8,55)),8))
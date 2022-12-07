import dataclasses
import numpy
import logging

@dataclasses.dataclass
class binary:

    def One__(self,target_):
        ii,jj = 0,0

        list_ = numpy.arange(0,263)

        if target_>len(list_):
            assert False,'Data_ Does\' not matched '

        unx,llen,check =  0,len(list_)//2,0

        while unx!=target_:
            
            if llen<=target_:
                return llen,'right side-- check'

            else:
                if llen>target_:
                    return llen, 'r side-- check'
        else:
            return "Target_ Achieved_--"

b = binary()
print(b.One__(263))
 __from functools import (lru_cache,total_ordering,singledispatch,singledispatchmethod,partialmethod)


#------------------------------------------------singledispatch--------------------------------------------------
# class functool:
#
#     @singledispatchmethod
#     def tool(self):
#         pass
#
#     @tool.register(list)
#     def _(self,list):
#         print(list)
#
#     @tool.register(int)
#     def _(self,a,b):
#         pass
#
#     @tool.register(str)
#     def  _(self,a):
#         print(a)
#
#
# a = functool()
#

#---------------------------------------------total_ordering-----------------------------------------------------------
#
# @total_ordering
# class functool:
#
#     def __init__(self):
#         self.computer = 0
#         self.me = 100
#
#     def __eq__(self, other):
#         return self.me == other.me
#
#     def __lt__(self, other):
#         return  self.me < other.me
#
#
# b = functool()
# c = functool()
# c.me = 200
# print(b<c)
# print(b>c)
# print(b<=c)
# print(b>=c)
# print(b!=c)
# print(b==c)
#
#

# #============================================lru_cache=================================================================
# import time
# class functool:
#
#     @lru_cache()
#     def __bigdata(self,param):
#         print('__called__')
#         time.sleep(3)
#         print('__Finished__',param)
#
#
# c = functool()



#-------------------------------------------------partial----------------------------------------------------------

class method:

    definit__(self):
        self.one = 'guru'
        self.tool = method._tool

    @partialmethod
    def _tool(self,a,b):
        return 'Your Result -- ',a+b


a = method()
print(a.tool(a,3,))
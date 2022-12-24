import numpy
import numpy as np
#
# a = np.arange(6)
# print('np.newaxis = ',a[np.newaxis]) # nd to conver to 2d list
#
#
# b = np.array([[1,2,3,4,5],[1,2,3,4,5]]  )
#
# print('np array ',b) # 2d list
#
# c = np.zeros((3,2),dtype=numpy.int32) # all value Zeros
#
# print(' np zeros ',c)
#
#
# d = np.ones((3,2),dtype='str')
# print('np ones ',d)
#
#
# e = np.linspace(0,10,num=5)
# print('linespace',e)
#
#
# f = np.sort([5,3,2,1,0])
# print('np sort ',f)
#
#
# a = np.array([[1,2,3,4]])
# b = np.array([[1,2,3,4]])
#
# g = np.concatenate((a,b),axis=0)
# print(g)
#
#
# h = np.arange(0,24).reshape(3,2,4)
# print('n-dim',h.ndim) # konse -d ka hai batayega
#
# print(h.size) # total elements in list
#
#
# print(h.shape) # konse shape me hai tuple hai return karega
#
# print(np.reshape(h,newshape=(1,-1),order='C')) # np.reshape(object,konse shape change karnahai)
#
# print(np.expand_dims(np.array([[4,5,6],[1,2,3]]),axis=0))
#
#
# # ------------------------------------Oprerations-------------------------------------------
#
#
# a = np.array([1,2,3,4,5])
# print(' greater sign ',a>3)
#
# b = np.array([5,6,7,8,9])
#
# print(b[b>7]) # is array ke andar 7 se greater ke list return hone
#
# print((b>10) | (b==5))


#======================================================================
#
# j= np.nonzero(np.array([1,2,3,4])) # 0 hona hi chahiye array me nahi first me konse bhi element ko zero banadega
# print(j)


list__ = np.array(['Guru',"Pravin","Gundya","Chetan","Sumit","Ajay"])
ages__ = np.array([22,10,25,25,2,2])
print(ages__>=2)
print(ages__.nonzero())


import numpy as np

    # 1d Array Vector
    # 2d matrix
    # 3d tensor


    # arange = np.arange(0,12).reshape(3,4)
    # ndarray = np.array([1,2,3]) # normal list ndarray
    # zeros = np.zeros((3,2))
    # ones = np.ones((3,2))
    # identity = np.identity(6,dtype='int8') # diagonal ones create(only rows give)
    # eeye = np.eye(3,4,dtype='int8',order='C') # diagonal ones create method2
    # linespace = np.linspace(10,20,10) #(lower,higher,how many numbers)
    #
    # linespace.view() # (COPY KI TARHA KAAM KARTA HAI BUT AAP ORIGINAL CHANGE KAROGE YE BHI CHANGE HOGA)
    # linespace.copy() # Fully Different Object
    #
    #
    # #----------------------------------2nd Video----------------------------------
    #
    # one_d = np.arange(0,4)
    # two_d = np.arange(0,8).reshape(2,4)
    # three_d = np.arange(0,9).reshape(3,1,3)
    #
    #(shape & ndim ) you can use both
    # print(one_d.shape) #       (8,)
    # print(two_d.shape)#         (2,4)                                           # (3, 1, 3)
    # print(three_d.shape)#       (3,1,3)
    # print(one_d.ndim) #( return 1 because 1d array)
    #
    # print(two_d.size) # How Many Elements in (two_d array)
    #
    #
    # # int-> 4 bytes
    # # float -> 8 bytes
    #
    # print(two_d.dtype) # Andar Konsa Data Store Kiya Hai O return Karega
    # print(one_d.itemsize) # output -> 4 (Because Stores Value in List Is Int)
    # print(three_d.astype(float)) # Ye Naya Array Ga Naye Object ME floats value daalega
    #
    #
    # # arthemetic operations
    #
    # print(one_d*two_d)
    # print(one_d**two_d)
    # print(one_d+two_d)
    # print(one_d-two_d)
    # #print(one_d-two_d) #devide karte waqt yaad rakha oppisite 0 na ho
    #
    # print(two_d@one_d) # dot
    #
    # # boolcomparehension arrays
    #
    # print(two_d>5)
    # print(two_d<5)
    # print(two_d>=5)
    # print(two_d<=5)
    # print(two_d!=5)
    # print(two_d==5)
    #
    #
    # #boolen accesing elements in array
    #
    # print(two_d[(two_d>2) & (two_d%2!=0)])
    # print(two_d[(two_d>2) | (two_d%2!=0)])
    # print(two_d[(two_d>2) ^ (two_d%2!=0)])
    #
    #
    # print(two_d.min())
    # print(two_d.max())
    #
    # print(two_d)
    # # 0 -> Columns 1 -> Rows
    # print(two_d.argmax(axis = 0 )) # columns..
    # print(two_d.argmin(axis=1)) # rows ...
    # print(two_d.sum())
    # print(two_d.mean())
    # print(np.exp(two_d))
    # two_d[:,:] = 1
    # two_d.sort()
    # print('sorted----',two_d)
    #
    #
    # # Konse bhi array me ho  1d array me convert karta hai
    # print(two_d.ravel())
    #
    # print(three_d)
    # print(three_d.transpose()) # (row ka column) (column to row)
    #
    # print(np.hstack((two_d,two_d))) # rows same hone change columns se farak nahi padta
    # print(np.vstack((two_d,[1,2,3,4]))) # v stack me columns matter karenge

    # print(np.vsplit(two_d,2)[1]) # rows wise split
    # print(np.hsplit(two_d,4)[3]) # columns wise split
    #
    #
    # print(three_d)
    #
    # three_d[three_d==0] = 1
    # #
    # #
    # print(np.where(two_d%2==0))
    #
    # print(np.unique(['A',"A","A"],
    #                 return_counts=True,
    #                 return_index=True))
    #
    # a = np.random.random((2, 2))
    # b = np.random.rand(3, 2)
    # c = np.random.choice([1, 2, 3, 4], size=2)
    # d = np.random.randint(0, 8, size=1)
    # e = np.random.randn()
    # f = np.random._generator.default_rng()
    # ff = f.integers(3.2, 8.5, size=5)


import  numpy
from pprint import pprint

l = np.arange(0,16).reshape(2,2,4)
# ll  = np.arange(0,8).reshape(2,4)
# print(a)
# print()
# print(a.transpose())
#

# print(np.cumsum(ll).reshape(2,4))
# print(np.percentile(ll,100))
# print(np.histogram(l,bins=[0,10,20,30,40]))
# print(np.isin([1,2,3,4,5,6],[1,2,3,4,5]))
# print(np.flip(l))
# np.put(l,[0,1],[555,1000])
# print(np.clip(ll,a_min=2,a_max=3))


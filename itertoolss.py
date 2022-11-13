from bz2 import compress
import itertools
import operator

from functools import reduce
#accumplate... 
lists = [6,2,35,62,2]


print(list(itertools.accumulate(lists,func=operator.add)))
# #accumplate(iterable,(func,lamba))) func =me aap jo function paas karoge ye waisa result dega

#chain....


# a = itertools.chain([1,2,3,4,5],[6,7,8,9,10],[11,12,13,14]) # return iterator
# output : - [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
# for i in a:
#     print(i)

# gernrator loop aur kuch nahi hai -> normol loop ki tarha bas ye mermory clean rakhta hai
# print(list(a)) # now list empty


#combinations...


# #aap isko kitne list list de sakte ho o apko ye sab combine karke ek iterator dega 
# #...jo aap ek hi baar use kar sakte ho

# b = itertools.combinations([1,2,3,4,5],3)
# c = itertools.combinations_with_replacement([1,2,3,4,5],2) # same but ye kuch extra combinations dega

# #output dhekh ke samajlo: 
# # output : -> [(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)]

# print(list(b))


#itertools.compress...


list_true_false = [True,False,True,False]
d = itertools.compress([1,2,3,4,2],list_true_false)
print(list(d))
# # konse konse index pe True hai wahi elements return honge
# #output : [1,3]

#itertools.cycle...

# #saare elements khatam hone baad phirse wahi saare elements chanlenge infinite chalenge
# # for i in itertools.cycle([1,2,3,4,5]):
# #     print(i)


#itertools.dropwhile....


print(list(itertools.dropwhile(lambda a :  a<=2 ,[1,2,3,5,6]))) # jo false hoga o return karega 

#itertools.dropwhile(func,iterable)


# ye sirf less than greater than pe work karega



#..................................itertools.groupby....

#important method

# a =itertools.groupby('baddajljdj')

# for i in a:
#     print(i[0],"_",list(i[1]))

# output :      a _ ['a', 'a', 'a']
                # b _ ['b', 'b', 'b']
                # c _ ['c', 'c', 'c']
                # d _ ['d', 'd', 'd']

# a b c d 
#3,3,3,3




# a =itertools.groupby('baddajljdj',key = lambda x: x=='a')
# False _ ['b']
# True _ ['a']
# False _ ['d', 'd']
# True _ ['a']
# False _ ['j', 'l', 'j', 'd', 'j']

#output = ('b', <itertools._grouper object at 0x00000251AF4DF970>)
# character  = how many characters list


#itertools.permutations 



# ye permutaitons and combination same hai

#print(list(itertools.permutations([1,2,3],3))) 

#  output : ->[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]


#itertools.product...

#print(list(itertools.product([1,2,3,4],[1,2])))
# [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2), (4, 1), (4, 2)]

#note : left list ke first element ke saath agle saare elements ke saath tuple list banata hai


#itertools.zip_longest and zip....


# print(list(itertools.zip_longest([1,2,3,4,5],[1,2,3,5,6,9])))
# # zip_longest output :-> [(1, 1), (2, 2), (3, 3), (4, 5), (5, 6), (None, 9)]

# print(list(zip([1,2,3,4,5],[1,2,3,5,6,9])))
#  zip-> [(1, 1), (2, 2), (3, 3), (4, 5), (5, 6)]

 
#zip_longest -> me aage wale me kuch nahi hai to None value banata hai
#zip -> apne paas aage wale ke paas bhi elements hai banata hai nahi to nahi banata

#examples dheklo upar


#itertools.isslice...

# print(list(itertools.islice([1,2,3,4,5],0,7,2))) # same indexing tarha kaam karta hai


#itertoools.slice(iterable,start=0,end,step=1)


     
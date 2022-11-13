import collections

# #collections.namedtuple...
# #___________________________________________________________________________________________________________________
# #...................................namedtuple.......................................................................


# x = (1,2)
# Point = collections.namedtuple("Point",["x","y","z"])
# b = Point(*x,3) #indexing also works    #0   1   2
# print("x",b[0])

# print(b._asdict()) # converted dictonary 
# # ouput :-> {'x': 1, 'y': 2, 'z': 3} 

# #namedtupleObjet.fields....

# print(b._fields) # keys return 
# #output :-> ('x', 'y', 'z')

# #namedTupleobject.make......


# print(b._make((10,20,30))) # naya  object create karega  with  new values

# Point(x=10, y=20, z=30) # but orginal namedtuple me  value change nahi honge


# print(b._replace(x = 100)) # ye bhi new object banega new values ke saath orginal ko 
# #...... nahi chedega


# #_____________________________________________________________________________________________________________________
# #...................................deque............................................................

# # same list ki tarha hai

# dequee_list = collections.deque([1,2,3,4,5,6,7])
# dequee_list.rotate(1)
# dequee_list.append(3)
# dequee_list.extendleft([1,2,3,4])

# #______________________________________________________________________________________________________________________________
# #...................................chainmap.......................................................................

# #collentions.chainmap......


# x = {"a":10,"b":20}
# b = {"c":30,"d":40}
# c = {"e":50,"f":69}

# chain_map = collections.ChainMap(x,b,c)
# indexing_chainmap = chain_map.maps
# # chain_map.maps: ->  [{'a': 10, 'b': 20}, {'c': 30, 'd': 40}]

# #chain_map.maps[] indexing :-> [{'a': 10, 'b': 20}, {'c': 30, 'd': 40}]
# #                         0 index                 1 index

# #chain_map.maps[0] :->  {"a",10,"b",20}
# chain_map2 = collections.ChainMap({},{})
# chain_map2["Guru"] = "Mahendrakar"
# print(chain_map2)

# #chain_map.parents....


# print('parents chainmap :->',chain_map.parents) #  first wali dict ko... chod ke saare dict return kart hai
# #original dict->  ChainMap({'a': 10, 'b': 20}, {'c': 30, 'd': 40}, {'e': 50, 'f': 69})

# #after dict ->  ChainMap({'c': 30, 'd': 40}, {'e': 50, 'f': 69})


# #chain_map.update.......


# chain_map.update({"a":"Guru Mahendrakar"}) # value sirf first vali dict me change honge
# #updated value :-> ChainMap({'a': 'Guru Mahendrakar', 'b': 20}, {'c': 30, 'd': 40}, {'e': 50, 'f': 69})
# #original value :-> ChainMap({'a': 10, 'b': 20}, {'c': 30, 'd': 40}, {'e': 50, 'f': 69})

# print(chain_map)


# #------------------------------------------------------------------------------------------------------------------------
# #.................................Counter........................................................

# a = collections.Counter("aaabbbbccc")
# # ye itertools.groupby ki traha hai aa kitne hai b kitne hai c kitne hai dict me return karega

# #output :->Counter({'b': 4, 'a': 3, 'c': 3})

# #a.iterms....

# print(a.items()) # ouput:-> dict_items([('a', 3), ('b', 4), ('c', 3)])

# print(a.most_common()) # output -> [('b', 4), ('a', 3), ('c', 3)]


# print(a.subtract({"a":1})) # orginal value me isme ka a ka value minus hoga orignal me 
# # ye sirf int pe work karta hai

# print(a)


#..........................defaultdict.........................................................


defaultdictt = collections.defaultdict(list)
 #defaultdict(<class 'list'>, {}) ye
print(defaultdictt['u'])
#after........
# print(defaultdictt) :-> ---->  <class 'list'>, {'u': []} 
listes = [("Guru", "Mahendrakar"),("Nitin" ,"Mahendrakar"),("Gulle", "Biradar"),("Ketan","Biradar"),("shubham","kshirsagar")]

# for (name,sirname) in listes:
#     defaultdictt[sirname.strip()].append(name)

# print(defaultdictt['Mahendrakar'])

# print(defaultdictt['Biradar'])

# print(defaultdictt['kshirsagar'])



#2nd method defaultdict ke jaisa hai

# dicts = {}

# for (name,sirname) in listes:
#     dicts[sirname] = []

# for name,sirname in listes:
#     dicts[sirname].append(name)

# print(dicts)



#......................................Orderdict.............................................\
# jald hi likhenge Bro



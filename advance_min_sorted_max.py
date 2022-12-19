
#important

dict = [{"Car":50000},{"Car":20000},{"Car":30000}]


min = min(dict,key=lambda x: x['Car'])
max = max(dict,key=lambda x: x['Car'])
sorted = sorted(dict,key=lambda x:x['Car'])

print(min) # min(iterable,key=func)
print(max) # max(iterable,key=func)
print(sorted) # sorted(iterable,key=func)

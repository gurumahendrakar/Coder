# # default field example
# from dataclasses import dataclass, field
#
# #........................field..................................
#
# #fronzen = True App Objects Pe attirbutes nahi bana sakte aur na pehle ke attributes ko ched sakte
# # order = True Hone Pe hi aap sorting kar sakte hai
# # A class for holding an employees content
# @dataclass(frozen=True,order= True)
# class employee:
#
# 	# Attributes Declaration
# 	# using Type Hints
# 	name: str
# 	emp_id: str
# 	age: int
#
# 	# default field set
# 	# city : str = "patna"
# 	city: str = field(init = False,default="patna",repr=False,metadata={"Guru":"Mahendrakar"})
#
# 	def __post_init__(self):
# 		print("__post_init__")
# 		return self.age > 2
#
#
# emp = employee("Guru","Sex", 21)
# emp2 = employee("Guru","Sexy",21)
# print(emp==emp2)
#
# #__post_init__ #automated Call
#
# print(sorted((emp,emp2))) # Order= True Hone Pe Hi Work karega
#
# print(emp.__dict__) # __dict__ acces
#
# import dataclasses
# print(dataclasses.asdict(emp)) # dataclass object
# print(dataclasses.astuple(emp)) # dataclass object
# # ==
# # <
# # >
#
# {'name': 'Satyam', 'emp_id': 'ksatyam858', 'age': 21, 'city': 'patna'} #name and values return
# ('Satyam', 'ksatyam858', 21, 'patna') # astuple all value return
#
#
#
# #field(init= True,default='patna',repr)
#
# #init = True karoge to aap city ka argument nahi de sakte o default use karega
#
# #repr = False karoge to O Attribute show nahi karega
#
# #default =  jo argument nahi dena chahte o default rakho init = False ke saath
#
# #metadeta take dictionary {'format':'State'}
#
# # city: str = field(init=False, default="patna", repr=True,
# #                       metadata={'format': 'State'})
#
# #meatadata acces
# print(emp.__dataclass_fields__['city'].metadata) # output :-> Guru Mahendrakar
#
#

#read write os moudle se work kare hai 


# import os
# file = os.open('texting.txt',os.O_RDWR)

#file2 = os.fdopen(file,'a',newline='').write("Hello Brother In the world forget to have anyonelike\n")

# readfile = os.fdopen(file)
# print(readfile.readlines())




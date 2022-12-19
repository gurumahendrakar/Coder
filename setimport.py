
set1 = {1,2}
print(set1.issubset({1,2,5}),"Issubset")
#set1 ke paas jo hai o set2 me ho to aur extra elements honge to bhi True return karega
# Nahi Hai False

print(set1.intersection({1,5,6,7}),"Intersection")
#set1 aur set2 me jo same elements honge wahi return honge baake elements nahi show honge

print(set1.difference({3,2,1}),"Diffrence") # set2 ke paas set1 ke konsi element nahi hai o return elements return honge

print(set1.symmetric_difference({3,2,1}),"Symetric Difference") # set1 -> set2 me check karega konsa element nahi hai
                                        # set2 -> set1 me check karega mera paas ka konsa element iske paas nahi hai

                                        # aur dono ne bataya o return hoga 

print(set1.issuperset([1,2]),"issupreset") # set1 and set2 saare elements same hai to True 
                             # oske aalwa dusre elements to False

print(set1.isdisjoint({5,2}),"isdisjoint") # set1 ke paas jo iske paas o elements nahi hai to True
                            # Ek bhi iske paas set1 ka Element hai To False




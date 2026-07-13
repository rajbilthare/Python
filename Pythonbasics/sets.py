#Sets    values are seprated by commas 
"""
{}  empty set
values cannot be duplicated 
sets are unordered and unsubscriptable
sets is hetrogenous data structure
mutable.
"""


"""s = set()
print(type(s))"""


"""s = {1,2,3,4,5}
print(type(s))"""


"""s = {1,1,2,2,3,3,4,5}  duplicacy not
print(s)"""



"""s = {1,2,3,4,5}  gives error cuz indexing is not there and not ordered,not subscriptable
print(s[4])"""


#item adding for example append() is possible in sets

"""s = {"hello",1,3.14,True}  #boolean value nahi aati
print(s)"""


#implicit conversion and explicit conversion


#methods in sets .
#1. add a new value in set.
#Item adding.
"""s = {1,1,1,2,3,3,3,4,4,5,5}

s.add(100)
s.update([200,300,400,500])   #for adding multiple values inside set we use []
print(s)"""



#2.  removing an element from the set
#1. .remove(element)
"""s = {1,1,1,2,3,3,3,4,4,5,5}
#s.remove(1)
s.discard(6) #agr value exist nhi krti it will return you exact set bina kisi error ke

s.clear() #sb hata dega yeh

print(s)
"""





#Advanced Methods in sets.
"""
1.Union -> Sare elements between 
your sets.
2.Intersection -> Dono set ke beech mai 
jo common values.
3. Difference.-> s1 mai ho pr s2 mai na ho  ya 
s2 mai ho pr s1 mai na ho 
4. Symmetric Diffrence.-> common elements ko chor ke jo 
bach rahe hai woh laa do.
"""



"""
s1 = {1,2,3,4,5}
s2 = {1,24,56,73}
print(f"Union of set1 and set2 is {s1.union(s2)}")
print(f"Intersection of set1 and set2 is {s1.union(s2)}")
print(f"Difference of Set1 and Set2 {s1.difference(s2)}")
print(f"Difference of Set2 and Set1 {s2.difference(s1)}")
print(f"Symmetric Difference between Set1 and Set2 {s1.symmetric_difference(s2)}")"""






"""l = [1,2,1,2,1,1,3,3,3,4,5,6,7]

s = set() 
for i in l:
    s.add(i)

print(s)  """  















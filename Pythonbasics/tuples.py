#Tuples.

"""
(parenthesis)  -> empty Tuple
1. Tuples are ordered.
2. Tuples are hetrogenous.
3. Tuples are Immutable.
4. Tuples can have duplicate values.
5. As there is indexing so slicing is also allowed
"""

"""t = (1,2,"hello",True,3.14)
t[2] = 10   # it gives an type error cuz its not mutable
print(t)"""

#slicing
"""a = (1,2,3,4,5,6,7,8)

print(a[1:7])"""


# to count element  kitni baar aaya we use count
a = (1,1,1,1,1,2,3,4,5,6,7,8)  
print(a.count(1))     #.count() will count the occurence of any value

print(a.index(1))   #First occurrence index.
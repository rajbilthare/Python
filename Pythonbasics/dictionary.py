#Dictionary.
# [] -> List -> Square Brackets
# {} -> Curly Brackets

"""
Keys - Values Pair
Keys cannot be duplicate
but values can be duplicate
1. Hetrogenous
2. Mutable
3. Ordered
"""

#print 40
"""
print(d['b'])
"""

#Creating a new key and assigning value to it.
"""d['e'] = 100
print(d)
"""


"""d = {'a':10, 'b':20, 'c':30, 'd':40 , 'e':100}
d['e'] = 200 #Old value at key 'e' will be overwrite.
print(d)"""


"""info = {'name':'Rahul', 'age':21, 'marks':50.25, 'Present': True}

#1. age -> 25 
info['age'] = 25 #Item Assignment
print(info)"""


#Methods in Dictionary
"""
#1. .values() -> Sirf dictionary ki values.
print(info.values())
"""

"""#2. .keys() -> Sirf Keys milengi.
print(info.keys())"""

#3. .items()
"""info = {'name':'Rahul', 'age':21, 'marks':50.25, 'Present': True}

print(info.items())"""

#4. .pop() -> It accepts key and will remove key and value
"""info.pop('name')
print(info)"""


#5. .get() -> gives you value of a key and if not present gives you None
"""d = {'a':10, 'b':20, 'c':30}
print(d.get('d'))"""



#6. .update({key:value})
"""d.update({'c':500})
print(d)"""


#7. clear() -> Removes all the elements.
d = {'a':100, 'b':200, 'c':300}
"""d.clear()
print(d)"""

del d
print(d)

# print(len(info)) Jitni keys utni length.

info = {'name':'Rahul', 'age':21, 'marks':50.25, 'Present': True}

"""for i in info: #i-> keys
    print(i, info[i]) #info[i] -> Values.
"""


#You will only get values from dictionary.
"""
for i in info.values():
    print(i)
"""

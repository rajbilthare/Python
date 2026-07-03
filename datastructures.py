# data structures is used to store , organize and  manipulate data efficiently

#list 
"""
a = [12,13,134,1,3,13,"ghjjw",True]

print(a[::])"""


# data structures (advanced data types )

# list
#dictionary 
# tuple
# set



#1. list
"""denoted by [] square brackets """
# 1. list is a hetrogenous data structure  - multiple types ka data store krskte hai 
# 2. duplicacy is allowed 
# 3. list is ordered
# 4.  list is mutable(all the value are changable )

# l =[] Empty list

#l[3] = 400  Item Assignment operator 

# l[5] = 100 Index out of range 


#l = [10,20,30,40,50]

# Item wise loop
"""for i in l:
    print(i)"""


#Index wise loop 
"""for i in range (len(l)): #i = 0,1,2,3,4
    print(i,l[i])"""
    #i -> Index of list
    #l[i] -> Item of index 


#l = [1,67,10,25,14,77]

"""for i in l:
    if i > 15:
        print(i)"""

"""for i in range(len(l)):
    if l[i]>15:
        print(i)"""

# sum all the elements of a list
"""
l = [10,20,30,40,50]
sum =0
for i in l:
    sum += i
print(sum)"""

#slicing
# [Start=0:stop-1: step=1]

#Methods in list

#kisi bhi function ke aage . lg gya toh woh method hai 


#1. .append(last me element add krene wala element)


"""l = [10,20,30,40,50]
l.append(100) # append method ek baar me ek hi vaklue add krega  
print(l)"""


#2. extend    # agar mujhe ek list me dusri ya multiple elements daalne ho 
"""l1 = [10,20,30,40,50]
l2 = [60,70,80]
l1.extend(l2)
print(l1)
"""

#3.  .insert (index,value)
"""l1 = [10,20,30,40,50]

l1.insert(1,100)
print(l1)"""


#4. .pop(index value which you want to remove)
"""l1 = [10,20,30,40,50]
l1.pop(1)
print(l1)"""


#5. remove(element)
"""l1 = [1,5,5,5,2,3,4,5]   
l1.remove(5)   # agar duplicate values hai toh first occurrence remove hogi
print(l1)"""


#6. len() -> List lenght
"""l1 = [1,5,5,5,2,3,4,5]
print(len(l1))"""

#questions
#1. Accept list elements and reprint it.

"""n = int(input("enter the size of the list: ")) 
l = []
for i in range(n):   #0,1,2,3,4
    element = input("enter element for your list: ")
    l.append(element)
print(l)   """ 


#2. reverse a list without using slicing.

"""l1 = [10,20,30,40,50]

left = 0
right = len(l1)-1

while left<right:
    l1[left],l1[right] = l1[right],l1[left]

    left += 1
    right += 1

print(l1)
"""
    


# find the largest an second largest

"""l = [10,5,20,15]
largest = l[0] #20
s_largest = l[0] 


for i in l:
    if i > largest:
        s_largest = largest
        largest = i

    elif i > s_largest:
        s_largest = i

print(largest,s_largest)           
"""



"""l = [10,5,20,15]
largest = l[0] 
s_largest = l[0] """

"""
index = 0 #2
sindex = 0 #0


for i in range(len(l)):
    if l[i] > largest:
        s_largest = largest
        largest = l[i]

        sindex = index
        index = i

    elif l[i] > s_largest:
        s_largest = l[i]

        sindex = i

print(largest,s_largest) 
print(index,sindex)"""


#dictionary -- keys and values ka pair keys dupicate nhi ho shakti values ho shakti h
#{} represented by curly braces 
"""hitrogeneous 
mutable
ordered"""
    
"""d = {1:23,'b':66,'x':55}
print(d['b'])"""

#creating a new key and assigning vale to it --> item assignment
"""d['e'] = 100
print(d)

d['b'] = 223 # old value of b will be overrite
print(d)
"""
"""info = {'name' : 'rahul' , 'age':24,'marks':55}
info['age'] = 20
print(info)"""








#methods in dictionary

#5 get() gives you value of a key and if not present gives you none

"""d = {'a':10, 'b':20,'c':30}
print(d.get('d'))"""








#3 merge two dictionaries

"""d1= {'a':10,'b':20}
d2 ={'c':30,'d':40}
  #d1.update(d2)
for i in d2: #i->c,d
    if i not in d1: #cnot in d1
        d1[i] = d2[i]

print(d1)        
"""


#4. frequency count
"""
l = [1,1,1,2,2,3,3,3,6,6,7,7,8,8,8,9]

d = {}
for i in l:
    if i not in d:   #1 not in d
        d[i] = 1
    else :
        d[i] += 1 
print(d)            
"""

#Ques. You have a list [1,2,3,4,5] and you have a variable k = 2 and you just have to rotate the list by k elements.
"""
l = [1,2,3,4,5]
k = 2
for i in range(k):
    last=l[-1]   #Storing last value of the list

    for j in range(len(l)-1,0,-1):
        l[j] = l[j-1]
    l[0] = last
print(l)
"""




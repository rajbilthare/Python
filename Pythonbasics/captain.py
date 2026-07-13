#3-> 2 / 2 = 0   pair 
#2-> 4 / 2 = 0   pair
#every element is making an pair.
#no some elemnts are not making pair.

nums = [3,2,3,2,2,2]
d = {}
for i in nums: #i -> 3
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

#itni loop jissi mein i  ke andar sirf values aaye 
for i in d.values():
    if i % 2 != 0:
        print("not making pair")
        break
else :
        print("making pair")   


#factorial using recurrsion
#print prime  number within a range.       
   
            
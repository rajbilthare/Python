 #for i in 
#function is something  jiske baad apn parenthesis lagate hain

#range(s , s ,s)

#a = range(1,101,1)

"""for i in a:
    print(i)

b = range(50,121,1)

for i in b:
    print(i)

c = range(-10,31,1)

for i in c:
    print(i)


for i in range(2,-21,-1):
    print(i)


a = int(input("enter no"))  
for i in range(a,a * 10 + 1,a):
    print(i)  
    """

"""a = "raj is learning python"

for i in range(22):
    print(a[i])"""

#len function gives the length of the string

"""a = "raj is the pro coder"
print(len(a))

for i in range(len(a)): 
    print(a[i])
"""

"""a = "raj is so cool and handsome"

for i in a:
    print(i)
"""

"""for i in range(1,24):
    if i == 21:
        break         #it will break the loop when i is 21
    print(i)    """

"""for i in range(1,24):
    if i == 21:
        continue      #it will skip the iteration when i is 21 and continue with the next iteration
    print(i)    """

#when break dont executed it will execute the else block otherwise it will not execute the else block

"""for i in range(1,24):
    if i == 57:
        break
    print(i)    
else:
    print("break was not executed")    """

 #questions

"""n = int(input("enter a number")) 

for i in range(n):
    print("hello world")"""

"""n = int(input("enter a number"))    

for i in range(1,n+1):
    print(i)"""

"""n = int(input("enter a number"))    

for i in range(n,0,-1): 
    print(i)"""   

"""n = int(input("enter a number"))    

for i in range(n,n*10+1,n):
    print(i)"""

#sum up to n terms 

"""n = int(input("enter a number"))
sum = 0 

for i in range (1,n+1):
    sum = sum +i

print(f"your sum is {sum}") """

"""
n = int(input("enter a number"))
fact = 1 

for i in range (1,n+1):
    fact = fact * i

print(f"your factorial is {fact}")"""

"""n = int(input("enter a number"))
even = 0 
odd = 0

for i in range(1,n+1):
    if i%2 == 0:
        even = even + i
    else:
        odd = odd + i 

print(f"your even and odd sum are {even},{odd}")   """         

"""
n = int(input("enter a number"))
for i in range(1,n+1):
    if n%i == 0:
        print(i)"""

"""n = int(input("check your no is perfect or not"))
sum = 0 

for i in range(1, n):
    if n%i == 0:
        sum = sum + i
print(sum)

if sum == n:
    print("your no is perfect")
else:
    print("your no is not perfect")"""

"""n = int(input("check your no is prime or not"))
count = 0
for i in range(1,n+1):
    if n%i == 0:
        count = count + 1
if count == 2:
    print("your number is prime")
else:
    print("your number is not prime")            
"""
"""even =0
odd = 0
for i in range(1,51):
    if i%2==0:
        even += 1
    else:
        odd += 1  

print(even)
print(odd)          """


#s = "hello sherry"

"""count_vowels = 0
count_consonant = 0
for i in s:
    if i in "aeiouAEIOU":     #in is a membership operator that we use here
        count += 1
print(f"coount of vowels are: {count}" ) 
print(f"count of consonant  """     

"""for i in range(1,21):
    if i%3 ==0 or i%5 == 0:
        print(i)"""

#while loop 
"""a = 1

while a <= 20:
    print(a)
    a = a + 1 """

#by for loop
"""for i in range(1,21):
    print(i)"""


"""num = 2
sum = 0
for i in range(1,num+1): #i = 1,2,3,4,5,6,7,8,9,10
    if num % i == 0:
        sum += i
print(sum)        """
"""       count += 1
if count == 2:
    print("your number is prime")
else:
    print("your number is not prime")  """   

# ques print prime numbers for 1 to 50

"""for i in range(1,51):
    count = 0
    for j in range(1,i + 1):
        if i%j == 0:
            count += 1
    if count == 2:
        print(i)"""
             
 #find the sum of all the numbers from 1 to 100   
"""sum = 0
for i in range(1,101):
        sum += i        
print(sum)       """

#find the factorial of a number
"""n = int(input("enter a number"))
fact = 1

for i in range(1,n+1):
    fact *= i

print(f"your factorial is {fact}")"""

"""
for i in range(1,5):
    for j in range(i):
        print("*",end = "")
    print()"""


"""for i in range(4,0,-1):
    for j in range(i):
        print("*",end = "")
    print()
"""

"""
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end = "")
    print()"""


"""num = 1024
num2 = str(num)
for i in num2:
    print(i)"""

#while loop 

# how to print numbers from 1 to 10 using while loop
"""i =  0
while i < 11:
    print(i)
    i = i + 1  """


"""i =  0
while i < 11:
    if i == 5:
        break
    print(i)
    i = i + 1"""
     
"""sum = 0
num = 1054
while num > 0:
    last = num % 10
    sum = sum + last
    num =   num // 10   
print("num is ",num) 
print("sum is ", sum)"""

#how to seprate the digits of a number using while loop
"""num = int(input("enter a number"))   
while num > 0:
    print(num % 10)
    num = num // 10"""

# accept a number from user and reverse it using while loop

"""num = int(input("enter a number"))
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num = num // 10     
print("reverse is ", rev) """


#check whether a number is palindrome or not using while loop

"""num = int(input("enter a number"))
copy = num   # the reason of creating this copy because in the end the original no becomes 0 so then its not equal to the rev so we first save this by copy
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num = num // 10     
if copy == rev:
    print("your number is palindrome")
else:
    print("your number is not palindrome")""" 

#armstrong number or not using while loop
"""num = 153
power = len(str(num))  #3
copy = num
sum = 0
while num> 0:
    last =num % 10
    num = num // 10
    sum = sum + last ** power
if copy == sum:
    print(f"(copy) is an armstrong number")
else:
    print(f"(copy) is not an armstrong number")"""
    

     



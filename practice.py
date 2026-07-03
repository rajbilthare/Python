"""a = "B"
print(ord(a))
a = 24
print(chr(a))"""

"""if 9 > 10:
    print("15 is greater than 10")
else:
    print("15 is not greater than 10") """   


"""n = int(input("please tell your number"))

if n%2 == 0:
    print("the number is even")
else:
    print("the number is odd") """   


# how to seprate digits of a number by using for loop 
"""num1 = 1345
num2 = str(num1)
for i in num2:
    print(i)
"""

# lets try this by using while loop
"""num = 15677
while num>0:
    print(num%10)
    num = num//10"""

# create a random guessing game by using python 

"""import random

num = random.randint(1,11)

tries = 0

while True:
    guess = int(input("guess your number between 1 and 10  "))

    if guess == num :
         tries += 1
         print(f"you are right you guessed the number in {tries} tries")
         break

    elif num < guess:
        print("go a little lower")   
        tries += 1
    
    elif num > guess:
        print("go a little higher")     
        tries += 1
    
    else :
        tries += 1
        print("you are wrong")
        """

"""a = int(input("enter a number"))
for i in range(a,a*10+1,a):
    print(i)"""

"""n = 1024
sum = 0
while n > 0:
    last = n % 10
    sum = sum + last
    n = n // 10

print(f"Sum of digits: {sum}")"""

#practice basics questions


"""num = int(input("enter a number"))
if num > 0:
    print("the number is positive")
elif num < 0:
    print("the number is negative")
else:
    print("the number is zero")"""


"""num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num2} is greater than {num1}")
else:
    print("both are equal")   """     


"""num = int(input("enter a number"))
if num %2 == 0:
    print("the number is even")
else:
    print("the number is odd")"""

"""for i in range(1,51):
    if i % 2 == 0:
        print(i)"""


"""sum = 0
for i in range(5):
    num = int(input("enter a number"))
    sum = sum + num 
print(f"the sum is {sum}")"""

"""attempt = 0
while attempt < 3:
    pin = int (input("enter your pin"))
    if pin == 1234:
        print("access granted")
        break
    else:
        print("your card is blocked")
        attempt += 1"""
"""
s = "gdfjsfhjevfgewk"
count_vowels = 0
count_consonant = 0
for i in s:
    if i in "aeiouAEIOU":     #in is a membership operator that we use here
        count_vowels += 1
    else:
        count_consonant += 1    
print(f"coount of vowels are: {count_vowels}" ) 
print(f"count of  cocnsonants are: {count_consonant}"""


"""
for i in range(1,13):
    for j in range(i):
        print("raj", end = "")
    print()   """ 


"""n = 153
power = len(str(n))
sum = 0
copy = n 
while n > 0:
    last = n% 10
    n = n // 10
    sum = sum + last**power   
    if copy == sum:
        print("no is armstrong no ")
    else :
        print("not an armstrong no ")    """


#armstrong no

"""num = 153
power = len(str(num))
copy = num 
sum = 0
while num>0:
    last = num%10
    num =  num//10
    sum = sum + last**power
if copy == sum:
        print("its an armstrong no")
else:
        print("its not an armstrong no")   """ 


#sort the list in ascending order 

"""l = [1,2,344,55,5,5,6]

for i in range(len(l)):
    for j in range(len(l)-1):
        if l[j]>l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]
print(l)           """


#output - person jiske largest marks aa rhe hai. [dhanya]

"""marks = {'shivam':90,'abhishek':80,'kunal':70,'dhanya':95,'raj':75}

largest = 0  #95

for i in marks.values():
    if i > largest:
        largest = i

l = []        

for key, value in marks.items():
    if value == largest:
        l.append(key)

print(l)"""


marks = {'shivam':90,'abhishek':80,'kunal':70,'dhanya':95,'raj':75}

largest = 0  #95
s_largest = 0

for i in marks.values():
    if i > largest:
        s_largest = largest
        largest = i
    elif i > s_largest or i != largest:
        s_largest = i    

l = []        

for key, value in marks.items():
    if value == largest:
        l.append(key)
    if value == s_largest:
        l.append(key)    

print(l)


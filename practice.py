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


num = int(input("enter a number"))
if 





          
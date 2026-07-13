# function is a block of  reusable code which only runs when it is called. 
#types of function
#1. user defined function
#2. built in function

# how to create a user defined function

"""def hello():
    print("this is my first function")

hello() # we need to call the function"""


# parameters - the thing we accept in the function is called parameter
# argument - the thing we provide  in the function is called argument

"""def sum(a,b):
    print(f"the sum of the number is {a+b}")  # positional argument

sum(13,13)

def raj():
    print("raj is a all roundeer")

raj()  

def division(a,b):
    print(f'the division of the numbe is {a/b} ')

division(12,13)    """

"""def hello(name,age):
    print(f'hello {name} your age is {age}')

hello(name = "raj",age = 20) """ #keyword argument   


"""def hey(a,b=12):    # 12 is a default parameter 
    print(f'the sum is {a+b}')
   
hey(1,13)              """  ## 13 is the default argument


# return function
"""def learn():
    return "python is a fun language"

print(learn())"""


"""def fun():
    return 
print(fun())  # it will return none because we have not return anything in the function

def show():
    print("hello")"""

"""
def greet():
    return("hello")
def add():
    print(greet())
    a = 12
    b = 13
    return a+b
print(add())"""


"""def add(a,b): #function define krte waqt
    print(a+b)
add(10,20)    # function call krte waqt"""


# type hindting in function  
#syntax - (variable : type)

"""def add(a : int, b : int):
    print(a+b)
add(10,10)   """ 
"""       
def add(a : int, b : int):
    print(a+b)
add(True,False) """ # true ki default value 1 hoti hai and false ki 0




#default parameter 
"""def add(a,b=0):
    print(a+b)
add(10)    
add(10,20)"""


# accept an parameter named as 'n' and print factoriral of'n' using function 


"""def factorial(n:int):
   # n = int(input("enter a number"))
    fact = 1
    for i in range(1,n+1):
       fact *= i #shorthand operator
    return fact

print(factorial(5))"""

"""def even_odd(n):
 n = int(input("enter a number"))
 even = 0
 odd = 0
 for i in range(1,n+1):
    if i%2 == 0:
        even += 1 
    else :
        odd += 1
    return even_odd    

print(even_odd(12))
"""


#factorial using recursion 

"""def factorial(num):
    if num == 0 or num == 1:
        return 1 
    else :
        return num * factorial(num - 1)
    
print(factorial(5))  """



#lambda , args , kwargs  skip kra hai kyuki data structure nhi hua 

   

   
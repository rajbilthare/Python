# questions

"""name = " mohit"
print(name[::-1])
print(len(name))
print(name.upper())
print(name.lower())"""


"""name = "PyThon"
lower = ""
upper = ""
for i in name:
    if i.islower():
        lower = lower + i
    else :
        upper = upper + i
print(lower + upper) """           

# armstrong number is a number which is equal to the sum of the cube of its digit
# ques is num is armstrong or not
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


#no is perfect or not
"""num = 6
sum = 0
        
for i in range(1,num):
    if num % i == 0:
        sum = sum + i   
    
if sum == num :
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")   """     



#pattern printing
"""rows = 5
for i in range(1,rows+1):
    print("*" * i)"""







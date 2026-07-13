#random no guessing game 

"""import random

num = random.randint(1,10)

print(num)

tries = 0

while True:
   guess = int(input("guess your no between 1 to 10"))

   if num == guess:
        tries += 1
        print(f"you are right you guessed the number in {tries} tries")
        break
   elif num < guess:
        tries += 1
        print("go a little lower")
   elif num > guess:
        tries += 1 
        print("go a little higher")

   else:
        tries += 1
        print("you are wrong")         """   

#user have only 5 chances and if those chances are over either win or lose 

"""import random

num = random.randint(1,10)

chances = 5

while chances>0:
    guess = int(input("guess the no"))

    if num == guess:
        print("you win ")
        break
    else :
        chances -= 1
        print("wrong guess")
        print("chances left",chances)

if chances == 0:
    print("you lose")
    print("the correct number was",num)"""






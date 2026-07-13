# What is class? ->


#when you run your code you always initialize your class
# class only initailize one time

# class ka phela letter captial letter me likhna hai 




"""class Factory:
    print("Hello world.")


Factory()
Factory()
Factory()#-> This will not run your code inside class
Factory()"""

# class me attirubtes and methods create krte hai 
"""
class Animal :
    #attributes
    name = 'long_neck' #A variable defined inside a class is an attribute.
    #method -> function defined inside a class called method
    
    def speak():
        print("Hello i am a lion")


print(Animal().name) #calling an attribute

Animal.speak() #calling a method
"""
"""

#creating an object

class Animal:

    name = 'Bear'

    def speak():
        print("Bear is roaring.")
#This is how you create an object
obj = Animal()
obj2 = Animal()

#object has all the powers of its class 

print(obj.name) # objects can also attributes and methods
# print(obj.speak()) here we will send one argument by default
obj.speak()
print(obj2.name)
"""

#constructor function 

#whenever you call a class this function will run
"""class Bag_factory : #constructor called magic method in python
    def __init__(self): #self by default python create krke deta hai... 
        # self will capture the location of object or class itself
        print("How are you")
        print(self)

obj = Bag_factory()
Bag_factory()"""


"""class bag_factory:
    def __init__(self,material,zips,pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets
    def showdetails(self):
        print("material is ",self.material)
        print("zips are ",self.zips)
        print("pockets are ",self.pockets)



campus = bag_factory("leather", 3, 2) 
hrx = bag_factory("canvas", 2, 4)
campus.showdetails()       
hrx.showdetails()  """     








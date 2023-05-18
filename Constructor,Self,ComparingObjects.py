#__init__() method is called constructor
class Computer1:
    def __init__(self):
        self.name = "madhan"
        self.roll = 10

    def update(self):
        self.roll = 14
        #self is a pointer and it will be directed to c1 or c2 based on
        #what you are calling, as below we are calling update using c1
        #hence self refer to c1
    def compare(self,other):
        #compare(who is calling it,whom to compare)
        if self.roll == other.roll:
            return True
        else:
            return False
        #here c1 becomes self and other becomes c2
c1 = Computer1()#c1 is the object referring to class Computer
#c1 object will be created in heap memory
c2 = Computer1()
c2.roll=10
if c1.compare(c2):#compare is not an inbuilt method
    print("same roll")
else:
    print("diffeent roll")
#inorder to assign our own values to objects we have two ways
c1.name = "kumar"
c1.update()#updates roll
print(c2.roll)
print(c1.roll)
print(c2.name)
print(c1.name)
#size of object depends upon the size of the each variables and number of variables
#created in the class
#the constructor allocated required memory for the object in the heap memory
#when ever we write constructor it calls init method automatically so we no need
#to call explicitly
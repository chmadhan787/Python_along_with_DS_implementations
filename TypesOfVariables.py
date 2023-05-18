#in oops we have two types of variables
#one is instance variable and other is class or static variable
class Car:
    #if we define variable outside init and inside class they become class variables
    wheels = 4
    def __init__(self):
        #if we define variables inside init they become instance variables
        self.mil = 100#instance variable
        self.car = "BMW"#unstance varible
        #mil and car belongs to instance namespace and wheels belong to
        #class namespace
c1 = Car()
c2 = Car()
#we can change the value of instance variables using object
c1.mil = 80
#changing one object doesnt effect other object
Car.wheels = 5
#this will effect all the objects because wheels is shared between all the objs
#print(c1.car , c1.mil ,c1.wheels)
#since wheels are class variables we can access them with class name also
print(c1.car , c1.mil ,Car.wheels)
#print(c2.car , c2.mil ,c2.wheels)
print(c2.car , c2.mil ,Car.wheels)
#namespace is the area where we create and store object or variable
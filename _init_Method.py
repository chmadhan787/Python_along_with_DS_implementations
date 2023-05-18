class Computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu#self acts as an object here
        self.ram = ram
        print("in init")
        print()
#here we can initialize variables
#we can imagine it as a constructor
#this __init__ method will be called automatically when object is created

    def config(self):
        #as we have SpecialVariable __name__ similarly we have SpecialMethod
        #called __init__
        print("config is : ",self.cpu," and ",self.ram,"GB ram")
        print()

com1 = Computer('i5',16)
com2 = Computer('rysen 3',8)

com1.config()
com2.config()
#we can use del key word to delete objects
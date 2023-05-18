#object oriented programming in python
#python is functional programming(we can perform operations using functions,
# passing function to a function)
#object oriented programming
#procedure oriented programming(we can create different kinds of functions for
#different kinds of tasks ie we can divide a program into simple parts)
#in real world everything is object
#every object will have certain attributes(data,properties) and behaviour(talking,
# walking,dancing) actions defines our behaviour
#as an object it knows something and it does something which it knows
#an object will have something to store data and it will have some behaviour
#inorder to store something object we need to create variables
#in order to give behaviour we need to create methods
#functions in object oriented programming are called as methods
#in oops we will have object , class , polymorphism,abstraction,encapsulation,inheritance
#class is a design(blueprint) and object is an instance
class Computer:
    #here we can have attributes (variables)
    #behaviour (methods or functions)
    def config(self):
        print("i5 ,16gb ,1TB ")
        print()

com1 = Computer()#this constructor will create object for class Computer
com2 = Computer()

Computer.config(com1)#here we use class and object in order to call the func
Computer.config(com2)#normally this is done inside if we use com2.config()

com1.config()#here we use object itself to call the function
com2.config()#com1 or com2 will go as an object in the place of self
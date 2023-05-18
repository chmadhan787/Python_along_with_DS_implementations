#OOPs
#1>Inheritance
#2>Polymorphism
#3>Abstraction
#4>Encapsulation
#INHERITANCE
# when one object acquires the properties and behaviours of parent object, is known as inheritance.it helps for
# code re-usability.it is used to achieve runtime polymorphism
# using inheritance we can create class which uses all properties and behaviour of another class and the
# class which uses all properties is called as derived or child or subclass and the class from which derived
# is called base or parent class.
#1.Single level inheritence:
class Animal:
    def speak(self):
        print("Animal speaking")
class Dog(Animal):
    def bark(self):
        print("Dog barking")
# d = Dog()
# d.speak()
# d.bark()
#
#2.multilevel inheritance:
class DogChild(Dog):
    def eat(self):
        print("DogChild eating bread")
d=DogChild()
d.speak()
d.bark()
d.eat()
#
#3.multiple inheritance:
class Human:
    def speak1(self):
        print("human is talking")
class Multiple(Human,Animal):
    pass
m = Multiple()
m.speak()
m.speak1()
#
#4.Heirarchical inheritance
class Cat(Animal):
    def speak2(self):
        print("cat says meow")
c = Cat()
c.speak()
c.speak2()
#
#Hybrid inheritance:
class Hybrid(Dog,Cat):
    def hybrid(self):
        print("hybrid inherited")
h = Hybrid()
h.speak()
h.bark()
h.speak2()
h.hybrid()
#
# POLYMORPHISM
# "poly" means "many" and "morph" means "shapes".
# if one task is performed in different ways we say it as polymorphism.that means we use same method name or
# sometimes even same parameter for two methods with different functionality.
#=>in java we use method overriding and method overloading to achieve polymorphism.
# for ex-ample you have a class animal and all animals speak differently, here in animal class for same speak
# method we may have different kinds of sound for different animals.
#
#1.Method Overloading: defining a method in child class which already defined in the parnt class and with
# defferent parameters is called method overloading.
class Poly:
    def add(self):
        print("it is a method which adds two numbers.")
class ChildPloy(Poly):
    #method overloading
    def add(self,a,b):
        self.a = a
        self.b = b
        print(self.a +self.b)
ol = ChildPloy()
ol.add(1,3)#we can access only the method used to overload the parent class method
ol.add(2,3)
#
#2.Method Overriding:defining a method in child class which is already defined in the main class and with
#same parameters.
class Mor:
    def add(self,a,b):
        self.a = a
        self.b = b
        print(self.a+self.b)
class ChildMor(Mor):
    #overrided method
    def add(self,a,b):
        self.a = a
        self.b = b
        print(self.a*self.b)
mr = ChildMor()
mr.add(2,3)#we can access only the method used to override the parent class method
#
# ABSTRACTION
# data abstraction is achieved through encapsulation.
# Hiding internal(implementation) details and showing functionality is known as abstraction.
# =>in java we use interface and abstract classes to achieve abstraction.
# Abstracting something means that we give names to things such that by knowing that name itself we can judge
# functionality of that thing and what the program does.
#
#ABC module is used to acheive abstract classes and ABC means
#abstract base classes
from abc import ABC, abstractmethod
class Computer:
    @abstractmethod
    def process(self):
        pass
class WhiteBoard(Computer):
    def write(self,obj):
        print('its writing')
        obj.process()

class Laptop(Computer):
    def process(self):
        print('its running')

class Programmer:
    def work(self,com):
        print('solving bugs')
        com.process()

lap = Laptop()
#lap.process()
prog = Programmer()
prog.work(lap)
wh = WhiteBoard()
wh.write(lap)

#a class which have abstract methods are known as abstract classes
#python by default doesnt support abstract classes
#for creating abstract classes we need to import abc module
#we cannot create object for abstract classes

# ENCAPSULATION
# Binding(or wrapping) code and data together into a single unit is called as encapsulation.
# java class is an example of encapsulation, java bean is a fully encapsulated class because all the data
# members are private here.
# it is used to restrict access to internal methods and variables of a class,so that nobody can modify the
# functionality of code or code is not disturbed by an accident.
# data abstraction and encapsulation are often used as synonyms.

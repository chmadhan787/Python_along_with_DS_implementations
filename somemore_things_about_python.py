#in python every variable is an object.
#in declaring strings making use of double quotes makes easy to use
# apostrophes in the string
# python supports multiple assignments in a single line
# concatenation in between two different types is not possible
# in order to check that some object is of specified type then we need
# to use isinstance() function ,it returns true if the given object is
# of required type.
print(isinstance(5,int))
print(isinstance(5.0,float))
#remember that in python every floating point number is defaultly taken
# as a double number.
print(isinstance('m',str))
#same as strings python also supports creating new lists with a
# repeated sequence using multiplication operator.
#list methods and functions
l = [1,2,3,5,4,6,7,8]
l.append(9)#1
print(l.pop())#2 we can mention index in the pop()
l.remove(8)#3
l.insert(3,9)#4
print(l.count(1))#5
print(l.index(9))#6
t = l.sort()#7
print(t)
l1 = [0]
e = l.extend(l1)#8
print(e)
print(sum(l))#9
print(sorted(l))#10
print(any(l))#11
print(all(l))#12
print(min(l))#13
print(max(l))#14
print(len(l))#15
print(l[::-1])#[start:stop:step] 16
x=l.reverse()#17
print(x)
print(list(reversed(l)))#18
#string formatting
name = 'madhan'
number = 1
print("%s and %d are my details" % (name,number))
#any object which is not string van be formatted using the %s operator
# well.
l = [1,2,3,4]
print("a list: %s" % l)
# %x is used for hexadecimal representation (capital and small)
n = 2
print("%.2f" % n)#we can specify number of zeros in floating point numbr
#strings
s = 'String'
print(s[0])#1
print(s[1])
print(s.index('S'))#2
print(s[::-1])#3
print(s[2:4])#4
print(s.upper())#5
print(s.lower())#6
print(s.count('t',1,4))#7
print(s.split())#8
print(s.startswith('t',1,4))#9
print(s.endswith('g'))#10
print(s.rjust(10,"-"))#11
print(s.ljust(10,"-"))#12
print(s.center(10,"-"))#13
print(s.replace('g','G'))#14
print(s.isupper())#15
print(s.islower())#16
print(s.capitalize())#17
print("-".join(s))#18
#upper case letters and spaces have more priority
print(sorted(s))#19
print(s.isalpha())#20
print(s.isalnum())#21
print(s.isdigit())#22
print(s.isascii())#23
print(reversed(s))#24
print(ord('a'))#25 used to convert alphabet to ascii
print(chr(97))#26 used to convert ascii to alphabet
#python uses boolean values to evaluate conditions and it returns boolean values true and false based on the
#condition
x=2
print(x==2)
print(x==3)
print(x<3)
#and & or boolean operators are used to build complex boolean expressions
name = "john"
age = 23
if name == "john" and age == 23:
    print("your name is john and you are 23 yrs old")

if name == "john" or name == "rick":
    print("your name is either john or rick")
#in operator is used to check whether a specified operator is there in an iterable object container
if name in ["john","rick"]:
    print("your name is either john or rick")
#== matches values but is (return true if variables reference the same object) operator matches the
# instances themselves
x=[1,2,3]
y = [1,2,3]
print(x==y)
print(x is y)
#for mutable objects python doesnt reuses the existing objects but creates another one
x = 100
y = 100
print(x is y)
# in case of immutable objects the python reuses the existing objects with same values
#is not operator works opposite to is operator

#for loop can iterate over a range of numbers using range or xrange functions, difference between range
# and xrange is that the range return new list with numbers of that specified range where xrange returns
# an iterator which is more efficient, in python 3 range itself works as xrange function
#for loop is better to use when number of iterations are known
#while loop is better to use when number of iteration are unknown
#break is used to exit loops and continue is used to skip current iteration and goes again to for or while loop
#pass is used is there are empty blocks
#we can use else with both of the loops and it executed when the condition given at loops resolves to be false
#else will not be executed if the loops are terminated using break statement

#Functions are a convenient way to divide your code into useful blocks, allowing us to order our code, make it more
# readable, reuse it and save some time. Also functions are a key way to define interfaces so programmers can
# share their code.We use def key word to define functions
def my_function():
    print("here is my function")
my_function()
def my_function_with_args(username,age):
    print("%s and %d are my details" %(username,age))
    return username,age
result = my_function_with_args("madhan",21)#scince multiple values are returned to a single variable it form
# a tuple with returned values
print(result)
def var_le(*a):
    for i in a:
        print(i)
    return
var_le(1,2,3,4)

#classes and objects
#objects are the encapsulation(warapping up of data in to a single unit) of variables and functions in
# a single entity . objects get their variables and functions from the classes
#class is a template to create objects
#we can delete a object using del keyword.

class Myclass:
    variable1 = "blah"
    def function(self):
        print("this is a message inside the class")

myobjectx = Myclass()#assigning Myclass template to myobjectx, now the myobjectx holds the object of Myclass
# which contains variables and functions defined in Myclass
myobjectx.function()#accessing function inside the class using created object
print(myobjectx.variable1)#accessing variable inside Myclass

# you can create multiple different objects of same class having same variables and methods.but each object
#contains independent copies of variables define in class.for ex, if i create another object of Myclass and change
# string in the variable:
myobjecty = Myclass()
myobjecty.variable1 = "blah blah"#we can modify the value of variable of class by accesssing it to outside the
# class using class's object
print(myobjecty.variable1)

#init()-it can be treated as a constructor of a python class
#init() function is the special function that is called when ever the class is initiated.it is used to
#assign values inside a class
#we can pass parameters to a class.++-

# class NumberHolder(object):
class NumberHolder:
    def __init__(self,number):
        self.number = number

obj = NumberHolder(10)
print(obj.number)

#iter() : returns iterator object
#iter() function is used to convert an iterable(such as list,tuple,string) to an iterator
#syntax: iter(obj,sentinel) where obj is the iterable that need to be converted to iterator and sentenal is
#used to represent the end of the sequence
#iteration object remembers iteration count via internal count variable
#once the iteration is completed then it raises the stopiteration exception and the iteration count cannot be
#reassigned to 0
#therefore it is used to traverse the container just once
lst = [1,2,3,4,5]
print("the list is of type : ",str(type(lst)))
lst = iter(lst)
print("the list is of type : ",str(type(lst)))
print(next(lst))#next() function is used to print the iterator values
print(next(lst))
print(next(lst))
print(next(lst))
print(next(lst))

#tuple:
tup = (1,2,4,3,5)
print(len(tup))#1
print(sorted(tup))#2
print(sum(tup))#3
print(tup.index(3))#4
print(tup.count(2))#5
print(min(tup))#6
print(max(tup))#7
print(reversed(tup))#8
print(any(tup))#9
print(all(tup))#10

#Dictionary
# dictionary datatype is similar to arrays but works with keys and values instead of indexes
# each value in the dictionary can be accessed using keys, which is any kind of datatype instead of using its
# index to address it
# a dictionary can be initialised as.
dic = {}
dic['m'] = 1
dic['a'] = 2
dic['d'] = 3
print(dic)
#or
dic = {
    'h':4,
    'a':5,
    'n':6
}
print(dic)
#dictinaries can be iterated same as lists but as dictionaries use key value pairs use below syntax to iterate
# over a dictionary.
for letter,number in dic.items():
    print('%s %d'%(letter,number))

# for removing a value :
del dic['h']
print(dic)
#or
dic.pop('a')#1
print(dic)
#if you print an element that doesnt present in the dictionary then it will give an error, so to avoid error
# we use get method available in dictionaries as.
# print(dict['h'])#this gives an error as 'h' is not in the dictionary
print(dic.get('h'))#2#this returns None if the element is not present in the dictionary
#to return a desired thing u can mention it as a second parameter in the get method
print(dic.get('h','not found'))#2.1

#we can use zip() function to form a dictionary form two sets / lists /tuples, it works even if the lengths
#are different but it form a dict length that is the lowest of given two itrerables

keys = {1,2,3,4}
values = {'m','a','d','h'}
d = dict(zip(keys,values))#3
print(d)
#you can store multiple values for a single key
print(*d.values())#4
print(*d.keys())#5
print(d.items())#6
# print(d.clear())# this removes all elements from the dictionary
#copy() returns a copy of dictionary
t = d.copy()#7
s = {'m': 1,'a': 2,'d': 3}
#for unpacking of a dictionary using asterisks(the keys must strings)
s1 = {**s,'h': 4}#8
print(s1)

#unpacking dictionary keys to tuples
print(tuple(s1))#9
print(list(s1))

#traversing through dictionary
for i in s1:
    print(i,':',s1[i])

#fromkeys() method is used to assign value to elements in given iterable or keys
x = ("key1",'key2','key3')
y = 0
print(dict.fromkeys(x,y))#10
#here x is an iterable specifying the keys of a new dictionary

#as pop() removes element with specified key
#popitem() will remove the last inserted key value pair in the dictionary
print(s1.popitem())#11
print(s1)

# to print unpacked keys of a dictionary
print(*s1)#12

#setdefault() : this method is used to return the value of item with specified key ,if the value not present in
# the dictionary then inserts the key with specified value
print(s1.setdefault('h',4))#13#scince the specified key is not present in the list it inserts 'h':4 as a key value
# pair to the end of the dictionary
print(s1)

#update() updates dictionary with specified key value pairs
s1.update({'n':5})#14
print(s1) 
#we can merge two dictinaries using update method and the result will be stored in the first dictionaru which
#used to call that update method
s2 = {'m':6,'c':7,'e':8}
s1.update(s2)
print(s1)#if there is same key present then it updates value of that key with new value of adding list
#to know which functions are used in the imported module you can use dir function
# import urllib
# print(dir(urllib))
#name spaces in python:
# name space is a system that has a name for each and every object in python.
# that object might be a variable or a method.
# python itself maintain a namespace in the form of dictionary
# lets take an example of directory-file system . we know that there can be multiple files of same name
# but they should be  in different directory,and those files with same name without error can be accessed
# by specifying path along with directory of the file
# when coming to real life example if a file consists of students with same name then they can be differentiated
# using their surnames
# python name spaces uses same type of concept to differentiate objects
# in Namespace : Name (which means name,a unique identifier) + space (which talks something related to scope,
# this scope is about the scope of object in python program)
# here the name might be of any python method or variable and space depends on the location from where is trying
# to access method or variable
#
# types of name spaces:
# 1.built-in name spaces
# 2.global name spaces
# 3.local name spaces
# when python interpreter solely without any user defined modules,methods,classes etc.some functions like
# print(),id(),are always present,these are built-in namespaces when a user himself creates a module then
# a global name space is created, later the creation of local function will create a local namespace
# always Built-in namespaces encompasses the global namespaces and these global namespaces encompasses the
# local namespaces
# remember that the life time of name spaces depends on the life of the object.
#
#ByteArray : gives the mutable sequence of integers in range 0 to 256
a = bytearray((12,8,25,2))
a[2] = 3# since it is mutable we can modify the values of the array
print(a)
#
#ARRAYS in python:
# we can implement arrays in python using two modules one is array module and another is numpy module
# arrays in python are not of fixed size
# 1.USING ARRAY MODULE:
import array
vals_signed = array.array('i',[1,2,-3,4,-5])
print(vals_signed,":'i' is used to create array which supports signed and unsigned numbers.")
vals_unsigned = array.array('I',[1,2,3,4,5])
print(vals_unsigned,":'I' is used to create array with only positive or unsigned numbers.")
print(vals_unsigned.buffer_info())#this method returns the address and size of the array mentioned
vals_unsigned.reverse()#used to reverse the given array
print(vals_unsigned)
#always remember that if the methods are used inside print then it will only returns None so first apply the
# method and then print it
# for characters use character.
char_array = array.array('u',['a','b','c','d'])#similarly 'U' is used to create array with Uppercase letters
print(char_array)
#to copy the datatype from another array
new_arr = array.array(vals_unsigned.typecode,(t*t for t in vals_unsigned))
print(new_arr)

#2.USING NUMPY MODULE :
# numpy arrays are great alternatives to python lists
#some of the key advantages of numpy arrays are
# 1.they are fast when compared to arrays in array module and lists
# 2.they are easy to implement and use
# 3.it gives the users an opportunity to perform calculations over an entire array
# we can create single and multidimensional arrays using numpy in python
# syntax : array([values],datatypes) here the datatypes are optional
# there are six ways to create array using numpy
# 1.array()
# 2.linspace()
# 3.logspace()
# 4.arange()
# 5.ones()
# 6.zeros().
from numpy import*
arr = array([1,2,3,4],int)
print(arr)
print('type of values in arr : ',arr.dtype)
arr1 = array([1.0,2.1,3.2])
print('type of values in the arr1 : ',arr1.dtype)
#using linespace(start,stop,step) here step is optional
arr2 = linspace(0,15,16)#here 15 is also included unlike range() function
#0-15 is divided into 16 parts i.e step decides the no. of parts that the range is to be divided
#difference will be constant unlike logspace , if we dont mention the step then it takes 50 as default value.
print(arr2)
#logspace() : syntax is same as linspace() but here the spaces(difference) between the elements depends on the
# log values of the elements.
l = logspace(1,40,5)#it starts from 10 raise to 1 and goes till 10 raise to 40
print(l)
for i in range(len(l)):
    print('%.2f'%(l[i]),end = ' ')
print()
#arrange() : syntax is same as linspace :
a = arange(1,15,2)#this is similar to range function but returns a list
print(a)
#we can print odd numbers using numpy as
print(*arange(1,20,2))

#zeros(size,datatype) : creates an array with given size and all the default values will be zeros
# and default data type is float hence datatype is optional
z = zeros(5,int)
print(z)
# ones() : this works similar to zeros() but default values are ones
o = ones(5)
print(o)

#pandas module basics:
#=> pandas data frames :
# pandas is a high-level data manipulation tool developed by Wes McKinney
# it is built upon numpy module and its key data structure is Dataframe. DataFrames allow you to store data and
# manipulate tabular data in rows of observations and columns of variables
# there are several ways to create data frames and one way is usign dictionary,
dic = {
    'country':['Brazil','Russia','India','China','South Africa'],
    'capital':['Brasilia','moscow','New delhi','Beijing','pretoria'],
    'area':[8.975,9.765,6.345,7.897,8.898],
    'population':[200.4,143.6,345.5,342.5,234.5]
}
import pandas as pd
brics = pd.DataFrame(dic)
print(brics)
#it automatically assigns numerical indeces even if not mentioned in the dictionary
#to assign used desired keys :
brics.index = ['BR','RU','IN','CH','SA']
print(brics)
#another way to create dataframe is by importing csv file using pandas
#easiest way for indexing a dataframe is by using square brackets

#Generators :
#for working with generators you should know the yield keyword and iterators
#yield statement suspends a functions execution and sends the value back to the caller but it retains the
# enough state to resume the function from where it left off and when the function resumes it starts execution from
# immediately after the last yield run ,this allows the code to produce a series of values over time instead
# of computing them at once and sending them back like a list, for example:.
def simpleGeneratorFunction():
    yield 1
    yield 2
    yield 3

for value in simpleGeneratorFunction():
    print(value)

#RETURN send a specified value back to its caller but YIELD can produce a sequence of values
# WE should use yield when we want to iterate over a sequence but don't want to store entire sequence in
# the memory.
#YIELD is used in pyhton generators. A generator function can be declared as a normal function but whenever it
# needs to generate a value , it does so using yield keyword rather than return keyword.
#if the body of the funtion contains yield keyword then that function automatically becomes a generator function.
#Generator Function example
def nextSquare():
    i = 1
    while True:
        yield i*i
        i+=1

for num in nextSquare():
    if num == 100:
        break
    print(num)

#Generators :
#there are two terms involved when we talk about generators:
# 1.Generator Function:
# a generator function is a normal function, but when ever it needs to generate a value, it used yield keyword
# rather than return. if the body of a function contain yield then that function automatically becomes a generator
# function for example see above code with yield keyword
#
# Generator Object:
# generator Function returns a generator object.generator objects are used either by calling next method on
# generator object or by using for in loop.
#EX
def simpleGen():
    yield 1
    yield 2
    yield 3

xx = simpleGen()
# print(xx.next())
# print(xx.next())
# print(xx.next())

#so we can say we can say that a generator return an object which is iterable i.e it can be used as an iterator
def fib(limit):
    a,b = 0,1
    while a<limit:
        yield a
        # c = a+b
        # a = b
        # b = c
        a,b = b,a+b
# y = fib(5)
# print(y.next())
# print(y.next())
# print(y.next())
# print(y.next())
# print(y.next())
print('using for in loop :')
for i in fib(10):
    print(i)

#List Comprehensions:
# list comprehension is a very powerful tool , which creates a list from another,in a single, readable line
# for Example lets say we need to create a list of lengths of words of a sentence but it should not be equal
# to word 'the'.
sentence = 'the quick brown fox jumps over the lazy dog'
words = sentence.split()
lengths = [len(word) for word in words if word!='the']
print(words)
print(lengths)

#lists can be directly created as :
#for list of even numbers :
even = [i for i in range(10) if i%2==0]
print(even)
#for list of squares :
squares = [i*i for i in range(10)]
print(squares)

#Anonymous or Lambda functions :
# anonymous function means a function without name and we normal functions are defined using def keyword but
#anonymous functions are defined using lambda keyword
# for normal functions we define the function somewhere and call it whenever required but in case of lambda
# functions we declare them in the place where we use them
# so, we don't need to revisit the code when ever required , which is the case of normal functions.
#below are some Instances of lambda functions :
a,b = 1,2
sum = lambda x,y:x+y#x,y are the parameter or formal parameters which accepts values from the arguments or
#parameters
print(sum(a,b))#a,b are the arguments or actual parameters
#lly
for i in range(10):
    s = lambda i : i*i
    print(s(i),end= '-')
print()
#Multiple Function arguments :
#every function in python receives a predefined number if arguments when declared normally but is also
# possible to declare a function which accepts predefined number of arguments using following syntax :.
def multi_args(first,second,third,*therest):
    #in this function therest parameters accepts variable length arguments hence it is called variable
    #arguments
    print("first : %s"%(first))
    print("second : %s"%(second))
    print("third : %s"%(third))
    print("the rest are : %s"%list(therest))
multi_args(1,2,3,4,5,6,7)

# it is also possible to send function arguments by keywords, so that the order of arguments doesn't matter
def bar(first,second,third,**options):
    if options.get('action')=='sum':
        print('sum is %d.'%(first + second + third))
    if options.get('number')=='first':
        print('first : %d'%first)
bar(1,2,3,action = 'sum',number = 'first')
#types of arguments in python :
# 1.positional arguments
# 2.keyword arguments
# 3.default arguments.
# 5.variable length arguments.
#ex
def args(a,b=2,*c):
    #there will be tuple formed in 'c' using the extra arguments which are more than the number of parameters.
    sum = a+b
    print(sum)
    print(c)
args(3,4,5,6,7)#these are arguments
#args function the arguments 3 passed to a is called positional arguments because the first argument
#in the call must be passed to first parameter in the definition.
#in positional arguments the order of arguments and parameters are considered and important
#in args b can be a default argument because even if we don't pass any value to b then 2 will be taken
#as a default value to it
#c can store variable length arguments passed from the call of function and stored in the form of a tuple
def args1(a,b):
    sum = a+b
    print(sum)
args1(b=3,a=9)
#as we assign parameters as keywords to values those values will surely fit in the parameters matching with
#those keywords hence the order is not important if we use keyword arguments

#REGULAR EXPRESSIONS :
#regular expressions are a tool for matching patterns in text, to implement this in python we have re module

#EXCEPTION HANDLING:
#errors are problems in a progrom due to which the program will stop its execution, on the other hand
#exceptions are raised when some internal eventsoccur which change the normal flow of a program
#there are two types of errors occur in python:
#1.syntactical errors
#when proper syntax is not followed a syntactical error is thrown
#2.logical errors
#the error occurs at the run time after passing syntax test is called logical or exception type.
#there logical error leads to exceptions
#ex. div by zero and if imported module doesnt exist
#some  common builtin exceptions :
#1.IndexError - when wrong index of a list is retrieved
# 2.AssertionError - it occurs when the assert statement fails
# 3.AttributeError - it occurs when attribute assignment is failed
# 4.ImportError - it occurs when an imported module is not found
# 5.KeyError - it occurs when key of a dictionary is not found
# 6.NameError - it occurs when the variable is not defined
# 7.MemoryError - it occurs when a program runs out of memory
# TypeError - it occurs when a function and operation applied in an incorrect type.
#we Handle these errors and exceptions using error or exception handling methods
#Handling exceptions using try/except/finally:
#we can handle errors by above mentioned methods .we write unsafe code in try block and fall back code in
#except and final code in finally block.
#For exmample:
try:
    print('code start :')
    print(1/0)
except:
    print('exception is raised')
finally:
    print('finally block is executed')

#Raising exceptions for predefined conditions :
#when we want to code for limitation of certain conditions then we can raise exceptions.
try :
    l = [1,2,3,4]
    index = 4
    # print(l[4])
    if index > 3 :
        raise IndexError('index out of bounds...')

except IndexError as e:
    print(e)

#SETS in python : a set of an unordered collection datatypes that is iterable ,mutable and have no duplicate
#elements, set id defined in {}.
#major advantages of sets when compared to list is that it has optimized method for checking whether a specific
#element is present in the set.
#this based on data structure known as hash table. scince sets are unordered we cannot access elements using
#indeces as we do in the list.
se = {'m','a','d'}
print(type(se))
print(se)
se.add('h')
print(se)
#python Frozen sets:
#frozen sets in python are immutable object that only support methods and operators that produces a result
#without affecting frozen set or sets to which they are applied . this can be done with frozen set method
#in python.
#while elements of set can be modified at any time , elements of frozen set remain the same after creating.
#if no parameters are passed, it returns an empty frozen set.
normal_set = set(['a','b','c'])
print(normal_set)
frozen_set = frozenset(['e','f','g'])
print(frozen_set)

#Methods for sets :
#Adding elements :
#insertion in a set is done using set.add() function, where an appropriate record value is created to store
# in the hash table. avg case time complexity is O(1) and worst case time complexity is O(n).
normal_set.add('d')
print(normal_set)

#UNION : two sets can be merged using union() function or | operator. both the hash table values are accessed
#and traversed with merge operation perform on them to combine the elements, at the same time the duplicates
#are removed . time complexity of this is O(len(s1) + len(s2)) where s1 and s2 are two sets whose union is to
#be done.
overall_set = normal_set.union(frozen_set)
# overall_set = normal_set | frozen_set
print(overall_set)

#intesection : this can be done through intersection() or & operator. Common elements are selected.they are
# iteration over hash lists and combining the same values on the table .Complexity of this is
# O(min(len(s1),len(s2))) ,where s1 and s2 are two sets whose union needs to be done.
set1 = {1,2,3,4,4}
set2 = {3,4,5,6}
print(set1.intersection(set2))
print(set1&set2)

#Difference betweem sets : finding difference between sets is similar to finding difference between linked lists
#this is done through difference or - operator . time complexity of finding difference between s1 and s2 is
#O(len(s1)
print(set1 - set2)
print(set1.difference(set2))

#clearing sets : clear() empties the whole set
set1.clear()
print(set1)
#disadvantages of sets:
#1.it doesnt maintain the order of elements in any particular order.
#2.only instances of immutable types can be added to set

#Operators that can be used on sets :
# 1.key in s - containment check
# 2.key not in s - non - containment check
# 3.s1 == s2 - s1 is equivalent to s2
# 4.s1 != s2 - s1 is not equivalent to s2
# 5.s1 <= s2 - s1 is subset of s2
# 6.s1 < s2 - s1 is proper subset of s2
# 7.s1 >= s2 - s1 ia super set of s2
# 8.s1 > s2 - s1 is proper superset of s2
# 9.s1^s2 - the set of elements are precisely in s1 or s2.

#Decorators in python : Decorators in python are very powerful and usefultool in python because it allows
# programmers to modify the behaviour of functions or class. Decorators help us to wrap another function in
# order to extend the behaviour of the wrapper function , without permanently modifying it
# Before knowing about decorators we need to know about
# 1. First Class Objects : first class objects in python are handled uniformly throughout .they may be stored
# in data structures , passes as arguments, or used in control structures .a programming language supports
# first class functions if it treats functions as first class objects . python supports the first class funcs
# Properties of first class function :
# 1.a function is an instance of object type
# 2.you can store a function in a variable
# 3.you pass a function as a parameter to another function
# 4.you can return the function from a function
# 5.you can store them in data structures like hash tables,lists ....
#in python functions are first class objects which means that functions can be used or passes as arguments
# after understanding the properties of first class objects now we can learn decorators
# Decorators : as stated above the decorators are used to modify the behaviour of function or a class
# in Decorators, functions are taken as argument in to another function and then called inside the wrapper
# function.
#this is also called metaprogramming because a part of program modifies another part of program at compiletime.
#Ex
# @smart_div
def div(a,b):
    print(a/b)

def smart_div(func):#here smart div acts as a decorator for div function

    def inner(a,b):#inner functions should have same number of parameters as div has
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner

div_new = smart_div(div)
div_new(2,4)

#MAP ,FILTER and REDUCE :
#these three functions allow you to apply a function across a number of iterables.
#MAP :
# syntax = map(func,*iterables) , note there is an asterisk(*) that means we can apply as many iterables
# map function returns a map object and we need to use list() function to convert that object into a list
# number of arguments to func must be the number of iterables listed.
my_pets = ['cat','dog','pig','buffallo']
uppered = list(map(str.upper,my_pets))

print(uppered)

#round() - takes two arguments - the number to round up and number of decimal places to round up
circle_areas = [3.43454,5.5234,6.324354,7.3245635,1.2334532]
rounded = list(map(round,circle_areas,range(1,6)))
print(rounded)

#zip() - it is function which accepts number of iterables and then create a tuple containind each of the
#elements in the iterables like map it also returns a generator which can be easily converted to list
# function on it.
names = ['madhan','sameer','harshith','fardeen','rohit']
rolls = [1,2,3,4,5]
l = list(zip(names,rolls,ones(5)))
print(l)
t = list(map(lambda x,y :(x,y),names,rolls))
print(t)

#FILTER:
# while map() passes each element of iterable through a function and returns the result of all elements
# having passed through the function, filter(), first of all requires the function to return boolean values
# and the pass each element of iterable through a function 'filtering' away those that are false
# syntax : filter(func,iterable)
# the following points are to be noted while using filter function:
# 1.unlike map only one iterable is required
# 2.func argument is required to return a boolean type. if it doest , then filter just returns the iterable
# passed to it ,also as only one iterable is required ,func must take only one argument
# 3.filter passes each element in the iterable through func and returns only that evaluates to be true.
t = [1,2,3,4,5,6,7,8,9]
k = filter(lambda x:x%2==0,t)
print(list(k))

#REDUCE : reduce applies a function of two arguments cumulatively to elements of an iterable optionally
#starting with an initial argument
# syntax : reduce(func,iterable,initial) , initial is optional and serves as default when iterable is empty
# the following things to be noted about reduce :
# 1.func requires two arguments , the first of which is first element in the iterable, if initial is not
# supplied and the second element in iterable , if initial is supplied
# 2.reduce , reduces iterable to a single value.
from functools import  reduce
n = [32,2,42,4,3,5,5]
def custom_sum(first,second):
    return first + second

result = reduce(custom_sum,n)
print(result)

print(reduce(lambda a,b : a+b,n))
print(reduce(lambda a,b : a+b,n,10))#takes initial sum as 10 then adds remaining from them

#enumerate is used to keep tract of count of items in the iterables
l = [1,2,3,4,5]
print(list(enumerate(l)))
for i,j in enumerate(l):
    print([i,j])

#pickling : it is a process of converting python objects to byte stream and dumps into
# a file by using dump function this process is called pickling
# unpickling : inverse of pickling.
#some popular python libraries:
#1.pandas:it is used to easily work with structures.
#2.Numpy:used to work with advance math functions.
#3.scipy:it has number of user friendly and efficient numerical routines.
#4.pillow:used for woking with imagers.
#5.pywin32:used for interaction with windows.
#6.pythontwisted:used to allow thread programming in order eventually answer the requests .
#7.nose:used to make testing easier.
#8.flask:it is a web framework used to develop web applications easily.
#9.fabric:used to execute shell commands remotely using SSH,yeilding useful python objects in return.
#10.pygame:it provides an extremely easy interface to the sdl(simple direct media library.
#11.request:it is to make http requests in python.
#12.pygtk:used for creating programs with gui.
#13.sympy:it is an open source library for symbolic math.
#14.matplotlib:it helps for data analyzing
#15.pypython:using it we can develop,debug,execute,monitor parallel applications.
#16.pyglet:provides an oops ,interfacing and developing games and visual rich applications.

#OOPs in python :
#class is a collection of objects or it is a blue print or prototy*-+
# pe followed by objects
# it a logical entity that contains some attributes and methods
# classes are created using keyword  class
# attributes are the variables that belong to class
# attributes are always public and can be accessed using the dot(.) operator.
#
# an Object is an entity that has a state and behaviour associated with it
# state means an attribute of an object and it also reflects the properties of object
# behaviour is represented by methods of an object and it also reflects to the response of the object to the
# other objects
# identity gives the unique name to the object  and enables one object to interact with other objects
#
# The self:
# self is a kind of pointer which points to the current object of class which is trying to access methods
# inside that object's class.
#if we have method with no arguments then we still have one argument.
# this is similar to pointers in c++ and this keyword in java
#
# The init method:
# it is similar to constructors in c++ and java and it runs as soo as the object is instantiated
# this is method is used to do any initialization you want to do with your object
#
#iNHERITANCE :
# inheritance is the capability of one class to derive or inherit the propertiies from another class
# the class that derives properties is called derived or child class and the class from which the properties
# are derived is called base class or parent class
# -- it represents real-world relationships well
# -- it provides reusability of code
# -- it is transitive in nature ie if class b inherits a then all subclasses of b will automatically inherit a

# SINGLE LEVEL INHERITANCE
# single level inheritance enables a derived class  to inherit characteristics from a single parent class
#
# MULTI LEVEL INHERITANCE
# multi level inhritance enables a derived class to inherit properties from its immediate parent class and
# and in turn inherits properties from its parent class
#
# HIERARCHICAL INHERITANCE
# hierarchical inheritance enables multiple derived classes to inherit from a single base class
#
# MULTIPLE INHERITANCE
# multiple inheritance enables a single derived class to inherit from multiple base classes
#
# EXAMPLE .
class person:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def display(self):
        print(self.name)
        print(self.id)

    def details(self):
        print("my name is {}".format(self.name))
        print("my id is %d"%(self.id))

class Employee(person):
    def __init__(self,name,id,salary,post):
        self.salary = salary
        self.post = post
        person.__init__(self,name,id)

    def details(self):
        print("my name is {}\nmy id is {}\nmy salary is {}\nmy post is {}".format(self.name,self.id,self.salary,self.post))

e = Employee('madhan',19311,45000,'intern')
e.details()


#POLYMORPHISM :
#polymorphism simply means that having same name but can have different forms ie having same name for the method
# have same name but it can perform multiple tasks
#for example if we want to know if a bird fly or not then we can do it using single function.
# in java and python, polymorphism can be achieved using the method overloading and method overriding concepts
class Bird:
    def intro(self):
        print("there will be many birds")

    def flight(self):
        print("most of the birds can fly but some cannot")

class Ostrich(Bird):# this is called single level inheritance
    def flight(self):# this is called method overriding
        print("ostrich cannot fly")

class Parrot(Bird):#this is called hierarchical inheritance

    def flight(self):
        print("parrot can fly")

obj_Bird = Bird()
obj_ostrich = Ostrich()
obj_parrot = Parrot()

obj_Bird.intro()
obj_Bird.flight()

obj_ostrich.intro()
obj_ostrich.flight()

obj_parrot.intro()
obj_parrot.flight()

#ENCAPSULATION :
# encapsulation is one of the fundamental concepts of oops and it describes the idea of wrapping data
# and the methods that work on data in a single unit. this puts restrictions for accessing variables and
# methods directly and can prevent the accidental modification of data. To prevent accidental change an
#objects variable can only be changed by objects methods and those type of variables are known as private
#variables.
# The bext example is a class that it encapsulates all the variables,methods,member functions ects in single
# unit
# .
class Base:
    def __init__(self):
        self.a = "geeks for geeks"
        self.__c = "geeks for geeks"

    def setter(self,var):
        self.__c = var

    def getter(self):
        return self.__c

class Derived(Base):
    def __init__(self):
    #calling the constructor of base class
        Base.__init__(self)
        print("calling private member of base class")
        # print(self.__c) this gives error if we create object for the derived class

base = Base()
print(base.a)
d = Derived()
d.setter("c value is changed")
print(d.getter())# setter and getter methods are universal methods to work with the private members of a class
#print(base.__c) to acces this private variable we can use setter and getter methods

# DATA ABSTRACTION :
# This feature of oops allows us to hide unneccessary features of the user .Also when we donot want to give
#sensitive  parts of our code implementation and this is where the data abstraction came into picture
# data abstraction in python and java can be achieved using abstract classes( anstract classes cannot be
#instatiated)
#for abstraction concept implementation we need to import abc module
from abc import ABC,abstractmethod
class Polygon(ABC):
    @abstractmethod
    def number_of_sides(self):
            pass

class Rectangle(Polygon):
    def number_of_sides(self):
        print("i have four sides")

class Triangle(Polygon):
    def number_of_sides(self):
        print("i have 3 sides")

Rectangle().number_of_sides()
Triangle().number_of_sides()

#
# COLLECTIONS MODULE :
# python collection module was introduced to improve the functionality of built in datatypes . it provides
# various containers
#
# COUNTER :
#   a counter is a subclass of dictionary . it is used to keep the count of an element in the iterable
#   in the form of an unordered dictionary where key is the element in the iterable and the value is the count
#   of that element in the iterable .
from collections import Counter
print(Counter(['A','B','A','A','C','C','C','C','B']))

c = Counter({'A': 3,'B' : 2,'C' : 4 })
print(c)
c.update(['A',1])
print(c)

#ORDERED DICT :
# an ordered dict is also a subclass of dictionary , unlike the dictionary the ordered dict remembers the
# order in which the keys were inserted
# .
from collections import OrderedDict

print("Before deleting:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

for key, value in od.items():
    print(key, value)

print("\nAfter deleting:\n")
od.pop('c')
for key, value in od.items():
    print(key, value)

print("\nAfter re-inserting:\n")
od['c'] = 3
for key, value in od.items():
    print(key, value)

# DEFAULT DICT:
# DefaultDict is used to provide some default values for the key that does not exist and never raises a
# KeyError. Its objects can be initialized using DefaultDict() method by passing the data type as an argument.
# Note: default_factory is a function that provides the default value for the dictionary created. If this
# parameter is absent then the KeyError is raised.


from collections import defaultdict

# Defining the dict
d = defaultdict(int)

L = [1, 2, 3, 4, 2, 4, 1, 2]

# Iterate through the list
# for keeping the count
for i in L:
    # The default value is 0
    # so there is no need to
    # enter the key first
    d[i] += 1

print(d)

# CHAINMAP :
# A ChainMap encapsulates many dictionaries into a single unit and returns a list of dictionaries. When
# a key is needed to be found then all the dictionaries are searched one by one until the key is found..


from collections import ChainMap

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

# Defining the chainmap
c = ChainMap(d1, d2, d3)
print(c)

print(c['a'])
print(c['f'])

# NAMEDTUPLE :
# A NamedTuple returns a tuple object with names for each position which the ordinary tuples lack.
#
# For example, consider a tuple names student where the first element represents fname, second represents
# lname and the third element represents the DOB. Suppose for calling fname instead of remembering the index
# position you can actually call the element by using the fname argument, then it will be really easy for
# accessing tuples element. This functionality is provided by the NamedTuple..

from collections import namedtuple

# Declaring namedtuple()
Student = namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

# Access using index
print("The Student age using index is : ", end="")
print(S[1])

# Access using name
print("The Student name using keyname is : ", end="")
print(S.name)

# DEQUE :
# Deque (Doubly Ended Queue) is the optimized list for quicker append and pop operations from both sides of
# the container. It provides O(1) time complexity for append and pop operations as compared to the list
# with O(n) time complexity.
#
# Python Deque is implemented using doubly linked lists therefore the performance for randomly accessing
# the elements is O(n)..

import collections

# initializing deque
de = collections.deque([1, 2, 3])

# using append() to insert element at right end
# inserts 4 at the end of deque
de.append(4)

# printing modified deque
print("The deque after appending at right is : ")
print(de)

# using appendleft() to insert element at left end
# inserts 6 at the beginning of deque
de.appendleft(6)

# printing modified deque
print("The deque after appending at left is : ")
print(de)

# using pop() to delete element from right end
# deletes 4 from the right end of deque
de.pop()

# printing modified deque
print("The deque after deleting from right is : ")
print(de)

# using popleft() to delete element from left end
# deletes 6 from the left end of deque
de.popleft()

# printing modified deque
print("The deque after deleting from left is : ")
print(de)


# USER DICT :
# UserDict is a dictionary-like container that acts as a wrapper around the dictionary objects. This container
# is used when someone wants to create their own dictionary with some modified or new functionality.

from collections import UserDict


# Creating a Dictionary where
# deletion is not allowed
class MyDict(UserDict):

    # Function to stop deletion
    # from dictionary
    def __del__(self):
        raise RuntimeError("Deletion not allowed")

    # Function to stop pop from
    # dictionary
    def pop(self, s=None):
        raise RuntimeError("Deletion not allowed")

    # Function to stop popitem
    # from Dictionary
    def popitem(self, s=None):
        raise RuntimeError("Deletion not allowed")


# Driver's code
d = MyDict({'a': 1,
            'b': 2,
            'c': 3})

print("Original Dictionary")
print(d)

d.pop(1)

# USER LIST :
# UserList is a list-like container that acts as a wrapper around the list objects. This is useful when
# someone wants to create their own list with some modified or additional functionality..


# Python program to demonstrate
# userlist


from collections import UserList


# Creating a List where
# deletion is not allowed
class MyList(UserList):

    # Function to stop deletion
    # from List
    def remove(self, s=None):
        raise RuntimeError("Deletion not allowed")

    # Function to stop pop from
    # List
    def pop(self, s=None):
        raise RuntimeError("Deletion not allowed")


# Driver's code
L = MyList([1, 2, 3, 4])

print("Original List")
print(L)

# Inserting to List"
L.append(5)
print("After Insertion")
print(L)

# Deleting From List
L.remove()

# UserString
# UserString is a string-like container and just like UserDict and UserList, it acts as a wrapper around
# string objects. It is used when someone wants to create their own strings with some modified or
# additional functionality. .

from collections import UserString


# Creating a Mutable String
class Mystring(UserString):

    # Function to append to
    # string
    def append(self, s):
        self.data += s

    # Function to remove from
    # string
    def remove(self, s):
        self.data = self.data.replace(s, "")


# Driver's code
s1 = Mystring("Geeks")
print("Original String:", s1.data)

# Appending to string
s1.append("s")
print("String After Appending:", s1.data)

# Removing from string
s1.remove("e")
print("String after Removing:", s1.data)


#Variables:
# variables are reserved memory locations(means when you create a variable you create some space in the memory)
# based on the data type of variable interpreter allocates memory
# and decides what can e stored in the reserved memory
# therefore,by assigning different data types we can store integers
# ,characters,strings,decimals in these variables
# Assigning values to variables:
# pyhton do not need an explicit declaration to reserve memory
# Declaration happens automatically when you assign values to variables
# '=' sign is used to assign values to variables
# The opreand to the left of the = operator is name of the variable
# and the operand to the right of the = operator is value stored in the variable
# For example ;
m = 'madhan'#it is a string
n = 33#it is an integer
p = 55.99#if is a floating type number
print(m,'\n',n,'\n',p)
#in the above code madhan,33,55.99 are the values assigned to the variables
# which produces the result as shown in the console
# Multiple assignment;
# python allows to assign a single c
#vallue to multiple variables simultaneously, For example.
a = b = c = 1
print(a,b,c)
#Here an integer object is created with value 1 and all three variables
# assigned to the same memory location
# similarly you can also assign multiple objets in a single line.
a,b,c = 1,1.1,'madhan'
print(a,b,c)
#data stored in memory can be of many types
# ex. person's age is of numeric type and adress can have alpha
# numeric types
# python has various datatypes that are used to define the possible
# operations that can be performed on the variable and storage method
# for each of them
# Python have five standard data types
# 1.Numbers
# 2.String
# 3.list
# 4.Tuple
# 5.Dictionary
# Number type stores only number values and number objects are created
# when you assign values to them
# ex.
var1 = 10
var2 = 20
print(var1,var2)
#you can delete the reference of number object by using del statement
# you can delete reference of multiple variables at a time.
del var1,var2
# print(var1,var2)
#python supports four different numeric types;
#1.int(signed integers)
# 2.long(long integers,they can also be represented in octal and
# hexadecimal)
# 3.float (floating point real values)
# 4.comlex (complex numbers)
# pyhton allows you to use lowercase l for long but try to use L
# always because to avoid confusion with number 1.
#we use j to represent imaginary numbers.
# Python Strings:
# String in python is identified as contiguos set of charachters
# represented in single or double qoutes
# subset of string can be taken using slice operator([] or [:])
# with indexes staring 0 at the beginning and -1 from the end
# plus(+) is string concatenation operator and asterisk(*) is
# string repetition operator .For example:.
str = 'Hello python!!!'
print(str)
print(str[0:])
print(str[:-1])
print(str[2:])
print(str[:2])
print(str*2)
print(str+' TEST')
#3.Python list:
#it is most versatile of pythons compound data types.
# list contains items seperated by commas and enclosed by square
# brackets
# to some extent lists are similar to arrays in C
# the one difference is that the items belong to list are of
# different datatypes
# the values stored in the list can be accessed using slice operator
# with indexes starting from 0 and -1 from end
# + is list concatenating operator and * is list repetition operator
# For example:.
list1 = [1,2,3,4]
list2 = [1,1.1,'madhan']
print(list1)
print(list2)
print(list1[0])
print(list2[-1])
print(list1+list2)
print(list1*2)
list1[0]=0
print(list1)
#4.Tuples:
#tuples is another sequence datatype which is similar to list
# tuples also consists of number of values seperated by comma
# and are enclosed with in parantheses()
# main difference between tuples and lists is that the list are
# enclosed in the brackets and elements can be updated but the
# tuples are enclosed in the parantheses and cannot be updated
# hence tuples are immutable and lists are mutable
# tuples can be thought of as read only lists.
#tuples also supports slicing
tup1 = (1,2,3,4,5)
# tup1[0]=0
# print(tup1) this gives error because tuples are immutable
print(tup1[0])
print(tup1[:3])
print(tup1[::-1])
print(tup1*2)
print(tup1+tup1+tup1)
#5.dictionary:
#python's dictionary consists of key:value pairs
# key can be almost any type but mostly used are numbers or strings
# dictionaries are enclosed by curly braces but are accessed using
# square braces.
dict = {}
dict['mad']='han'
dict[1] = 2
tinydict = {4:3,'han':'mad'}
print(dict)
print(tinydict)
#dictionary cannot be concatenated and key are immutable but
# values are mutable.
print(dict.keys())
print(dict.values())
#we can access values of dictionaries using its keys
#operators are construsts that can manipulate the values of
# operands
# pyhton language supports 7 types of operators
# 1.Arithmetic operators
# +,-,*,/,%,**,//.
# 2.Comparison or relational operator
# ==,!=,<>,<,>,<=,>=
# 3.Assignment operators
# =,+=,-=,*=,/=,%=,**=,//=
# 4.Logical operators
# and,or,not
# 5.Bitwise operators
# &,|,^,~(2's complement),<<,>>
# 6.Membership operators
# in,not in
# 7.Identity operators.
# is,is not
#Python decision making:
#decision making is anticipation of conditions occuring while
# execution of program and specifiying actions taken according to
# conditions
# decision structures evaluate multiple expressions which
# produce TRUE or FALSE as outcome and you need to determine which action
# to take and which statements to execute if outcome is TRUE or
# FALSE
# python programming language assumes non zero and non null values as true
# and if is zero or null then it is false
# python language provides following types of decision making statements
# 1.if statement
# 2.if...else statement
# 3.Nested...if statement
# =>if statement:it is similar to that os other languages
# if statement contains a logical expression using which
# data is compared and a decision is made based on the result
# of comparision
# if the expression evaluates to be true then the statements in
# the if block are executed
# if the expression evaluates to be false then the statements in
# the false block will be executed,For example.
if 1>0:
    print('1 is greater than zero')
var = 100
if var:
    print('TRUE')
var = 0
if var :
    print('TRUE')
else:
    print('FALSE')
var = 3
if var<1:
    print('<1')
elif var<2:
    print('<2')
elif var<3:
    print('<3')
elif var<4:
    print('<4')
#nested if
var = 100
if var%10==0:
    if 10/5>1:
        print('yes')
#python loops:
#loops are used when we need to execute a block of code repeatedly
# python language provide more control structures that allow for more
# more complicates execution paths
# loop statement allows us to execute a statement or group of
# statements multiple times
# python programming language provides following types of loops
# to handle looping requirements
# 1.while    2.for       3.nested loop.
i = 0
while i<10:
    print(i,end=' ')
    i+=1
else:
    print('\nwhile loop is ended')
print('bye bye')
#single statement while loop
# flag = 1
# while(flag):print('yes')
#infinite while loop:
# a loop becomes infinite when the condition never resolves
# to be false.you must use the caution when using while loop
# because there is possibility that the given condition never
# resoves to be FALSE.this results in a loop that never ends
# this is called as infinite loop,for example.
flag = 0
while(flag):
    i = input('enter any number:')
    print(' u entered a number')
#for loop:
#it has the ability to isterate over the items of any sequence
# such as list or a string
# for example:.
for i in 'madhan':
    print(i,end='')
#each item in the list or  string is assigned to variable
# specified in the for statement
# and the statement lock is executed until the list or string
# exhausted.
n = 1
# word = input('\nenter any string : ')
word = 'madhan'
for i in word:
    print(n,' : ',i)
    n += 1
str = 'madhan'
for i in range(len(str)):
    print(str[i],end = '')
print()
#break:
#break statement in python terminate the current loop and
#resumes execition at the immediate next statement,just
# like the traditional break in C
# the common use for break statement is when an external
# condition is requiring an hasty exit from loop
# break statement can be used in both while and for loop
# continue:
# it returns the control to beginning of loop
# continue statement rejects all the remaining statements in
# the current iteration and returns the control to the beginning
# of the loop
# it can also be used in both while and for loop
# pass:
# pass statement is a null operation, nothing happens when it executes
# pass is also useful when your code will eventully go but
# has not been written yet
# we can use else with for loop as given below.
i = 2
while i<10:
    j = 2
    while j<=(i/j):
        if i%j==0:
            break
        j = j+1
    if j>(i/j):
        print(i,' is prime.')
    i = i+1
print()
# lower = int(input('enter the lower number : '))
lower = 2
upper = 20
# upper = int(input('enter the upper number : '))
for i in range(lower,upper+1):
    if i>1:
        for k in range(2,i):
            if i%k==0:
                break
        else:
            print(i,end = ' ')
#str.format()
#it is used if you want to insert a variable or expression or
# object into another string and display it to user as a
#single string
# format() method will return a resulting string with inserted
# values and this method works for all releases of python 3.x
# format() method uses its arguments to substitute an appropriate
# value for each format code in the template,syntax can be given as
# str.format(p0.p1.....k0=v0,k1=v1.....) where p0,p1... are called
# positional arguments and k0,k1... are called keyword arguments
# str is a mixture of text and flower braces with indexed or
# keyword types then indexed and keyword types are replaced by
# their appropriate argument values and displayed as a single
# string
# formatted strings or f strings were introduced in python 3.6
# f string is string literal that is prefixed with f
# f at the beginning of the string tells python to allow
# currently valid variables.
triple_quote_string = '''This 
is..triple ... quote'''
print(triple_quote_string)
lst= [i for i in range(0,5)]
print(lst)
str = 'SNIST'
print(list(str))
lst.insert(5,5)
print(lst)
print(lst.index(5))
list1 = [1,2,3,4,5,6,7,8,9,0]
for i in range(list1.index(list1[-1])+1):
    print(list1[i])
name = 'madhan'
print(name.split('a'))
print(len(list1))
tu = 12,3,4,5,6,7,0
print(tu)
print(type(tu))
#packing tuples
tupack = ('page','number',33)
#unpacking tuple
a,b,c = tupack
print(a,b,c)
x = ('string')
print(type(x))
#it is not sufficient to enclose a single value in a tuple but
# in order to convert it into tuple precede the element with a
# comma ,for example in x.
x = ('string',)
print(type(x))
t = tuple()#constructs an empty tuple
#comparision operators are used by tuples to compare them
# position by position.
day = ('sunday')
print(tuple(day))
day1 = ('monday')
nested_tuple = (tuple(day),tuple(day1))
print(nested_tuple)
#tuple can be concatenated with another tuple only
print(sorted(tuple(day)))
l = list(tuple(day))
print(l)
#
# t = tuple()
# n = int(input('enter the number of elements to be entered : '))
# for i in range(n):
#     t += (input('enter the element : '),)#tuple concatenation
# print(t)

# list = list()
# n = int(input())
# for i in range(n):
#     list.append(i)
#     t = tuple(list)
#
# lis = [1,2,3,4,5,6,7,8]
# dic = dict.fromkeys(lis)
# print(dic)
# d = {}.fromkeys(range(5),10)
# print(d)
# print(dic.get(9,'not found'))
# print(dic.items())
# print(dic.keys())
# print(dic.pop(1))
# print(dic.popitem())
# print(d.setdefault(5))
# dic = dic.update(d)
# print(dict)
# print(d.values())
# dict1 = {'a':1,'b':2}
# dict2 = {'c':3}
# print(dict1.update({'d':4}))

d = {'a':1,'b':2,'c':3}
for i in d :
    print(d[i])
del d['a']
print(d)
print(d.keys())
print(d.items())
print(d.values())

tup = (('a',1),('b',2))
# print(dict(tup))

s = 'string'
l = list(s)
print(l)
print(''.join(l))

s = 'abcd'
s = s.replace('a','-').replace('d','a').replace('-','d')
print(s)
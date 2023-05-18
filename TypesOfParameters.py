
def add(a,b):#a and b are called parameters
    c=a+b
    print(c)

add(5,6)#5 and 6 are called arguments
#we have 4 types of argument passing
#1.positional arguments
#2.keyword arguments
#3.default arguments
#4.variable length arguments
print()
def person(name,age):
    print('name : ',name)
    print('age : ',age)
#person('madhan',20)
#we need to take care of arguments while passing them to function
#what if i dont know the sequence in which the actual args to be passed?
#like if we pass 20 for name and madhan for age
person(20,'madhan')#wrong assign(position arguments,we need to be aware of
#positions of actual and formal arguments)
print()
person(age=20,name='madhan')#using keywords solves the problem and this is
# called the keyword arguments
print()
def person(name,age=18):#defaut arguments,we can give a default value to argument
    #when no value at actual argument is passed the default value will come in to
    #picture and if we pass the value at actual parameter even there is default
    #value then it overrides the default value
    print('name : ',name)
    print('age : ',age)
person('madhan')
print()
#variable lemgth arguments
def add(a,*b):#here *b implies it can accept multiple values as formal
    # arguments from actual arguments
    #c=a+b
    print(a)
    print(b)#here b is formed as tuple
    c=a
    for i in b:
        c= c+i
    print(c)
add(5,6,7,8)
print()
def add(*b):
    print(b)#here b is formed as tuple
    c=0
    for i in b:
        c= c+i
    print(c)
add(5,6,7,8)


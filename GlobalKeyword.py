
a=10#the variable defined outside the function are called global vars
def function1():
    #if you want to change the value of global var in function
    #you should specify in the function that you are using global var
    global a
    #after specifying a as global we cannot create another variable named a
    #we cannot have global and local variable with same name in the same function
    #we can get rid of this problem using function called globals()
    #ie we can change the global var value but also we can create and access
    #local var with same name and in same function
    a=20#if the variable is defined inside the function it is called local var
    b=4#when there are two vars with same name such that one is local and
    #another is global then preferece will be always given to local variable
    print('local : ',a)
function1()
#print(b) we cannot use local variable outside the fumction
print('global : ',a)
print()

a=10
print(id(a))
def function1():
    a=9
    x=globals()['a']#this function will collect all the global vars but we can also
    #specify which global var need to be collected
    print(id(x))#ids will be same that means x also refers to same val in a
    print('local : ',a)
    globals()['a']=15
function1()
print('global : ',a)
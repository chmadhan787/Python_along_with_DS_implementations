# namespaces in python are mapping of names to objects.
# they are implemented as python dictionaries.
# builtin name spaces - ex print(),type() ,these can be used where ever in the program
# global name spaces - like modules and classes
# local name spaces - like functions

# using the global variable inside function without changing the value
sum = 10
def f():
    balance = 100
    total = balance + sum
    # the global sum variable can be accessed by the function and then it can modify it
    # but that modification will not be applicable to the global var sum
    print(total)
f()
print(sum) # prints the global value of sum

# changing the value of global variable inside the function creates a new variable
# with same name and that will be visible to global space
sum1 = 20
def f1():
    sum1 = 30 # when we assign a value to the global sum1 in local then a new variable
    # named sum1 will be created locally with assigned value and there will be no
    # relation between the local and global sum1
    balance1 = 200
    total1 = balance1+sum1
    print(total1)
f1()
print(sum1) # since the local sum1 variable bot visible to global space the value 20
# will be printed in the output

# using the global varaible as i is even we change the value of that in local space
sum2 = 30
def f2():
    global sum2
    sum2 = 50
    balance2 = 300
    total2 = balance2 + sum2
    print(total2)
f2()
print(sum2) # this value is a modified value of global variable inside the local space


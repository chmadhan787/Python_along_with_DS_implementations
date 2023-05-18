# if we dont mention function name it becomes anonymous
#we can also call them as lambdas
#if you want to use any function only once and you dont want to create any
#name to it we can use lambda
#we can pass functions to functions as functions are objects in python
def square(a):
    return a*a
y=square(5)
print(y)
print()
f = lambda a : a*a #a is argument and this is anonymous function or lambda func
y=f(5)#since function is object in python we assign it to var as f
print(y)
#always your lambda should have only one expression
print()
t = lambda b,c : b+c
n=t(5,6)
print(n)
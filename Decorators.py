# in python we can return a func from a function, for example

def funcret(num):
    if num == 0:
        return int
    if num == 1:
        return sum

a = funcret(0)
print(a)
b = funcret(1)
print(b)

# along with that inp python we can pass a funciton as an argument to a function
# for example :
def executor(func):
    func("this is from print")

executor(print)

# from the above two example we came to a conclusion that we can pass functions as
# an argument to a function as well as we can return a function from a function.
# from this we get the decorators concept...
# using decorators we can change the class method or attribute without affecting
# the client side code.
# What is Decorator Actually ?
# In Python, decorators are a way to modify or enhance the behavior of functions or
# classes without directly modifying their source code. Decorators are applied using
# the @decorator_name syntax, placed above the function or class definition.
#
# A decorator is essentially a callable (a function or a class) that takes another
# function or class as input and returns a modified version of it. This allows you
# to add functionality to functions or classes dynamically.

# hence by using this decorators in python we can extend the functionalities of a
# function for example :
def dec1(func1):
    def nowexec():
        print("executing now")
        func1()
        print("executed")
    return nowexec
@dec1
def who_is_madhan():
    print("madhan is a good boy")

# who_is_madhan = dec1(who_is_madhan) this line can be done in another way that is
# by using the @ symbol along with the name of function used for
# extending the functionality upon definition of the original function whose
# function is to be enhanced.
who_is_madhan()


def div(a,b):
    print(a/b)

#if i want a logic like the numerator should always be greater than the denominator
#using decorators we can add extra features to the existing functions
#we can write a function inside a function

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner
div1 = smart_div(div)
div1(2,4)
#using decorators we can change the behaviour of existing function at compile
#time itself
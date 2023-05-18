#function arguments or parameters
#types of arguments or parameters
#pass by value

#the values which are passed in the function call are called actual parameters
#the arguments which accepts the parameters passed from function call in fuction
# def are called formal parameters
#in call by value the values of actual parameters are passed into formal
#parameters having different address so what ever changes done to formal
#parameters inside the fuction doesnt effect the values of actual parameters
def update(x):#here value of x(x should have new adress but in python its
#address is same as address of actual parameter and hence at definition both
# x and a points to single memory location with value 20) is 20 copied from a

    print(id(x))
    print(x)
    x=8#when x value is manipulated to 8 its address will be changed and there
# is no link in between x and a ,now so value of a remains unchanged
    print('x ',x)
    print(id(x))
    print('a ', a)
a=20
print((id(a)))
update(a)#here we are passing the value of a ie 20
#when we use pass by value the x takes same(different in other languages) adress for same value of
# a when passed so both are not linked
print('a ',a)
#the nxt concept is pass by reference ie passing the address
#in this when we change the value of a(lst) then it affcts x(lst in def)
#in python we dont use pass by value or pass by reference.

# Python’s argument passing model is neither “Pass by Value”
# nor “Pass by Reference” but it is “Pass by Object Reference”.

#since list is mutable we can do following and below thing is called pass by
#object reference
print()
def update(lst1):
    print(id(lst1))#the reference id will not be changed
    lst1[1]=25#even after manipulating the lst using lst1
    print(id(lst1))#but the values in the lst can be changed using lst1
#the computations will be done without changing the address of lst
    print('lst1 ',lst1)
lst = [10,20,30]
print((id(lst)))
update(lst)#here the reference id of the lst is passed
print('lst ',lst)
#if we change values of list inside the fuction it will be reflected to
# original list also
#in the above code lst is taken as object and that object reference is passed
#to formal parameter lst1 in function def
#hence lst and lst1 will refer to same object in the memory
#now what ever the operation done by function update() on the lst1 will surely be
#reflected to lst outside the function because they share the same object memory
#in simple words, in pass by reference the function and the caller use same
#variable and object

# Pass by Value:
# In pass by value the function is provided with a copy of the argument
# object passed to it by the caller. That means the original object stays
# intact and all changes made are to a copy of the same and stored at
# different memory locations.

# Pass Object by Reference:
# As python is different in this context, the functions in python receive
# the reference of the same object in the memory as referred by the caller.
# However, the function does not receive the variable(the bucket) that the
# caller is storing the same object in; like in pass-by-value, the function
# provides its own bucket and creates an entirely new variable for itself.
#The same object in the memory is referred by both the caller and the function,
# so when the append function adds an extra element to the list, the caller
# object gets updated too. They have different names but are the same thing.
# Both the variables contain the same object. This is the meaning behind
# pass by object reference. The function and caller use the same object in
# memory, but get them through different variables. Any changes made to the
# function variable(bucket) won’t change the nature of the caller variable
# (bucket), only the content gets updated.
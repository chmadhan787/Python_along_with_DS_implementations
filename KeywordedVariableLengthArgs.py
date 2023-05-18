def person(name,*data):
#when i have no idea of what the user want to pass through actual parameters
#i need to use *var_name and it will be in the form of tuple
    print(name)
    print(data)
person('madhan',20,'hyderabad',9949199787)
print()
def person(name,**data):
# if we want to assign the key words to actual parameters in *data tuple
#     we need to use another star like **data
    print(name)
    print(data)
person('madhan',age=20,place='hyderabad',mobile=9949199787)
#this concept is called as keyword variable length arguments
#this can also be done in the following way
print()
def person(name,**data):
    print(name)
    for i,j in data.items():#here i refer to keys and j refer to
        # actual arguments
        print(i,j)
person('madhan',age=20,place='hyderabad',mobile=9949199787)
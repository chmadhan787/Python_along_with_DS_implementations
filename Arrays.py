#arrays in python doesnt have fixed size
from array import*

# the methods supported by array are same as lists in python

vals = array('i',[3,6,4,-7,5,2])#array('type code',[])(i for signed int)
vals1=array('I',[3,5,2,1])#I represents usigned int so it wont accept negative
#values

print(vals)
print()

print(vals1)
print()
#buffer_info() gives the size of array

print(vals.buffer_info())#1st parameter is address and second is size in output
vals.reverse()
# accessing using index values
for i in range(len(vals)):
  print(vals[i])
print()

for i in vals:
    print(i)
print()

u=array('u',['a','e','i','o','u'])

for i in u:
    print(i)
print()
#copying the array and manipulating the values
newArr = array(vals.typecode,(t*t for t in vals))#typecode copies the type of vals
for i in newArr:
    print(i)
print()
#accessing array elements using while
i=0#initialization
while i<len(newArr):#condition
    print(newArr[i])
    i+=1#updation




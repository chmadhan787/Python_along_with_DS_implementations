from array import *
arr = array('i',[])
n=int(input('enter the length of the array : '))

for i in range(n):
    x = int(input('enter next value : '))
    arr.append(x)
print()
print(arr)#prints array with type
print()
#or
for i in arr:
    print(i)#prints just elements of array
print()

value = int(input('enter number for search : '))
k=0
for i in arr:
    if i==value:
        print('index is : ',k)#manually searching and printing index value
        break#if we dont use break then we get indices for repeated values also
    k+=1
else:
    print('no element found')
print()
print('index is : ',arr.index(value))
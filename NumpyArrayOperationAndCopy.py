from numpy import *
arr1 = array([1,2,3,4,5])
#arr1 = arr1 + 5
print(arr1)
print()
arr2 = array([1,2,3,4,5])
arr3 = arr2+arr1#for this array sizes should be same(this operation also called
# as vectorized operation
print(arr3)
print()
#to find sin value of each element in array ,lly for cos,log ,sqrroot
print(sin(arr1))
print()
print(log(arr1))
#to get addition of entire array elements
print()
print(sum(arr1))
#to join two arrays
print()
print(concatenate([arr1,arr2]))
print()
#copying array
arr2 = arr1
print(arr2)
print()
print(id(arr1))
print(id(arr2))
print()
#we can see that both the arrays poinsto same location , it is called aliasing ie
#we are creating new allies(name) for same array
#we can modify the array values using arr1 or arr2
#to create new array at different location with same values, use view() function like
arr2 = arr1.view()
print(id(arr1))
print(id(arr2))
print()
#now if we check the address of both arrays will be different
#when we come to copying concept we have two types of copying methods
#1.shallow copy and 2.deep copy
#in shollow copy values will be copied but when we manipulate values in one
#array ,will reflect on another array elements(both arrays are linked to
# each other) for example
arr1[1] = 7
print(arr1)
print(arr2)
print()
#but in deep copy both arrays are not linked to each other in any way
#use copy() function in place of view() to attain deep copy
arr2 = arr1.copy()
arr1[1] = 6
print(arr1)
print(arr2)
#hence we see that changes will be reflected in arr1 but not in arr2
#adding arrays using for loop
print()
arr4 = zeros(5,int)
x=0
for i in range(len(arr4)):
    arr4[i]=arr1[i]+arr2[i]
print(arr4)
#finding maximum of array
print()
max=arr4[0]
for i in arr4:
    if max<i:
        max=i
print(max)

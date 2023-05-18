#we need to use third party package called numpy to implement
#we can also create single dimensional arrays in numpy
#multidimentional array
#by default numpy package is not available in python we need to install it
from numpy import *
arr = array([1,2,3,4,5,6],int)#here datatype is optional
#by default numpy will guess the datatype of values
#syntax
#array([values],datatypes)

# why numpy arrays are important means we can perform arithmatic operation directly
# on two arrays like :

numpy_array = array([1,2,3,4],int)
print(*numpy_array)

numpy_array1 = array([5,6,7,8])
print(*numpy_array1)

print(*numpy_array + numpy_array1)
print(*numpy_array * numpy_array1)
print(*numpy_array1 // numpy_array)
print(*numpy_array - numpy_array1)
print(*numpy_array1 % numpy_array)

#we have six ways to create an array in numpy
# 1.array()
# 2,linspace()
# 3.logspace()
# 4.arrange()
# 5.ones()
# 6.zeros()
print("type of values in arr : ",arr.dtype)
print(arr)
print()
arr1 = array([1,2,3,4,5.0])
print("type of values in arr1 : ",arr1.dtype)
#even there is one floating number entire array will be taken as
#floating type and also the remaining values are converted into floating type
print(arr1)
print()
#you can directly mention the type in array declaration
arr2 = array([1,2,3,4,5],int)
print("type of values in arr2 : ",arr2.dtype)
print(arr2)
print()
arr3 = array([1,2,3,4,5],float)#you have integer values but you have mentioned
#float then the values will be converted into floating type
print("type of values in arr3 : ",arr3.dtype)
print(arr3)
print()
#linspace(start,stop,step),step is optional
arr4 = linspace(0,15,16)#here 15 is included unlike range()
#and the 0-15 is divided into 16 parts hence here the step decides the
#number of parts that the range is to be divided
#difference between values will be constant unlike logspace
#if we dont mention the number of parts by default it will be 50
print(arr4)
print()
#arrange(start,stop,step)
arr5 = arange(1,15,2)
print(arr5)
print()
#logspace(start,stop,parts)
arr6 = logspace(1,40,5)#here the difference between the elements depends
#log values, it starts from 10 raise to 1 and goes till 10 raise to 40
print(arr6)
#for printing only two digits in output
print('%.2f'%arr6[0])
print('%.2f'%arr6[4])
print()
#zeros(size,datatype),it creates array of specified size and all default
# values will be zeros and datatype is optional,default datatype is float
arr7= zeros(5)
print(arr7)
#ones(size,datatype),working is similar to zeros()
print()
arr8 = ones(5)
arr9=ones(5,int)
print(arr8)
print()
print(arr9)
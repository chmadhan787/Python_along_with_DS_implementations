from numpy import *
arr1 = array([
    [1,2,3,5,4,3],
    [5,6,7,8,7,5]
])
print(arr1)
print(arr1.dtype)
print(arr1.ndim)#ndim gives the dimension number ie 2 as of now
print(arr1.shape)#gives(rows,columns)
print()
#converting one dimensional array to two dimension
arr2 = arr1.flatten()
print(arr2)
print()
arr3 = arr2.reshape(3,4)
print(arr3)
arr2 = arr1.flatten()
#converting one dimensional array into three dimentional array
print()
arr3 = arr2.reshape(2,2,3)#2 2d arrays has 2 1d arrays has 3 values each
print(arr3)
print()
arr1 = array([
    [1,2,3],
    [4,5,6]
])
m = matrix(arr1)
print(m)
#or
print()
m = matrix('1,2,3;8,4,5;6,0,9')
print(m)
print()
print(diagonal(m))
print()
print(m.max())
m1 = matrix('1,2,3;8,4,5;6,0,9')
m2 = m + m1
print()
print(m2)
print()
m2 = m * m1
print(m2)

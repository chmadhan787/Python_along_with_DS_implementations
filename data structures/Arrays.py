# an array is a linear data structure and it is a collection of items stored at contiguous memory locations
# the idea of array is to store multiple items of same type together in one place
# it allows the processing of large amount of data in relatively short period of time
# the first element of array is indexed with a subscript of 0
# there are different operations possible in array like searching ,sorting,inserting ,traversing ,
# reversing and deleting.
#
# Characteristics of array :
# *arrays use an index based data structures which helps us  to identify each of the elements in an array using
# index
# *if a user wants to store multiple values of same type then ,the array can be utilized efficiently
# *an array can also handle complex data structures by storing data in two dimensional array
# *an array is used to implement other data structures like stacks,queues,heaps,hash-tables etc
# *the search process in an array can be done very easily
# there will be no static array in python , there will be only dynamic array in python and that is the list in python
#
# Applications of array :
# *an array is used in solving matrix problems
# *data base records are also implemented by an array
# *it helps in implementing a sorting algorithm
# *it is also used to implement other data structures like queues,stacks,heaps,hash tables etc
# *an array can be used for CPU scheduling
# *an array can be applied as a look up table in computers
# *Arrays can be used in speech processing where every speech signal is an array
# *a screen of computer is also displayed by an array. here we use multi dimensional array
# *array is used in many management systems like library,students, parliament
# *arrays are used in online ticket booking system
# *contacts in the mobile are displayed using an array
# *arrays is used in games like online chess, where the player can store his past and present moves
# *it is used to store images in specific dimensions in android like 360*120
#
# Real life applications of array
# *an array is frequently used to store data or mathematical computations
# *it is used in image processing
# *it is also used in record management
# *book pages are also real life examples of array
# *it is used in ordering boxes as well
#
# Arrays uses ram to store data
# for each integer number we use 4 bytes.

#time complexity for looking an element of array using an index is O(1)
# but to lookup an array element by value then the time complexity will O(n)
# for array traversal the time complexity is of O(n)
# inserting element at a specific position in an array has time complexity of O(n)
# deleting element from the specific position of the array has time complexity of O(n)
# in python list is implemented as dynamic array but in other languages like java ,c++ they have both static and
# dynamic array but in dynamic array there will be an overhead of allocating memory
# array in python can store different types of data types
# but in java and c++ this cannot be done
# we can also have two dimensional and three dimensional array
# hence we can say that there is no static array in python language
# Example on array.
expenses = [['january',2200],['february',2350],['march',2600],['april',2130],['may',2190]]
print(abs(expenses[0][1]-expenses[1][1]))
sum = 0
for i in range(3):
    sum =  sum+ expenses[i][1]
print(sum)
for i in range(len(expenses)):
    if expenses[i][1]==2000:
        print(expenses[i][0])
expenses.append(['june',1980])
for i in range(len(expenses)):
    if expenses[i][0] == 'april':
        expenses[i][1] -=200
print(expenses)

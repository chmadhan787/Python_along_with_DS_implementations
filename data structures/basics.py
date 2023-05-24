#what is a data structure ?
# data structure is a storage used to store and organize data.it is the way of arranging data on computer
# so that it can be accessed and updated efficiently
# data structures is not only used for organising data but also used for processing,retrieving and storing of that data
# there are different basic and advanced types of datastructures which are used in almost every program or
# software that has been developed. so, we must have a good knowledge about data structures .

#classification of datastructures :
#it is classified into two types based on their appearance as linear and non linear data structures
# in linear data structures we have static i.e, array and dynamic i.e, linkedlist,queue,stack
# in non linear data structures we have tree,graph
# LINEAR : data structures in which elements are arranged sequentially or linearly, where each element
# is connected to next and/or previous element , is called as linear data structures
# STATIC : static data structures have fixed size of memory, it is easier to access elements in static
# data structures
# DYNAMIC : in dynamic data structure ,the size is not fixed .it can be randomly updated during the runtime
# which may be considered efficient concerning the memory(space) complexity of the code
# NON-LINEAR :datastructures in which the data elements are not arranged sequentially or linearly
# but in case of non linear datastructures we cannot traverse all the elements in the single run only
#
#how data structures varies from data types?
#refer intro to data structures notes
#
# by using data structures ,one can organize and process very large amount of data in a relatively short period
#
#
# NEED OF DS :
# - data structure provides data representation which is easy to understand for the developer and the user
# can make an efficient implementation of the operation
# - data structures can provide an easy way of organizing ,retrieving ,managing and storing data
# here is a list of needs of data structures :
# 1.Data structures modification is easy
# 2.it requires less time
# 3.saves storage memory space
# 4.Data representation is easy
# 5.it provides easy access to large data base.



# data structures are the integral part of computers used for the arrangement of data in the memory
# they are essential and responsible for organizing ,processing ,accessing , and storing data efficiently.

#Data stuctures are the building blocks  or raw material for any software programs
#one cant become a good programmer without sound understanding of datastructures
#data structures are containers ,storing data in a specific memory layout

#BIG O NOTATION:
# it is used to measure how running time and space requirements for your program increases as your input size grows
# the mathematical representation of time required by a program according to size of input is BIG O NOTATION
# this BIG O NOTATION can be used for all programming languages , it is not specific to python programming
# Measuring running time growth is called : time complexity
# Measuring space growth is called: space complexity
# in big o notation generally worst case is most important
# worst case complexity of binary search is O(logn)
# cpu uses ram to store presently executing code variables and data



# Algorithms :
#
# Algorith means a step by step procedure for solving a computational problem
# a program is also a step by step process for solving a problem
# but the difference is that th algorithm is written before writing a program for a problem
# that is the algorithm is like english statements use to understand the logic for solving a problem and to write a
# code , An algorithm is written at the time of designing the code and the program is the thing develop by implemen
# ting the previously written algorithm
# Algorithms will be written by the people who have domain knowledge and the program will be written by the programmers
# we can use any language to write an algo but we must use a programming language to write a program
# both depends on the hardware and operating systems.
# we analyze the algorithm and we test the programs.
#
#
#
# characteristics of algorithm :

# 1. Algorithm can take 0 or more inputs
# 2. Algo must generate atleast one output
# 3. Definiteness - every statement should have only single meaning
# 4. Finiteness - algo must have finite set of statements, every algo must have a termination point
# 5. Effectiveness.
#
#
#
#How to analyze an algorithm ?
# -> check how much time it is taking
# -> check how memory space it is consuming.
# -> if is web based then check the network speed , data rate
# -> check hoe much power it is consuming.
# -> check how mush cpu registers it requires.
#
#
# Tricks to analyze the complexity of the algorithms with for loops
#
# 1. for(i = 0; i < n; i++) -> O(n)
# 2. for(i = 0; i < n; i = i+2) -> O(n)
# 3. for(i = n; i > 1; i--) -> O(n)
# 4. for(i = 1; i < n; i = i*2) -> O(logn{base 2})
# 5. for(i = 0; i < n; i = i*3) -> O(logn{base 3})
# 6. for(i = 0; i < n; i = i/2) -> O(logn{base 2})
#
# Tricks to analyze the complexity of the algorithms with while and if
#
# i = 0
# while i < n:      -> O(n)
#       i++ same for i--
#
#
# a = 1
# while a<b:        -> O(logb{base 2}) or O(logn{base 2})
#   a = a*2
#
#
# a = 1
# # while a<b:        -> O(logb{base 2}) or O(logn{base 2})
# #   a = a/2
#
#
# i = 1
# k = 1
# while k < n:         -> O(n^1/2)
#   k = k + i
#   i = i + 1
#
#   finding GCD of two numbers
#  while m!=n:          -> O(n)
#       if(m > n):
#           m = m-n
#       else:
#           n = n-m
#
#
# for the conditional statements like "if" the statements inside "if" will we executed only when the condition
# becomes true i.e, only once so the complexity will be O(1)
#
#
#
# What is Divide and Conquer?
#
# it is related to strategy( is an approach or design for solving a problem ) for solving a problem
# assume problem "P" is of size = n
# we can break that problem into sub problems like P1, P2, P3 .... let say up to Pk.
# now these sub problems can be solved to obtains solutions individually like S1, S2, S3 ..... let say up to Sk
# we combine all the solutions to get the absolute solution for the main problem as "S".
# we can apply divide and conquer for the sub problems also.
# sub problem must be same as the main problem like if  the main problem is sort then the sub problems also must be
# sort
# we can apply devide and conquer to certain problem such that if we break the problem then the problem must
# remain same ans also we should have a method for combining
#
# DAC(P):
#   if small(P):
#       S(P)
#   else:
#       divide P into P1, P2, P3, .... Pk
#       Apply DAC(P1), DAC(P2), ....
#       combine(DAC(P1), DAC(P2), ....)
#
# Example for DAC :
# 1. Binary search
# 2. Finding max and min
# 3. Merge Sort
# 4. Quick Sort
# 5. Strassen's Matrix Multiplication.

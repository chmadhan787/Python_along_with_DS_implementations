from functools import reduce
def is_even(n):#the elements in nums are taken as n and performs n%2
    return n%2==0
nums = [1,2,3,4,5,6,7,8,9]
evens = list(filter(is_even,nums))
#filter takes two arguments function and iterable
print(evens)
print()

nums = [1,2,3,4,5,6,7,8,9]
evens = list(filter(lambda n : n%2==0,nums))
print(evens)
print()
#hence using lambda function we can reduce the lines of code
#in order to change a value we can use a function called as map()
#we can use reduce() function in order to convert huge number of values to a single value
#map() also takes function and iterable as arguments
#in order to modify values in an iterable we use map(function or type,iterable)
doubles = list(map(lambda n : n*2,evens))
print(doubles)
print()
#reduce() function belongs to a module called functools and we need to import
#to use it
sum = reduce(lambda a,b : a+b,doubles)
print(sum)
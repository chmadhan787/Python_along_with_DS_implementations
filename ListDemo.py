#by default a square bracket is list
n=[2,3,5,7.7,"a"]
n[1]=6#can be done because list is mutable
print(n)
m=[6,5,"m",6.5]
s=[3,6,2,8]
print(sorted(s))
s.sort()#we cannot print directly while sorting so first we need to sort the
#elements and then print list or else use sorted() function to print sorted
# list in one line
print(s)
print(n)
print(n[3:])
print(n[-1])
print(n[3])
print(n[:2])
print(n[::-1])
#lists can have different datatypes
a=[n,m]
print(a)#we can pass list to a list
#different functions can be performed on the list like append,
# remove etc
#list is mutable that means we can change the values in the list
n.append(33)
print(n)
#append is used to add element at the end but insert is used to add
# element in between
n.insert(4,44)
print(n)
n.remove(44)
print(n)
print(n.pop(1))
print(n)
print(n.pop())#deletes the last element
print(n)
del n[2:]
print(n)
n.extend([6,8,3,0])#to add multiple values at a time
print(n)
print(min(n))
print(max(n))
print(sum(n))

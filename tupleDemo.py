#almost same as list but list is mutable and tuple is immutable
#for tuples we use paranthesis
# t=(32,21,43,56,77)
# print(t)
# #iteration in tuple is faster than list
# print(t[0])
# print(t[::-1])#reverse of a tuple
#5   2 3 6 6 5
n = int(input())
m = list(set(map(int,input().split())))
print(m[-2])
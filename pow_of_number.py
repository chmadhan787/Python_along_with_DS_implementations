#using pow() function
n = int(input())
p = int(input())
from math import pow
print(int(pow(n,p)))

#using simple iteration
t = 1
for i in range(p):
  t*=n
print(t)

#using python operator
print(n**p)

#using recursion
def po(n,p):
    if p==0:
        return 1
    return n*po(n,p-1)
print(po(n,p))
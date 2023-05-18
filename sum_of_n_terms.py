n = int(input())
print((n*(n+1))//2)

print(sum(list(range(1,n+1))))
c = 0
for i in range(1,n+1):
    c+=i
print(c)

def getsum(n):
    if n == 1:
        return 1
    return n + getsum(n-1)

r = getsum(n)
print(r)

print(sum([i for i in range(n+1)]))

import functools
print(functools.reduce(lambda x,y: x+y,[i for i in range(n+1)]))
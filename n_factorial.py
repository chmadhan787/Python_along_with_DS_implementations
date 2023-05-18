#using iteration
n = int(input())
t=n
for i in range(1,n):
    t = t*i
print(t)

#using recursion
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
print(fact(n))
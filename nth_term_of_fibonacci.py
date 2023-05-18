#using recursion
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1) + fib(n-2)
n = int(input())
print(fib(n-1),end = ' ')
print()
#using simple iteration
a = 0
b = 0
for i in range(n):
    c = a+b
    if not c:
        b=1
    a = b
    b = c
print(c)

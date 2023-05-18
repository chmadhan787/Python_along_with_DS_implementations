#without recursion
n = int(input("enter the length :"))
a = 0
b = 0
for i in range(n):
    c = a+b
    print(c,end = ' ')
    if not c:
        a = 1
    b = a
    a = c

print()

def fib(n):
    a,b=0,1
    for i in range(n):
        print(a, end=' ')
        c=a+b
        a=b
        b=c

x = n
if x>0:
    fib(x)
else:
    print('enter positive value')
print()
#with recursion
def fibo(n):
     if n<=1:
         return n
     else:
         return fibo(n-1)+fibo(n-2)

n_terms = 10
if n_terms<=0:
    print('enter only positive numbers')
else:
    for i in range(n_terms):
        print(fibo(i),end = ' ')

print()
#in 3 lines
a,b = 0,1
for i in range(10):
    print(a,end = ' ')
    a,b = b,a+b
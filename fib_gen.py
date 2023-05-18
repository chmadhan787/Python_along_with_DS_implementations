def fib_gen(n):
    a,b = 0,1
    i = 0
    while i<n:
        yield a
        a,b = b,a+b
        i+=1

print(list(fib_gen(10)))

a,b = 0,1
for i in range(10):
    print(a)
    a,b = b,a+b

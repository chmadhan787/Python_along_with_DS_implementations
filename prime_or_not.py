#simple iteration
n = int(input())
c=0
if n<2:
    c=1
for i in range(2,n):
    if n%i==0:
        c+=1
if c==0:
    print(n,' is a prime number')
else:
    print(n,' is a non-prime number')

#optimized by break condition

f = 0
if n<2:
    f=1
for i in range(2,n):
    if n%i==0:
        f = 1
        break
if f:
    print(n,' is a non-prime number')
else:
    print(n,' is a prime number')

#optimization by n/2 iterations
if n<2:
    f = 1
for i in range(2,int((n/2)+1)):
    if n%i==0:
        f=1
        break
if f:
    print(n,' is a non-prime number')
else:
    print(n,' is a prime number')

#optimization by (n)^(1/2)
if n<2:
    f = 1
for i in range(2,int(pow(n,0.5)+1)):
    if n%i == 0:
        f = 1
        break
if f:
    print(n,' is a non-prime number')
else:
    print(n,' is a prime number')

#optimizing by skipping even iteration:
f=0
if n<2:
    f=1
if n==2:
    f=0
for i in range(3,int(pow(n,0.5)),2):
    if n%i==0:
        f=1
        break
if f:
    print(n,' is a non-prime number')
else:
    print(n,' is a prime number')
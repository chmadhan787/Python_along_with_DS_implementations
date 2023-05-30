n=int(input('enter any number'))
c=0
for k in range(2,n):
    if n%k==0:
        print('given number is not prime')
        break
else:
        print('given number is a prime')

# prime check in a single line

print(True if [n for i in range(2,n) if n%i == 0] == [] else False)

print(False if 0 in [n%i for i in range(2,n//2+1)] else True)

def prime_check(n): return 0 not in [n%i for i in range(2,n//2+1)]
print(prime_check(n))

# list of prime number using recursion till n
def prime_rec(n,i,l=[]):
    flag = False
    for j in range(2,i):
        if i%j == 0:
            flag = True
    if flag is False:
        l += [i]
    if i==n:
        return l
    return prime_rec(n,i+1,l)
print(prime_rec(n,2))
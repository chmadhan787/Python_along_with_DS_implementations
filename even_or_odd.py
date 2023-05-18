def even_or_odd(a):
    if a%2==0:
        print(a,' is even')
    else:
        print(a,' is odd')
n = int(input())
even_or_odd(n)

print('given number is even' if n%2==0 else 'given number is odd')

print(n,' is even') if n%2==0 else print(n,' is odd')

def bit_check(n):
    if n&1:
        return n,' is odd'
    else:
        return n,' is even'
r = bit_check(n)
print(r)

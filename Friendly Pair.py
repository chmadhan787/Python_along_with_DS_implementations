a,b = map(int, input().split())

def fac_sum(n):
    l = [i for i in range(1,n) if n%i == 0]
    return sum(l)

if a%fac_sum(a) == b%fac_sum(b):
    print('friendly pair')
else:
    print('not friendly pair')
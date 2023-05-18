n  =int(input())
print('positive' if n>0 else 'negative')

if n>=0:
    if n==0:
        print('zero')
    else:
        print('positive')
else:
        print('negative')

if n>0:
    print('positive')
elif n==0:
    print('zero')
else:
    print('negative')

def p_or_n(a):
    if a>0:
        print('positive')
    elif a==0:
        print('zero')
    else:
        print('negative')
p_or_n(n)
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
        return 'positive'
    elif a==0:
        return 'zero'
    else:
        return 'negative'
p_or_n(n)


def pon(n):
        if n > 0:
            yield True
        elif n == 0:
            yield '0'
        else:
            yield False

v = pon(n)
try:
    print(next(v))
    print(next(v))
    print(next(v))
except:
    print("elements exceeded")
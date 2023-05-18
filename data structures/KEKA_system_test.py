n = int(input())
l = []
def conv(n):
    if n<=5:
        l = [0 if i<10-n else 1 for i in range(10)]
    else:
        l1 = [1]
        l = [0 for i in range(5)]
        l1.extend([0 if i<9-n else 1 for i in range(4)])
        l.extend(l1)
    return l
if n<10:
    print(*conv(n))
else:
    temp = n
    n = n%10
    right = conv(n)[5:]
    n = temp//10
    left = list(reversed(conv(n)))[:5]
    left.extend(right)
    print(*left)




N,M = map(int,input().split())
s = input()
L=[]
R=[]
F=[]
B=[]
for i in s:
    if i == 'L':
        L.append(1)
    elif i == 'R':
        R.append(1)
    elif i == 'F':
        F.append(1)
    else:
        B.append(1)

if sum(L)>=M:
    print('Unsafe')

elif sum(R)>=M:
    print('Unsafe')

elif sum(F)>=N:
    print('Unsafe')

elif sum(B)>=N:
    print('Unsafe')

else:
    print('Safe')
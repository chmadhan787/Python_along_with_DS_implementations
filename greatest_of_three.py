a,b,c = map(int,input().split())
if a>b and a>c:
    print(a,' is greater')
elif b>c:
    print(b,' is greater')
else :
    print(c,' is greater')

if a>b:
    if a>c:
        print(a,' is greater')
    else:
        print(c,' is greater')
elif b>c:
    print(b,' is greater')
else:
    print(c,' is greater')
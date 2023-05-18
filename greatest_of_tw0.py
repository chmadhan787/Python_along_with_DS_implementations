a,b = map(int,input().split())
print(a,' is greater') if a>b else print(b,' is greater')

def greater(a,b):
    if a>b: return a
    else : return b
r = greater(a,b)
print(r,' is greater')

print(max(a,b),' is greater')

if a>b:
    print(a,' is greater')
else:
    print(b,' is greater')
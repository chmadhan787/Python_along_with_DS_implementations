#using simple iteration
n = int(input())
r = 0
for i in range(len(str(n))):
    rem = n%10
    r = r*10 + rem
    n = n//10
print(r)

n = 123
print(str(n)[::-1])

def revnum(n,rev):
    if n==0:
        return rev
    r = n%10
    rev = rev*10+r
    return revnum(n//10,rev)

rev = 0
print(revnum(123,rev))
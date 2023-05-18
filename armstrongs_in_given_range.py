start,stop = map(int,input().split())
s = 0
for i in range(start,stop+1):
    temp = len(str(i))
    t1 = i
    for j in range(len(str(i))):
        t = i%10
        s += t**temp
        i = i//10
    if s == t1:
        print(t1,' is a armstrong number')
    s=0

#using recursion
s = 0
a = []
def arm(start,stop,s):
    if start>stop :
        return a
    l = start
    temp = len(str(start))
    for i in range(len(str(start))):
        t = start%10
        s = s + t**temp
        start = start//10
    if s==l:
        a.append(l)
    s=0
    return arm(l+1,stop,s)

print(arm(start,stop,s))
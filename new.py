n = int(input())
s = []
for i in range(n):
    s.append(list(map(int,input().split())))
c = 0
for i in range(s):
    for j in range(i,s):
        if s[i].intersection(s[j])==0:
            c+=1

N,M = map(int,input().split())
lst = []
for i in range(N):
    lst.append(list(map(int,input().split())))
mahesh = 0
suresh = 0
i = 0
for k in lst:
    for j in k:
        if j==1:
            if i%2==0:
                mahesh += 1
            else :
                suresh += 1
        if lst[lst.index(k)][lst.index(j)+1]==0:
            i +=1
print(mahesh)
print(suresh)

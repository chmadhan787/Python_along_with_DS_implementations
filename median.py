l = list(map(int,input().split()))
if len(l)%2 == 0:
    median = (l[len(l)//2]+l[len(l)//2-1])/2
else:
    median = l[len(l)//2]
print(median)
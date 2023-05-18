n = int(input())
#using simple iteration
l = []
for i in range(2,n):
    c=0
    if n%i == 0:
        for j in range(2,i):
            if i%j==0:
                c+=1
        if c==0:
            l.append(i)
print(*l)

# without using the count variable
l = []
for i in range(2,n+1):
    if n%i == 0:
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            l.append(i)
print(l)


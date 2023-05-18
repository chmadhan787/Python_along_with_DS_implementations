s = 'AAABCDDDA'
n = len(s)
k=3
if n%k==0:
    for i in range(0,n,k):
        line = s[i:i+k]
        seen=set()
        for i in line:
            if i not in seen:
                print(i,end='')
                seen.add(i)
        print()


for i in range(0,n,k):
    p = set(s[i:i+k])
    print(''.join(p))




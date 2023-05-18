n = '126'
s = 0
for i in n:
    s += int(i)
print(s)

n = '126'
s = 0
for i in range(len(n)):
    s += int(n)%10
    n = int(n)//10
print(s)

s = 0
def digsum(n,s):
    if n==0:
        return s
    return digsum(n//10,s=s+n%10)
r = digsum(126,s)
print(r)

#sum of digits without using temporary variable
def digsum1(n):
    if n==0:
        return 0
    return n%10 + digsum1(n//10)
s = digsum1(126)
print(s)

n = '126'
s = 0
for i in n:
    s+=ord(i)-48
print(s)

n = '126'
print(sum(list(map(int,n.strip()))))

#one line recursive
n = 126
def digsum2(n):
    return 0 if n==0 else n%10 + digsum2(n//10)
print(digsum2(n))

#cool method
n = '126'
n = [int(i) for i in n]
print(sum(n))
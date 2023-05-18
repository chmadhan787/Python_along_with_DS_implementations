n = input()
#using general approach
temp = n
rev= 0
for i in range(len(n)):
    t = int(n)%10
    rev = rev*10+t
    n = int(n)//10
if str(rev) == temp:
    print(temp, ' is a palindrome')
else:
    print(temp, ' is not a palindrome')

#using reversed function
s=''.join(list(reversed(temp)))

print(temp,' is a palindrome') if s==temp else print(temp,' is not a palindrome')

#using slicing
print(temp,' is a palindrome') if temp[::-1] == temp else print(temp,' is not a palindrome')

#using recursion
n = 1221
r = 0
def palin(n,r):
    if n == 0:
        return r
    t = n%10
    r = r*10+t
    return palin(n//10,r)
print(n,' is a palindrome') if palin(n,r)==n else print(n,' is not a palindrome')

#by checking string from both sides
n='1221'
def checkpallin(n):
    for i in range(len(n)//2):
        if n[i] == n[len(n)-i-1]:
            return True
        else:
            return False
print(n,' is a palindrome') if checkpallin(n) else print(n,' is not a palindrome')

#reversing traversing each charachter
n = '1221'
r = ''
for i in n:
     r += i
print(n,' is a palindrome') if r==n else print(n,' is not a palindrome')


#using flags
j = -1
flag = 1
for i in range(len(n)//2):
    if n[i]!=n[j]:
        flag = 0
    j -= 1
print(n,' is a palindrome') if flag else print(n,' is not a palindrome')

#using list
k = len(n)
l = []
for i in range(k-1,-1,-1):
    l.append(n[i])
g = ''.join(l)
if g == n:
    print(n,' is a palindrome')
else:
    print(n,' is not a palindrome')

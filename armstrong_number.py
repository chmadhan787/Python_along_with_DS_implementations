#using iteration
n = int(input())
s = 0
t = str(n)
for i in range(len(t)):
    temp = n%10
    s+=temp**len(t)
    n = n//10
print(t, ' is an armstrong number') if s==int(t) else print(t,' is not an armstrong number')

#using recursion
n = 371
s = 0
tem = len(str(n))
def armstrong(n,s,tem):
    if n == 0:
        return s
    t = n%10
    s += t**tem
    return armstrong(n//10,s,tem)
print(n,' is an armstrong number') if n==armstrong(n,s,tem) else print(n,' is not an armstrong number')
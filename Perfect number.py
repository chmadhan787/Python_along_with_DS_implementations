
# using iteration :
n = int(input())
sum = 0
for i in range(1,n):
    if n%i == 0:
        sum += i
print(True if sum == n else False)

#using recursion :

temp = n
def  perfect_num(n,temp,sum = 0):
    if temp == 0:
        return sum
    if n%temp == 0:
        sum += temp
    return perfect_num(n,temp-1,sum)

print(True if perfect_num(n,n-1) == n else False)

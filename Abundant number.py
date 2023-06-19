# if the sum of factors of a number other than itself is greater than that
# number that the number is called abundant number.

n = int(input())
sum = 0
for i in range(1,n):
    if n%i == 0:
        sum += i
if sum > n:
    print('the number is abundant')
else :
    print('the number is not abundant')